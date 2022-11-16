from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from View import Ui_MainWindow
from Repository import Repository
from Busquedas import Busqueda
import networkx as nx
import matplotlib.pyplot as plt

class searchingApp(QtWidgets.QMainWindow):
    def __init__(self, databaseName: str):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #logic classes
        self.repository = Repository(databaseName)
        self.busqueda = Busqueda(self.repository)
        self.Graph = nx.Graph()

        #buttons conections
        self.ui.CrearNodo.clicked.connect(self.crear)
        self.ui.CambiarNombre.clicked.connect(self.cambiarNombre)
        self.ui.ConectarNodos.clicked.connect(self.conectar)
        
        self.ui.EliminarNodo.clicked.connect(self.eliminar)
        self.ui.DesconectarNodos.clicked.connect(self.desconectar)
        self.ui.Aislar.clicked.connect(self.aislar)
        self.ui.Limpiar.clicked.connect(self.limpiar)
        self.ui.Reiniciar.clicked.connect(self.reiniciar)

        self.ui.Buscar.clicked.connect(self.buscar)

        #update data
        self.retrieveData()

    #funcionalidades del sistema
    def crear(self):
        nombre = self.ui.Nombre.text()
        if self.repository.buscarExistenciaPorNombre(nombre): return
        self.repository.agregarNodo(nombre)
        id = self.repository.getId(nombre)
        self.updateNodesComboBox(nombre)
        self.updateTableNodos((id,nombre))

    def cambiarNombre(self):
        id = self.repository.getId(self.ui.NodoCambioNombre.currentText())
        newName = self.ui.NuevoNombre.text()
        self.repository.cambiarNombre(id, newName)
        self.refreshNodes()

    def conectar(self):
        peso = int(self.ui.Peso.text())
        origen = self.repository.getId(self.ui.NodoOrigen.currentText())
        destino = self.repository.getId(self.ui.NodoDestino.currentText())
        if self.repository.seConectan(origen, destino):
            self.repository.editarConexion(origen, destino, peso)
            self.refreshConexiones()
            return
        self.repository.conectar(origen, destino, peso)
        self.updateTableConexiones((origen, destino, peso))
    
    def eliminar(self):
        id = self.repository.getId(self.ui.NodoEliminar.currentText())
        self.repository.eliminarNodo(id)
        self.retrieveData()

    def desconectar(self):
        id1 = self.repository.getId(self.ui.NodoConexion1Eliminar.currentText())
        id2 = self.repository.getId(self.ui.NodoConexion2Eliminar.currentText())
        self.repository.eliminarConexion(id1, id2)
        self.refreshConexiones()

    def aislar(self):
        id = self.repository.getId(self.ui.NodoAislar.currentText())
        self.repository.aislarNodo(id)
        self.refreshConexiones()
    
    def limpiar(self):
        self.repository.limpiar()
        self.retrieveData()

    def reiniciar(self):
        self.repository.reiniciar()
        self.retrieveData()

    def buscar(self):
        origin = self.repository.getId(self.ui.NodoInicial.currentText())
        destiny = self.repository.getId(self.ui.NodoObjetivo.currentText())
        self.busqueda.evaluate(origin)
        self.Amplitud, self.Peso = self.busqueda.bestPath(destiny)

        self.ui.BusquedaMovimientos.clear()
        self.ui.BusquedaPesos.clear()
        
        for name, peso in self.Amplitud.items():
            name = f"{name}:{peso}-->"
            self.ui.BusquedaMovimientos.setText(self.ui.BusquedaMovimientos.text()+name)
        for name, peso in self.Peso.items():
            name = f"{name}:{peso}-->"
            self.ui.BusquedaPesos.setText(self.ui.BusquedaPesos.text()+name)
        self.showGraph()

    def showGraph(self):
        AmplitudG = nx.Graph()
        WeightG = nx.Graph()
        nodes = set()
        for id, name in self.repository.getNodos():
            AmplitudG.add_node(name)
            WeightG.add_node(name)
            nodes.add(name)
        for nombre1, nombre2, peso in self.repository.getConexionesNombres():
            AmplitudG.add_edge(nombre1, nombre2, weight=peso)
            WeightG.add_edge(nombre1, nombre2, weight=peso)
        pos = nx.spring_layout(AmplitudG)
        #Amplitud subplot
        amplitudPlt = plt.subplot(121)
        amplitudPlt.title.set_text("Mejor camino en amplitud")
        #nodos
        nx.draw_networkx_nodes(AmplitudG, pos, nodelist=nodes-set(self.Amplitud.keys()), node_size=1500)
        nx.draw_networkx_nodes(AmplitudG, pos, nodelist=self.Amplitud.keys(), node_size=1500, node_color="red")
        nx.draw_networkx_labels(AmplitudG, pos)
        #conexiones
        nx.draw_networkx_edges(AmplitudG, pos)
        edge_labels = nx.get_edge_attributes(AmplitudG, "weight")
        nx.draw_networkx_edge_labels(AmplitudG, pos, edge_labels)
        #Weight subplot
        weightPlt = plt.subplot(122)
        weightPlt.title.set_text("Mejor camino en peso")
        #nodos
        nx.draw_networkx_nodes(WeightG, pos, nodelist=nodes-set(self.Peso.keys()), node_size=1500)
        nx.draw_networkx_nodes(WeightG, pos, nodelist=self.Peso.keys(), node_size=1500, node_color="red")
        nx.draw_networkx_labels(WeightG, pos)
        #conexiones
        nx.draw_networkx_edges(WeightG, pos)
        edge_labels = nx.get_edge_attributes(WeightG, "weight")
        nx.draw_networkx_edge_labels(WeightG, pos, edge_labels)
        plt.show()
        

    #Actualizacion desde controlador
    def updateTableConexiones(self, item:tuple):
        last: int = self.ui.TablaConexiones.rowCount()
        self.ui.TablaConexiones.setRowCount(last+1)
        self.ui.TablaConexiones.setItem(last, 0, QtWidgets.QTableWidgetItem(self.repository.getName(item[0]))) #id origin
        self.ui.TablaConexiones.setItem(last, 1, QtWidgets.QTableWidgetItem(self.repository.getName(item[1]))) #id desitny
        self.ui.TablaConexiones.setItem(last, 2, QtWidgets.QTableWidgetItem(str(item[2]))) #peso

    def updateTableNodos(self, item:tuple):
        last: int = self.ui.TablaNodos.rowCount()
        self.ui.TablaNodos.setRowCount(last+1)
        self.ui.TablaNodos.setItem(last, 0, QtWidgets.QTableWidgetItem(str(item[0]))) #id
        self.ui.TablaNodos.setItem(last, 1, QtWidgets.QTableWidgetItem(item[1])) #name

    def updateNodesComboBox(self, name:str):
        self.ui.NodoCambioNombre.addItem(name)
        self.ui.NodoOrigen.addItem(name)
        self.ui.NodoDestino.addItem(name)
        self.ui.NodoEliminar.addItem(name)
        self.ui.NodoConexion1Eliminar.addItem(name)
        self.ui.NodoConexion2Eliminar.addItem(name)
        self.ui.NodoAislar.addItem(name)
        self.ui.NodoInicial.addItem(name)
        self.ui.NodoObjetivo.addItem(name)
    
    #Actualizacion desde base de datos
    def refreshNodes(self):
        self.ui.TablaNodos.clear()
        self.ui.TablaNodos.setRowCount(0)

        self.ui.NodoCambioNombre.clear()
        self.ui.NodoOrigen.clear()
        self.ui.NodoDestino.clear()
        self.ui.NodoEliminar.clear()
        self.ui.NodoConexion1Eliminar.clear()
        self.ui.NodoConexion2Eliminar.clear()
        self.ui.NodoAislar.clear()
        self.ui.NodoInicial.clear()
        self.ui.NodoObjetivo.clear()

        for row, (id, nombre) in enumerate(self.repository.getNodos()):
            self.updateNodesComboBox(nombre)
            self.ui.TablaNodos.setRowCount(row+1)
            self.ui.TablaNodos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(id)))
            self.ui.TablaNodos.setItem(row, 1, QtWidgets.QTableWidgetItem(nombre))

        self.ui.TablaNodos.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.ui.TablaNodos.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Nombre"))

    def refreshConexiones(self):
        self.ui.TablaConexiones.clear()
        self.ui.TablaConexiones.setRowCount(0)

        for row, (name1, name2, peso) in enumerate(self.repository.getConexionesNombres()):
            self.ui.TablaConexiones.setRowCount(row+1)
            self.ui.TablaConexiones.setItem(row, 0, QtWidgets.QTableWidgetItem(name1))
            self.ui.TablaConexiones.setItem(row, 1, QtWidgets.QTableWidgetItem(name2))
            self.ui.TablaConexiones.setItem(row, 2, QtWidgets.QTableWidgetItem(str(peso)))
        
        self.ui.TablaConexiones.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Nodo 1"))
        self.ui.TablaConexiones.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Nodo 2"))
        self.ui.TablaConexiones.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Peso"))

    #Actualizacion completa
    def retrieveData(self):
        self.refreshNodes()
        self.refreshConexiones()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    aplicacion = searchingApp(sys.argv[1] if len(sys.argv) > 1 else "Database.db") #Recibe el Nombre de la base de datos a utilizar
    aplicacion.show()
    sys.exit(app.exec())