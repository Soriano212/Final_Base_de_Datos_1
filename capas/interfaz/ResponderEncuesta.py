# Form implementation generated from reading ui file 'ResponderEncuesta.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ResponderEncuesta(object):
    def setupUi(self, ResponderEncuesta):
        ResponderEncuesta.setObjectName("ResponderEncuesta")
        ResponderEncuesta.resize(708, 866)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../icons/editar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ResponderEncuesta.setWindowIcon(icon)
        self.scrollArea = QtWidgets.QScrollArea(ResponderEncuesta)
        self.scrollArea.setGeometry(QtCore.QRect(0, 110, 711, 761))
        self.scrollArea.setMinimumSize(QtCore.QSize(711, 651))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setGeometry(QtCore.QRect(0, 0, 709, 759))
        self.scroll_widget.setObjectName("scroll_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_box_texto = QtWidgets.QGroupBox(self.scroll_widget)
        self.group_box_texto.setMinimumSize(QtCore.QSize(661, 145))
        self.group_box_texto.setMaximumSize(QtCore.QSize(661, 145))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.group_box_texto.setFont(font)
        self.group_box_texto.setObjectName("group_box_texto")
        self.label_pregunta_texto = QtWidgets.QLabel(self.group_box_texto)
        self.label_pregunta_texto.setGeometry(QtCore.QRect(10, 30, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_pregunta_texto.setFont(font)
        self.label_pregunta_texto.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_pregunta_texto.setObjectName("label_pregunta_texto")
        self.txt_texto = QtWidgets.QPlainTextEdit(self.group_box_texto)
        self.txt_texto.setGeometry(QtCore.QRect(10, 70, 631, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txt_texto.setFont(font)
        self.txt_texto.setObjectName("txt_texto")
        self.verticalLayout.addWidget(self.group_box_texto)
        self.group_box_om = QtWidgets.QGroupBox(self.scroll_widget)
        self.group_box_om.setMinimumSize(QtCore.QSize(661, 141))
        self.group_box_om.setMaximumSize(QtCore.QSize(661, 141))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.group_box_om.setFont(font)
        self.group_box_om.setObjectName("group_box_om")
        self.label_pregunta_om = QtWidgets.QLabel(self.group_box_om)
        self.label_pregunta_om.setGeometry(QtCore.QRect(10, 30, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_pregunta_om.setFont(font)
        self.label_pregunta_om.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_pregunta_om.setObjectName("label_pregunta_om")
        self.rdbtn_op1 = QtWidgets.QRadioButton(self.group_box_om)
        self.rdbtn_op1.setGeometry(QtCore.QRect(20, 70, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rdbtn_op1.setFont(font)
        self.rdbtn_op1.setObjectName("rdbtn_op1")
        self.rdbtn_op2 = QtWidgets.QRadioButton(self.group_box_om)
        self.rdbtn_op2.setGeometry(QtCore.QRect(20, 100, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rdbtn_op2.setFont(font)
        self.rdbtn_op2.setObjectName("rdbtn_op2")
        self.verticalLayout.addWidget(self.group_box_om)
        self.scrollArea.setWidget(self.scroll_widget)
        self.label_crear = QtWidgets.QLabel(ResponderEncuesta)
        self.label_crear.setGeometry(QtCore.QRect(0, 0, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_crear.setFont(font)
        self.label_crear.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_crear.setObjectName("label_crear")
        self.label_titulo_encuesta = QtWidgets.QLabel(ResponderEncuesta)
        self.label_titulo_encuesta.setGeometry(QtCore.QRect(0, 60, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_titulo_encuesta.setFont(font)
        self.label_titulo_encuesta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo_encuesta.setObjectName("label_titulo_encuesta")
        self.btn_publicar = QtWidgets.QPushButton(ResponderEncuesta)
        self.btn_publicar.setGeometry(QtCore.QRect(520, 13, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_publicar.setFont(font)
        self.btn_publicar.setObjectName("btn_publicar")
        self.line_2 = QtWidgets.QFrame(ResponderEncuesta)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 711, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(ResponderEncuesta)
        QtCore.QMetaObject.connectSlotsByName(ResponderEncuesta)

    def retranslateUi(self, ResponderEncuesta):
        _translate = QtCore.QCoreApplication.translate
        ResponderEncuesta.setWindowTitle(_translate("ResponderEncuesta", "Responder Encuesta"))
        self.group_box_texto.setTitle(_translate("ResponderEncuesta", "1"))
        self.label_pregunta_texto.setText(_translate("ResponderEncuesta", "Pregunta"))
        self.group_box_om.setTitle(_translate("ResponderEncuesta", "3"))
        self.label_pregunta_om.setText(_translate("ResponderEncuesta", "Pregunta"))
        self.rdbtn_op1.setText(_translate("ResponderEncuesta", "Opcion1"))
        self.rdbtn_op2.setText(_translate("ResponderEncuesta", "Opcion2"))
        self.label_crear.setText(_translate("ResponderEncuesta", "Respondiendo Encuesta"))
        self.label_titulo_encuesta.setText(_translate("ResponderEncuesta", "Título"))
        self.btn_publicar.setText(_translate("ResponderEncuesta", "Responder"))