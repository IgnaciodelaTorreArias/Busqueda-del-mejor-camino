# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 742)
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
        self.frame_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.ArbolDeBusqueda = QtWidgets.QTreeWidget(self.frame_5)
        self.ArbolDeBusqueda.setObjectName("ArbolDeBusqueda")
        self.ArbolDeBusqueda.headerItem().setText(0, "1")
        self.gridLayout_12.addWidget(self.ArbolDeBusqueda, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 1, 0, 1, 1)
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
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConectarNodos.setText(_translate("MainWindow", "Conectar"))
        self.label_3.setText(_translate("MainWindow", "Peso"))
        self.label.setText(_translate("MainWindow", "Nodo X"))
        self.label_2.setText(_translate("MainWindow", "Nodo Y"))
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
        self.label_4.setText(_translate("MainWindow", "Nombre del nodo"))
        self.CrearNodo.setText(_translate("MainWindow", "Crear"))
        self.label_15.setText(_translate("MainWindow", "Nombre original"))
        self.label_16.setText(_translate("MainWindow", "Nuevo Nombre"))
        self.CambiarNombre.setText(_translate("MainWindow", "Cambiar"))
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
