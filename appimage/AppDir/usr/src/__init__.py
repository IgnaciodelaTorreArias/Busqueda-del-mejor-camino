from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
from dataclasses import dataclass
import networkx as nx
from matplotlib import pyplot as plt


class Ui_MainWindow(object):
    #conexion de validadores y vista
    def initializeEditTab(self):
        self.CrearNodo.setEnabled(False)
        self.CambiarNombre.setEnabled(False)
        self.ConectarNodos.setEnabled(False)
        self.Nombre.textChanged.connect(self.__createActive)
        
        self.NuevoNombre.textChanged.connect(self.__changeNameActive)
        self.NodoCambioNombre.currentIndexChanged.connect(self.__changeNameActive)
        
        self.NodoOrigen.currentTextChanged.connect(self.__connectActive)
        self.NodoDestino.currentTextChanged.connect(self.__connectActive)
        self.Peso.textChanged.connect(self.__connectActive)
        self.Peso.setValidator(QtGui.QIntValidator())
        
    def initializeDeleteTab(self):
        self.EliminarNodo.setEnabled(False)
        self.DesconectarNodos.setEnabled(False)
        self.NodoEliminar.currentTextChanged.connect(self.__deleteActive)
        
        self.NodoConexion1Eliminar.currentTextChanged.connect(self.__disconectActive)
        self.NodoConexion2Eliminar.currentTextChanged.connect(self.__disconectActive)
        
        self.NodoAislar.currentTextChanged.connect(self.__isolateActive)

    def initializeSearchTab(self):
        self.Buscar.setEnabled(False)
        self.NodoInicial.currentTextChanged.connect(self.__searchActive)
        self.NodoObjetivo.currentTextChanged.connect(self.__searchActive)
        
    #Configuracion de validadores por el lado de la vista
    def __createActive(self):
        if len(self.Nombre.text()):
            self.CrearNodo.setEnabled(True)
        else:
            self.CrearNodo.setEnabled(False)

    def __changeNameActive(self):
        if len(self.NodoCambioNombre.currentText()) and len(self.NuevoNombre.text()):
            self.CambiarNombre.setEnabled(True)
        else:
            self.CambiarNombre.setEnabled(False)

    def __connectActive(self):
        if self.NodoOrigen.currentText() != self.NodoDestino.currentText() and len(self.Peso.text()):
            self.ConectarNodos.setEnabled(True)
        else:
            self.ConectarNodos.setEnabled(False)

    def __deleteActive(self):
        if len(self.NodoEliminar.currentText()):
            self.EliminarNodo.setEnabled(True)
        else:
            self.EliminarNodo.setEnabled(False)

    def __disconectActive(self):
        if self.NodoConexion1Eliminar.currentText() != self.NodoConexion2Eliminar.currentText():
            self.DesconectarNodos.setEnabled(True)
        else:
            self.DesconectarNodos.setEnabled(False)

    def __isolateActive(self):
        if len(self.NodoAislar.currentText()):
            self.Aislar.setEnabled(True)
        else:
            self.Aislar.setEnabled(False)

    def __searchActive(self):
        if self.NodoInicial.currentText() != self.NodoObjetivo.currentText():
            self.Buscar.setEnabled(True)
        else:
            self.Buscar.setEnabled(False)

    #Ventana
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 742)
        icon = QtGui.QIcon.fromTheme("go-last")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_11.addWidget(self.label_15, 0, 0, 1, 1)
        self.NuevoNombre = QtWidgets.QLineEdit(self.frame_4)
        self.NuevoNombre.setObjectName("NuevoNombre")
        self.gridLayout_11.addWidget(self.NuevoNombre, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 1, 0, 1, 1)
        self.CambiarNombre = QtWidgets.QPushButton(self.frame_4)
        self.CambiarNombre.setObjectName("CambiarNombre")
        self.gridLayout_11.addWidget(self.CambiarNombre, 1, 2, 1, 1)
        self.NodoCambioNombre = QtWidgets.QComboBox(self.frame_4)
        self.NodoCambioNombre.setObjectName("NodoCambioNombre")
        self.gridLayout_11.addWidget(self.NodoCambioNombre, 0, 1, 1, 2)
        self.gridLayout_6.addWidget(self.frame_4, 1, 0, 1, 1)
        self.frame_connect = QtWidgets.QFrame(self.tab)
        self.frame_connect.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_connect.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_connect.setObjectName("frame_connect")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_connect)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.NodoOrigen = QtWidgets.QComboBox(self.frame_connect)
        self.NodoOrigen.setObjectName("NodoOrigen")
        self.gridLayout_3.addWidget(self.NodoOrigen, 1, 1, 1, 3)
        self.ConectarNodos = QtWidgets.QPushButton(self.frame_connect)
        self.ConectarNodos.setObjectName("ConectarNodos")
        self.gridLayout_3.addWidget(self.ConectarNodos, 3, 3, 1, 1)
        self.NodoDestino = QtWidgets.QComboBox(self.frame_connect)
        self.NodoDestino.setObjectName("NodoDestino")
        self.gridLayout_3.addWidget(self.NodoDestino, 2, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.frame_connect)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_connect)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_connect)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.Peso = QtWidgets.QLineEdit(self.frame_connect)
        self.Peso.setObjectName("Peso")
        self.gridLayout_3.addWidget(self.Peso, 3, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_connect, 2, 0, 1, 1)
        self.frame_creacion = QtWidgets.QFrame(self.tab)
        self.frame_creacion.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_creacion.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_creacion.setObjectName("frame_creacion")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_creacion)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Nombre = QtWidgets.QLineEdit(self.frame_creacion)
        self.Nombre.setObjectName("Nombre")
        self.gridLayout_2.addWidget(self.Nombre, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_creacion)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.CrearNodo = QtWidgets.QPushButton(self.frame_creacion)
        self.CrearNodo.setObjectName("CrearNodo")
        self.gridLayout_2.addWidget(self.CrearNodo, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.frame_creacion, 0, 0, 1, 1)
        self.frame_info = QtWidgets.QFrame(self.tab)
        self.frame_info.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_info.setObjectName("frame_info")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_info)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.TablaNodos = QtWidgets.QTableWidget(self.frame_info)
        self.TablaNodos.setObjectName("TablaNodos")
        self.TablaNodos.setColumnCount(2)
        self.TablaNodos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaNodos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaNodos.setHorizontalHeaderItem(1, item)
        self.gridLayout_4.addWidget(self.TablaNodos, 0, 0, 1, 1)
        self.TablaConexiones = QtWidgets.QTableWidget(self.frame_info)
        self.TablaConexiones.setObjectName("TablaConexiones")
        self.TablaConexiones.setColumnCount(3)
        self.TablaConexiones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaConexiones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaConexiones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaConexiones.setHorizontalHeaderItem(2, item)
        self.gridLayout_4.addWidget(self.TablaConexiones, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_info, 3, 0, 1, 1)
        self.MostrarGrafo = QtWidgets.QPushButton(self.tab)
        self.MostrarGrafo.setObjectName("MostrarGrafo")
        self.gridLayout_6.addWidget(self.MostrarGrafo, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.NodoAislar = QtWidgets.QComboBox(self.frame_3)
        self.NodoAislar.setObjectName("NodoAislar")
        self.gridLayout_10.addWidget(self.NodoAislar, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 1, 1, 1, 1)
        self.Aislar = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Aislar.sizePolicy().hasHeightForWidth())
        self.Aislar.setSizePolicy(sizePolicy)
        self.Aislar.setObjectName("Aislar")
        self.gridLayout_10.addWidget(self.Aislar, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_3, 3, 0, 1, 1)
        self.frame_disconect = QtWidgets.QFrame(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_disconect.sizePolicy().hasHeightForWidth())
        self.frame_disconect.setSizePolicy(sizePolicy)
        self.frame_disconect.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_disconect.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_disconect.setObjectName("frame_disconect")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_disconect)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_disconect)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.NodoConexion1Eliminar = QtWidgets.QComboBox(self.frame_disconect)
        self.NodoConexion1Eliminar.setObjectName("NodoConexion1Eliminar")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NodoConexion1Eliminar)
        self.label_9 = QtWidgets.QLabel(self.frame_disconect)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.NodoConexion2Eliminar = QtWidgets.QComboBox(self.frame_disconect)
        self.NodoConexion2Eliminar.setObjectName("NodoConexion2Eliminar")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NodoConexion2Eliminar)
        self.DesconectarNodos = QtWidgets.QPushButton(self.frame_disconect)
        self.DesconectarNodos.setObjectName("DesconectarNodos")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.DesconectarNodos)
        self.gridLayout_8.addWidget(self.frame_disconect, 2, 0, 1, 1)
        self.frame_delete = QtWidgets.QFrame(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_delete.sizePolicy().hasHeightForWidth())
        self.frame_delete.setSizePolicy(sizePolicy)
        self.frame_delete.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_delete.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_delete.setObjectName("frame_delete")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_delete)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_delete)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.NodoEliminar = QtWidgets.QComboBox(self.frame_delete)
        self.NodoEliminar.setObjectName("NodoEliminar")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NodoEliminar)
        self.EliminarNodo = QtWidgets.QPushButton(self.frame_delete)
        self.EliminarNodo.setObjectName("EliminarNodo")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.EliminarNodo)
        self.gridLayout_8.addWidget(self.frame_delete, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 1)
        self.Reiniciar = QtWidgets.QPushButton(self.frame_2)
        self.Reiniciar.setObjectName("Reiniciar")
        self.gridLayout_9.addWidget(self.Reiniciar, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame_2, 5, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        self.Limpiar = QtWidgets.QPushButton(self.frame)
        self.Limpiar.setObjectName("Limpiar")
        self.gridLayout_7.addWidget(self.Limpiar, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.frame, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_busqueda = QtWidgets.QFrame(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_busqueda.sizePolicy().hasHeightForWidth())
        self.frame_busqueda.setSizePolicy(sizePolicy)
        self.frame_busqueda.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_busqueda.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_busqueda.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_busqueda.setObjectName("frame_busqueda")
        self.formLayout = QtWidgets.QFormLayout(self.frame_busqueda)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_busqueda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.NodoInicial = QtWidgets.QComboBox(self.frame_busqueda)
        self.NodoInicial.setObjectName("NodoInicial")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NodoInicial)
        self.label_6 = QtWidgets.QLabel(self.frame_busqueda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.NodoObjetivo = QtWidgets.QComboBox(self.frame_busqueda)
        self.NodoObjetivo.setObjectName("NodoObjetivo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.NodoObjetivo)
        self.Buscar = QtWidgets.QPushButton(self.frame_busqueda)
        self.Buscar.setObjectName("Buscar")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Buscar)
        self.BusquedaPesos = QtWidgets.QLabel(self.frame_busqueda)
        self.BusquedaPesos.setText("")
        self.BusquedaPesos.setObjectName("BusquedaPesos")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.BusquedaPesos)
        self.BusquedaMovimientos = QtWidgets.QLabel(self.frame_busqueda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BusquedaMovimientos.sizePolicy().hasHeightForWidth())
        self.BusquedaMovimientos.setSizePolicy(sizePolicy)
        self.BusquedaMovimientos.setText("")
        self.BusquedaMovimientos.setObjectName("BusquedaMovimientos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.BusquedaMovimientos)
        self.gridLayout_5.addWidget(self.frame_busqueda, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.initializeEditTab()
        self.initializeDeleteTab()
        self.initializeSearchTab()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Busqueda del mejor camino"))
        self.label_15.setText(_translate("MainWindow", "Nombre original"))
        self.label_16.setText(_translate("MainWindow", "Nuevo Nombre"))
        self.CambiarNombre.setText(_translate("MainWindow", "Cambiar"))
        self.ConectarNodos.setText(_translate("MainWindow", "Conectar"))
        self.label_3.setText(_translate("MainWindow", "Peso"))
        self.label.setText(_translate("MainWindow", "Nodo X"))
        self.label_2.setText(_translate("MainWindow", "Nodo Y"))
        self.label_4.setText(_translate("MainWindow", "Nombre del nodo"))
        self.CrearNodo.setText(_translate("MainWindow", "Crear"))
        item = self.TablaNodos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.TablaNodos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TablaConexiones.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Nodo 1"))
        item = self.TablaConexiones.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID Nodo 2"))
        item = self.TablaConexiones.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Peso"))
        self.MostrarGrafo.setText(_translate("MainWindow", "Mostrar grafo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Editar Nodos"))
        self.label_13.setText(_translate("MainWindow", "Nodo a desconectar"))
        self.label_12.setText(_translate("MainWindow", "Desconexion Total.\n"
"Esta opcion desconecta el nodo seleccionado de cualquier otro nodo al que estuviera conectado"))
        self.Aislar.setText(_translate("MainWindow", "Aislar"))
        self.label_8.setText(_translate("MainWindow", "Nodo 1"))
        self.label_9.setText(_translate("MainWindow", "Nado 2"))
        self.DesconectarNodos.setText(_translate("MainWindow", "Desconectar nodos"))
        self.label_7.setText(_translate("MainWindow", "Nodo a elminar"))
        self.EliminarNodo.setText(_translate("MainWindow", "Eliminar nodo"))
        self.label_11.setText(_translate("MainWindow", "Reiniciar Base de datos.\n"
"Esta opcion elminara todos los nodos, sus conexiones y ademas reiniciara los id\'s de los nodos."))
        self.Reiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.label_10.setText(_translate("MainWindow", "Limpiar Base de datos.\n"
"Esta opcion elminara todos los nodos y sus conexiones pero no reiniciara los id\'s de los nodos"))
        self.Limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Eliminaciones"))
        self.label_5.setText(_translate("MainWindow", "Inicio"))
        self.label_6.setText(_translate("MainWindow", "Objetivo"))
        self.Buscar.setText(_translate("MainWindow", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Buscar"))

class Repository:
    def __init__(self, database:str):
        self.__data = sqlite3.connect(database)
        self.__cursor = self.__data.cursor()
        self.__cursor.executescript("""
            CREATE TABLE IF NOT EXISTS nodos(
                id      INTEGER     PRIMARY KEY AUTOINCREMENT,
                name    VARCHAR(15) NOT NULL
            );

            CREATE INDEX IF NOT EXISTS nodesID ON nodos (id);
            
            CREATE TABLE IF NOT EXISTS conexiones(
                punto1  INTEGER NOT NULL,
                punto2  INTEGER NOT NULL,
                peso    INTEGER NOT NULL,
                FOREIGN KEY(punto1) REFERENCES nodos(id)
                FOREIGN KEY(punto2) REFERENCES nodos(id)
            );
        """)
        self.__data.commit()

    #Consulta de existencia
    def buscarExistenciaPorNombre(self, name:str)-> bool:
        self.__cursor.execute(f"SELECT * FROM nodos WHERE name = '{name}'")
        if len(self.__cursor.fetchall()) == 0: return False
        return True

    def buscarExistenciaPorId(self, id:int)-> bool:
        self.__cursor.execute(f"SELECT * FROM nodos WHERE id = {id}")
        if len(self.__cursor.fetchall()) == 0: return False
        return True

    def seConectan(self, id1:int, id2:int)->bool:
        self.__cursor.execute(f"SELECT * FROM conexiones WHERE (punto1 = {id1} AND punto2 = {id2}) OR (punto1 = {id2} AND punto2 = {id1})")
        if len(self.__cursor.fetchall()) == 0: return False
        return True

    #Creacion y modificacion de nodos
    def agregarNodo(self, name:str)-> None:
        self.__cursor.execute(f"INSERT INTO nodos (name) VALUES ('{name}')")
        self.__data.commit()

    def cambiarNombre(self, id:int, newName:str)->None:
        self.__cursor.execute(f"UPDATE nodos SET name = '{newName}' WHERE id = {id}")

    #Creacion y modificacion de conexiones
    def conectar(self, id1: int, id2:int, peso:int)-> None:
        self.__cursor.execute(f"INSERT INTO conexiones (punto1, punto2, peso) VALUES ({id1}, {id2}, {peso})")
        self.__data.commit()

    def editarConexion(self, id1:int, id2:int, peso:int)-> None:
        self.__cursor.execute(f"UPDATE conexiones SET peso = {peso} WHERE (punto1={id1} AND punto2={id2}) OR (punto1={id2} AND punto2={id1})")
        self.__data.commit()

    #Eliminacion de datos
    def eliminarNodo(self, id:int)-> None:
        self.aislarNodo(id)
        self.__cursor.execute(f"DELETE FROM nodos WHERE id = {id}")
        self.__data.commit()

    def eliminarConexion(self, id1:int, id2:int)-> None:
        self.__cursor.execute(f"DELETE FROM conexiones WHERE (punto1={id1} AND punto2={id2}) OR (punto1={id2} AND punto2={id1})")
        self.__data.commit()

    def aislarNodo(self, id:int)-> None:
        self.__cursor.execute(f"DELETE FROM conexiones WHERE punto1 = {id} OR punto2 = {id}")
        self.__data.commit()

    #Recuperacion de datos
    def getNodos(self)-> list:
        self.__cursor.execute("SELECT id, name FROM nodos")
        return self.__cursor.fetchall()

    def getConexiones(self)-> list:
        self.__cursor.execute("SELECT punto1, punto2, peso FROM conexiones")
        return self.__cursor.fetchall()

    def getConexionesNombres(self)-> list:
        self.__cursor.execute("SELECT a.name, b.name, peso FROM conexiones INNER JOIN nodos a ON a.id = punto1 INNER JOIN nodos b ON b.id = punto2;")
        return self.__cursor.fetchall()

    def getName(self, id:int )->str:
        self.__cursor.execute(f"SELECT name FROM nodos WHERE id = {id}")
        name = self.__cursor.fetchall()
        if len(name) == 0: return None
        return name[0][0]

    def getId(self, name:str)->int:
        self.__cursor.execute(f"SELECT id FROM nodos WHERE name = '{name}'")
        ID = self.__cursor.fetchall()
        if len(ID) == 0: return None
        return ID[0][0]

    def whoConnects(self, origin:int )->list:
        self.__cursor.execute(f"SELECT punto1, punto2, peso FROM conexiones WHERE punto1 = {origin} OR punto2 = {origin} ORDER BY peso")
        result = []
        for item in self.__cursor.fetchall():
            result.append((item[1], item[2])) if item[0] == origin else result.append((item[0], item[2]))
        return result

    #Limpieza de base de datos
    def limpiar(self)->None:
        self.__cursor.execute(f"DELETE FROM conexiones")
        self.__cursor.execute(f"DELETE FROM nodos")
        self.__data.commit()

    def reiniciar(self)->None:
        self.__cursor.execute(f"DELETE FROM conexiones")
        self.__cursor.execute(f"DELETE FROM nodos")
        self.__cursor.execute(f"UPDATE sqlite_sequence SET seq = 0 WHERE name = 'nodos'")
        self.__data.commit()

class Busqueda:
    def __init__(self, repo:Repository):
        self.repo = repo
        self.amplitudPath = dict()
        self.weightPath = dict()
        self.origin = None

    def evaluate(self, origin:int):
        self.origin = origin
        self.amplitudPath =  self.__Explore(self.__visitA)
        self.weightPath = self.__Explore(self.__visitP)

    def __visitA(self, id:int):
        self.toVisit.remove(id) #Se marca como visitado
        level = self.path[id]['weight']

        for nextId, peso in self.repo.whoConnects(id):#Se evaluan los nodos a los que se conecta
            if level+1 < self.path[nextId]['weight']:#Se intercambia el mejor camino hacia los siguientes nodos, hasta encontrar el minimo
                self.path[nextId]['weight'] = level+1
                self.path[nextId]['previous'] = id
    
    def __visitP(self, id:int):
        self.toVisit.remove(id)
        level = self.path[id]['weight']

        for nextId, peso in self.repo.whoConnects(id):
            if level+peso < self.path[nextId]['weight']:
                self.path[nextId]['weight'] = level+peso
                self.path[nextId]['previous'] = id

    def __Explore(self, func):
        self.toVisit:set = set(id for id, peso in self.repo.getNodos()) #Control para evitar bucles
        self.path = {id:{'weight':sys.maxsize, 'previous':None} for id, peso in self.repo.getNodos()} #Para guardar los resultados de cada visita
        
        self.path[self.origin]['weight'] = 0

        func(self.origin)
        while(len(self.toVisit)): #Investigacion de todos los nodos
            minKey = None
            for key in self.toVisit:
                if minKey == None:
                    minKey = key
                    continue
                if self.path[key]['weight'] < self.path[minKey]['weight']: minKey = key
            func(minKey)
        return self.path

    def __bestPath(self, destiny:int, path:dict)->dict:
        bestPathId = [destiny]
        while path[bestPathId[-1]]['previous'] is not None: #Se regresa desde el nodo destino hasta el origen
            bestPathId.append(path[bestPathId[-1]]['previous'])
        bestPathId.reverse()

        bestPath = dict()
        try:
            while(True):
                id = bestPathId.pop(0)
                bestPath[self.repo.getName(id)] = path[id]['weight']
        except:
            pass
        return bestPath

    #Mejor camnino en amplitud y mejor camino en peso
    def bestPath(self, destiny:int)->tuple:
        return (self.__bestPath(destiny, self.amplitudPath), self.__bestPath(destiny, self.weightPath))

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
        self.ui.MostrarGrafo.clicked.connect(self.mostrarGrafo)
        
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
    
    def mostrarGrafo(self):
        G = nx.Graph()
        for id, name in self.repository.getNodos():
            G.add_node(name)
        for name1, name2, peso in self.repository.getConexionesNombres():
            G.add_edge(name1, name2, weight=peso)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=1500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.title("Grafo de conexiones")
        plt.show()

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
        if not self.busqueda.origin == origin: self.busqueda.evaluate(origin)
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
def main():
    app = QtWidgets.QApplication([])
    aplicacion = searchingApp(sys.argv[1] if len(sys.argv) > 1 else "Database.db") #Recibe el Nombre de la base de datos a utilizar
    aplicacion.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()