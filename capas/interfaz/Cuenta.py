# Form implementation generated from reading ui file 'Cuenta.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Cuenta(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(745, 330)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/usuario.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        Form.setWindowIcon(icon)
        self.label_image_usuario = QtWidgets.QLabel(Form)
        self.label_image_usuario.setGeometry(QtCore.QRect(20, 20, 221, 221))
        self.label_image_usuario.setText("")
        self.label_image_usuario.setPixmap(QtGui.QPixmap("icons/usuario.png"))
        self.label_image_usuario.setScaledContents(True)
        self.label_image_usuario.setObjectName("label_image_usuario")
        self.label_cedula = QtWidgets.QLabel(Form)
        self.label_cedula.setGeometry(QtCore.QRect(250, 50, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_cedula.setFont(font)
        self.label_cedula.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cedula.setObjectName("label_cedula")
        self.label_titulo_ced = QtWidgets.QLabel(Form)
        self.label_titulo_ced.setGeometry(QtCore.QRect(320, 20, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_titulo_ced.setFont(font)
        self.label_titulo_ced.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo_ced.setObjectName("label_titulo_ced")
        self.label_nombre = QtWidgets.QLabel(Form)
        self.label_nombre.setGeometry(QtCore.QRect(250, 130, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_nombre.setFont(font)
        self.label_nombre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_nombre.setObjectName("label_nombre")
        self.label_titulo_nom = QtWidgets.QLabel(Form)
        self.label_titulo_nom.setGeometry(QtCore.QRect(320, 100, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_titulo_nom.setFont(font)
        self.label_titulo_nom.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo_nom.setObjectName("label_titulo_nom")
        self.label_email = QtWidgets.QLabel(Form)
        self.label_email.setGeometry(QtCore.QRect(250, 210, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_email.setFont(font)
        self.label_email.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_email.setObjectName("label_email")
        self.label_titulo_email = QtWidgets.QLabel(Form)
        self.label_titulo_email.setGeometry(QtCore.QRect(320, 180, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_titulo_email.setFont(font)
        self.label_titulo_email.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo_email.setObjectName("label_titulo_email")
        self.combo_box = QtWidgets.QComboBox(Form)
        self.combo_box.setGeometry(QtCore.QRect(434, 290, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.combo_box.setFont(font)
        self.combo_box.setObjectName("combo_box")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 270, 721, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.txt_nuevo = QtWidgets.QLineEdit(Form)
        self.txt_nuevo.setGeometry(QtCore.QRect(20, 290, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_nuevo.setFont(font)
        self.txt_nuevo.setObjectName("txt_nuevo")
        self.btn_cambiar = QtWidgets.QPushButton(Form)
        self.btn_cambiar.setGeometry(QtCore.QRect(590, 290, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_cambiar.setFont(font)
        self.btn_cambiar.setObjectName("btn_cambiar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cuenta"))
        self.label_cedula.setText(_translate("Form", "0150440378"))
        self.label_titulo_ced.setText(_translate("Form", "Cedula:"))
        self.label_nombre.setText(_translate("Form", "Alberto Soriano"))
        self.label_titulo_nom.setText(_translate("Form", "Nombre:"))
        self.label_email.setText(_translate("Form", "alberto.soriano@u.com"))
        self.label_titulo_email.setText(_translate("Form", "Email:"))
        self.combo_box.setItemText(0, _translate("Form", "Nombre"))
        self.combo_box.setItemText(1, _translate("Form", "Email"))
        self.combo_box.setItemText(2, _translate("Form", "Contraseña"))
        self.btn_cambiar.setText(_translate("Form", "Cambiar"))
