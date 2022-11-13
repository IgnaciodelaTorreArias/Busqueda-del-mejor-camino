from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from mainWindow import Ui_MainWindow
from Repository import Repository
from Busquedas import Busqueda

class searchingApp(QtWidgets.QMainWindow):
    def __init__(self, databaseName: str):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #logic classes
        self.repository = Repository(databaseName)
        self.busqueda = Busqueda(self.repository)

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

        #iniciar
        self.initializeEditTab()
        self.initializeDeleteTab()
        self.initializeSearchTab()
        self.retrieveData()

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
        self.busqueda.Explore(0, origin)
        Amplitud = self.busqueda.bestPath(destiny)
        self.busqueda.Explore(1, origin)
        Pesos = self.busqueda.bestPath(destiny)
        self.ui.BusquedaMovimientos.clear()
        self.ui.BusquedaPesos.clear()
        for id, peso in Amplitud.items():
            name = f"{self.repository.getName(id)}:{peso}-->"
            self.ui.BusquedaMovimientos.setText(self.ui.BusquedaMovimientos.text()+name)
        for id, peso in Pesos.items():
            name = f"{self.repository.getName(id)}:{peso}-->"
            self.ui.BusquedaPesos.setText(self.ui.BusquedaPesos.text()+name)

    def updateTableConexiones(self, item:tuple):
        last: int = self.ui.TablaConexiones.rowCount()
        self.ui.TablaConexiones.setRowCount(last+1)
        self.ui.TablaConexiones.setItem(last, 0, QtWidgets.QTableWidgetItem(str(item[0]))) #id origin
        self.ui.TablaConexiones.setItem(last, 1, QtWidgets.QTableWidgetItem(str(item[1]))) #id desitny
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

        for nodo in self.repository.getNodos():
            self.updateNodesComboBox(nodo[1])
            self.updateTableNodos(nodo)

        self.ui.TablaNodos.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.ui.TablaNodos.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Nombre"))

    def refreshConexiones(self):
        self.ui.TablaConexiones.clear()
        self.ui.TablaConexiones.setRowCount(0)

        for conexion in self.repository.getConexiones():
            self.updateTableConexiones(conexion)
        
        self.ui.TablaConexiones.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Nodo 1"))
        self.ui.TablaConexiones.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Nodo 2"))
        self.ui.TablaConexiones.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Peso"))

    def retrieveData(self):
        self.refreshNodes()
        self.refreshConexiones()

    def initializeEditTab(self):
        self.ui.CrearNodo.setEnabled(False)
        self.ui.CambiarNombre.setEnabled(False)
        self.ui.ConectarNodos.setEnabled(False)
        self.ui.Nombre.textChanged.connect(self.__createActive)
        
        self.ui.NuevoNombre.textChanged.connect(self.__changeNameActive)
        self.ui.NodoCambioNombre.currentIndexChanged.connect(self.__changeNameActive)
        
        self.ui.NodoOrigen.currentTextChanged.connect(self.__connectActive)
        self.ui.NodoDestino.currentTextChanged.connect(self.__connectActive)
        self.ui.Peso.textChanged.connect(self.__connectActive)
        self.ui.Peso.setValidator(QtGui.QIntValidator())
        
    def initializeDeleteTab(self):
        self.ui.EliminarNodo.setEnabled(False)
        self.ui.DesconectarNodos.setEnabled(False)
        self.ui.NodoEliminar.currentTextChanged.connect(self.__deleteActive)
        
        self.ui.NodoConexion1Eliminar.currentTextChanged.connect(self.__disconectActive)
        self.ui.NodoConexion2Eliminar.currentTextChanged.connect(self.__disconectActive)
        
        self.ui.NodoAislar.currentTextChanged.connect(self.__isolateActive)

    def initializeSearchTab(self):
        self.ui.Buscar.setEnabled(False)
        self.ui.NodoInicial.currentTextChanged.connect(self.__searchActive)
        self.ui.NodoObjetivo.currentTextChanged.connect(self.__searchActive)
        
    def __createActive(self):
        if len(self.ui.Nombre.text()):
            self.ui.CrearNodo.setEnabled(True)
        else:
            self.ui.CrearNodo.setEnabled(False)

    def __changeNameActive(self):
        if len(self.ui.NodoCambioNombre.currentText()) and len(self.ui.NuevoNombre.text()):
            self.ui.CambiarNombre.setEnabled(True)
        else:
            self.ui.CambiarNombre.setEnabled(False)

    def __connectActive(self):
        if self.ui.NodoOrigen.currentText() != self.ui.NodoDestino.currentText() and len(self.ui.Peso.text()):
            self.ui.ConectarNodos.setEnabled(True)
        else:
            self.ui.ConectarNodos.setEnabled(False)

    def __deleteActive(self):
        if len(self.ui.NodoEliminar.currentText()):
            self.ui.EliminarNodo.setEnabled(True)
        else:
            self.ui.EliminarNodo.setEnabled(False)

    def __disconectActive(self):
        if self.ui.NodoConexion1Eliminar.currentText() != self.ui.NodoConexion2Eliminar.currentText():
            self.ui.DesconectarNodos.setEnabled(True)
        else:
            self.ui.DesconectarNodos.setEnabled(False)

    def __isolateActive(self):
        if len(self.ui.NodoAislar.currentText()):
            self.ui.Aislar.setEnabled(True)
        else:
            self.ui.Aislar.setEnabled(False)

    def __searchActive(self):
        if self.ui.NodoInicial.currentText() != self.ui.NodoObjetivo.currentText():
            self.ui.Buscar.setEnabled(True)
        else:
            self.ui.Buscar.setEnabled(False)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    aplicacion = searchingApp(sys.argv[1] if len(sys.argv) > 1 else "Database.db") #Recibe el Nombre de la base de datos a utilizar
    aplicacion.show()
    sys.exit(app.exec())