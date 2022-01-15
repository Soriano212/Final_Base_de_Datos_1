# Form implementation generated from reading ui file 'InicioSesion.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InicioSesion(object):
    def setupUi(self, InicioSesion):
        InicioSesion.setObjectName("InicioSesion")
        InicioSesion.resize(561, 402)
        font = QtGui.QFont()
        font.setPointSize(15)
        InicioSesion.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/usuario.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        InicioSesion.setWindowIcon(icon)
        
        # Tab Sesion
        
        self.tab_sesion = QtWidgets.QWidget()
        self.tab_sesion.setObjectName("tab_sesion")
        
        self.label_image_usuario = QtWidgets.QLabel(self.tab_sesion)
        self.label_image_usuario.setGeometry(QtCore.QRect(10, 110, 171, 161))
        self.label_image_usuario.setText("")
        self.label_image_usuario.setPixmap(QtGui.QPixmap("icons/usuario.png"))
        self.label_image_usuario.setScaledContents(True)
        self.label_image_usuario.setObjectName("label_image_usuario")
        
        self.label_email_sesion = QtWidgets.QLabel(self.tab_sesion)
        self.label_email_sesion.setGeometry(QtCore.QRect(210, 106, 331, 31))
        self.label_email_sesion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_email_sesion.setObjectName("label_email_sesion")
        
        self.label__contrasenia_sesion = QtWidgets.QLabel(self.tab_sesion)
        self.label__contrasenia_sesion.setGeometry(QtCore.QRect(210, 176, 331, 31))
        self.label__contrasenia_sesion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__contrasenia_sesion.setObjectName("label__contrasenia_sesion")
        
        self.txt_email_sesion = QtWidgets.QLineEdit(self.tab_sesion)
        self.txt_email_sesion.setGeometry(QtCore.QRect(210, 143, 330, 30))
        self.txt_email_sesion.setObjectName("txt_email_sesion")
        
        self.txt_contrasenia_sesion = QtWidgets.QLineEdit(self.tab_sesion)
        self.txt_contrasenia_sesion.setGeometry(QtCore.QRect(210, 210, 330, 30))
        self.txt_contrasenia_sesion.setObjectName("txt_contrasenia_sesion")
        self.txt_contrasenia_sesion.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        self.btn_ingresar = QtWidgets.QPushButton(self.tab_sesion)
        self.btn_ingresar.setGeometry(QtCore.QRect(310, 260, 121, 41))
        self.btn_ingresar.setObjectName("btn_ingresar")
        
        self.line_1 = QtWidgets.QFrame(self.tab_sesion)
        self.line_1.setGeometry(QtCore.QRect(0, 50, 561, 16))
        self.line_1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_1.setObjectName("line_1")
        
        self.label_titulo_1 = QtWidgets.QLabel(self.tab_sesion)
        self.label_titulo_1.setGeometry(QtCore.QRect(0, 0, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_titulo_1.setFont(font)
        self.label_titulo_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo_1.setObjectName("label_titulo_1")
        
        InicioSesion.addTab(self.tab_sesion, "")
        
        # Tab Registro
        
        self.tab_registro = QtWidgets.QWidget()
        self.tab_registro.setObjectName("tab_registro")
        
        self.line_2 = QtWidgets.QFrame(self.tab_registro)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 561, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.label__contrasenia_registro = QtWidgets.QLabel(self.tab_registro)
        self.label__contrasenia_registro.setGeometry(QtCore.QRect(210, 286, 331, 31))
        self.label__contrasenia_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__contrasenia_registro.setObjectName("label__contrasenia_registro")
        
        self.label_email_registro = QtWidgets.QLabel(self.tab_registro)
        self.label_email_registro.setGeometry(QtCore.QRect(210, 216, 331, 31))
        self.label_email_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_email_registro.setObjectName("label_email_registro")
        
        self.label_titulo_2 = QtWidgets.QLabel(self.tab_registro)
        self.label_titulo_2.setGeometry(QtCore.QRect(0, 0, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_titulo_2.setFont(font)
        self.label_titulo_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo_2.setObjectName("label_titulo_2")
        
        self.txt_nombre_registro = QtWidgets.QLineEdit(self.tab_registro)
        self.txt_nombre_registro.setGeometry(QtCore.QRect(210, 117, 330, 30))
        self.txt_nombre_registro.setObjectName("txt_nombre_registro")
        
        self.txt_usuario_registro = QtWidgets.QLineEdit(self.tab_registro)
        self.txt_usuario_registro.setGeometry(QtCore.QRect(210, 184, 330, 30))
        self.txt_usuario_registro.setObjectName("txt_usuario_registro")
        
        self.txt_email_registro = QtWidgets.QLineEdit(self.tab_registro)
        self.txt_email_registro.setGeometry(QtCore.QRect(210, 253, 330, 30))
        self.txt_email_registro.setObjectName("txt_email_registro")
        
        self.txt_contrasenia_registro = QtWidgets.QLineEdit(self.tab_registro)
        self.txt_contrasenia_registro.setGeometry(QtCore.QRect(210, 320, 330, 30))
        self.txt_contrasenia_registro.setObjectName("txt_contrasenia_registro")
        self.txt_contrasenia_registro.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        self.label_image_usuario_2 = QtWidgets.QLabel(self.tab_registro)
        self.label_image_usuario_2.setGeometry(QtCore.QRect(10, 86, 171, 161))
        self.label_image_usuario_2.setText("")
        self.label_image_usuario_2.setPixmap(QtGui.QPixmap("icons/lapiz.png"))
        self.label_image_usuario_2.setScaledContents(True)
        self.label_image_usuario_2.setObjectName("label_image_usuario_2")
        
        self.label_nombre_registro = QtWidgets.QLabel(self.tab_registro)
        self.label_nombre_registro.setGeometry(QtCore.QRect(210, 80, 331, 31))
        self.label_nombre_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_nombre_registro.setObjectName("label_nombre_registro")
        
        self.label__usuario_registro = QtWidgets.QLabel(self.tab_registro)
        self.label__usuario_registro.setGeometry(QtCore.QRect(210, 150, 331, 31))
        self.label__usuario_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label__usuario_registro.setObjectName("label__usuario_registro")
        
        self.btn_registro = QtWidgets.QPushButton(self.tab_registro)
        self.btn_registro.setGeometry(QtCore.QRect(40, 290, 121, 41))
        self.btn_registro.setObjectName("btn_registro")
        
        InicioSesion.addTab(self.tab_registro, "")

        self.retranslateUi(InicioSesion)
        InicioSesion.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InicioSesion)

    def retranslateUi(self, InicioSesion):
        _translate = QtCore.QCoreApplication.translate
        InicioSesion.setWindowTitle(_translate("InicioSesion", "Cuenta"))
        self.label_email_sesion.setText(_translate("InicioSesion", "Email"))
        self.label__contrasenia_sesion.setText(_translate("InicioSesion", "Contraseña"))
        self.btn_ingresar.setText(_translate("InicioSesion", "Ingresar"))
        self.label_titulo_1.setText(_translate("InicioSesion", "Bienvenido"))
        InicioSesion.setTabText(InicioSesion.indexOf(self.tab_sesion), _translate("InicioSesion", "Iniciar Sesión"))
        self.label__contrasenia_registro.setText(_translate("InicioSesion", "Contraseña"))
        self.label_email_registro.setText(_translate("InicioSesion", "Email"))
        self.btn_registro.setText(_translate("InicioSesion", "Registrarse"))
        self.label_titulo_2.setText(_translate("InicioSesion", "Registro"))
        self.label_nombre_registro.setText(_translate("InicioSesion", "Nombre"))
        self.label__usuario_registro.setText(_translate("InicioSesion", "Usuario"))
        InicioSesion.setTabText(InicioSesion.indexOf(self.tab_registro), _translate("InicioSesion", "Registrarse"))
