# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(482, 695)
        font = QtGui.QFont()
        font.setPointSize(10)
        Menu.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/casa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        Menu.setWindowIcon(icon)
        Menu.setStyleSheet("background-color: rgb(255, 255, 255);")
        Menu.setWindowFilePath("")
        
        self.centralwidget = QtWidgets.QWidget(Menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_image_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_image_usuario.setGeometry(QtCore.QRect(10, 80, 110, 110))
        self.label_image_usuario.setText("")
        self.label_image_usuario.setPixmap(QtGui.QPixmap("icons/usuario.png"))
        self.label_image_usuario.setScaledContents(True)
        self.label_image_usuario.setObjectName("label_image_usuario")
        
        self.label_Usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_Usuario.setGeometry(QtCore.QRect(130, 110, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_Usuario.setFont(font)
        self.label_Usuario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Usuario.setObjectName("label_Usuario")
        
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(160, 10, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(10, 60, 461, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_1.setObjectName("line_1")
        
        self.btn_todas_encuestas = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_todas_encuestas.setGeometry(QtCore.QRect(30, 230, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.btn_todas_encuestas.setFont(font)
        self.btn_todas_encuestas.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.495, x2:0, y2:0.438, stop:0.0909091 rgba(255, 170, 255, 255), stop:0.988636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/aplicaciones.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_todas_encuestas.setIcon(icon1)
        self.btn_todas_encuestas.setIconSize(QtCore.QSize(77, 80))
        self.btn_todas_encuestas.setObjectName("btn_todas_encuestas")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.btn_encuesta = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_encuesta.setGeometry(QtCore.QRect(30, 340, 421, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.btn_encuesta.setFont(font)
        self.btn_encuesta.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.495, x2:0, y2:0.438, stop:0.0909091 rgb(161, 255, 191), stop:0.988636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/editar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_encuesta.setIcon(icon2)
        self.btn_encuesta.setIconSize(QtCore.QSize(80, 80))
        self.btn_encuesta.setObjectName("btn_encuesta")
        self.btn_mis_encuestas = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_mis_encuestas.setGeometry(QtCore.QRect(30, 450, 421, 101))
        
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.btn_mis_encuestas.setFont(font)
        self.btn_mis_encuestas.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.495, x2:0, y2:0.438, stop:0.0909091 rgb(255, 228, 148), stop:0.988636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/noticias.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_mis_encuestas.setIcon(icon3)
        self.btn_mis_encuestas.setIconSize(QtCore.QSize(80, 80))
        self.btn_mis_encuestas.setObjectName("btn_mis_encuestas")
        self.btn_cerrar_sesion = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btn_cerrar_sesion.setGeometry(QtCore.QRect(30, 560, 421, 101))
        
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        self.btn_cerrar_sesion.setFont(font)
        self.btn_cerrar_sesion.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.495, x2:0, y2:0.438, stop:0.0909091 rgb(113, 208, 255), stop:0.988636 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/hacia-atras.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_cerrar_sesion.setIcon(icon4)
        self.btn_cerrar_sesion.setIconSize(QtCore.QSize(80, 80))
        self.btn_cerrar_sesion.setObjectName("btn_cerrar_sesion")
        
        Menu.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 482, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"selection-background-color: rgb(191, 191, 191);")
        self.menubar.setObjectName("menubar")
        
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        
        self.menuCuenta = QtWidgets.QMenu(self.menubar)
        self.menuCuenta.setObjectName("menuCuenta")
        
        Menu.setMenuBar(self.menubar)
        
        self.action_todas_ecuestas = QtGui.QAction(Menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_todas_ecuestas.setFont(font)
        self.action_todas_ecuestas.setObjectName("action_todas_ecuestas")
        self.action_crear_encuesta = QtGui.QAction(Menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_crear_encuesta.setFont(font)
        self.action_crear_encuesta.setObjectName("action_crear_encuesta")
        self.action_mis_Encuestas = QtGui.QAction(Menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_mis_Encuestas.setFont(font)
        self.action_mis_Encuestas.setObjectName("action_mis_Encuestas")
        self.action_administrar = QtGui.QAction(Menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_administrar.setFont(font)
        self.action_administrar.setObjectName("action_administrar")
        self.action_cerrar_sesion = QtGui.QAction(Menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action_cerrar_sesion.setFont(font)
        self.action_cerrar_sesion.setObjectName("action_cerrar_sesion")
        
        self.menuMenu.addAction(self.action_todas_ecuestas)
        self.menuMenu.addAction(self.action_crear_encuesta)
        self.menuMenu.addAction(self.action_mis_Encuestas)
        self.menuCuenta.addAction(self.action_administrar)
        self.menuCuenta.addAction(self.action_cerrar_sesion)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuCuenta.menuAction())

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menú"))
        self.label_Usuario.setText(_translate("Menu", "Juan Javier Malo Vega"))
        self.label_titulo.setText(_translate("Menu", "Menú"))
        self.btn_todas_encuestas.setText(_translate("Menu", "  Todas las Encuestas"))
        self.btn_encuesta.setText(_translate("Menu", "    Crear Encuesta"))
        self.btn_mis_encuestas.setText(_translate("Menu", "     Mis Encuestas"))
        self.btn_cerrar_sesion.setText(_translate("Menu", "     Cerrar Sesión"))
        self.menuMenu.setTitle(_translate("Menu", "Menú"))
        self.menuCuenta.setTitle(_translate("Menu", "Cuenta"))
        self.action_todas_ecuestas.setText(_translate("Menu", "Todas las Ecuestas"))
        self.action_crear_encuesta.setText(_translate("Menu", "Crear Encuesta"))
        self.action_mis_Encuestas.setText(_translate("Menu", "Mis Encuestas"))
        self.action_administrar.setText(_translate("Menu", "Administrar"))
        self.action_cerrar_sesion.setText(_translate("Menu", "Cerrar Sesión"))
