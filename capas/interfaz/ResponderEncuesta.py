# Form implementation generated from reading ui file 'ResponderEncuesta.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ResponderEncuesta(object):
    def setupUi(self, ResponderEncuesta, datos_preguntas: tuple[int, str, str, list[ tuple[int, str] | tuple[int, str, bool, list[tuple[int, str]]] ]]):
        ResponderEncuesta.setObjectName("ResponderEncuesta")
        ResponderEncuesta.resize(708, 866)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/editar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        
        self.label_titulo_encuesta = QtWidgets.QLabel(ResponderEncuesta)
        self.label_titulo_encuesta.setGeometry(QtCore.QRect(0, 60, 701, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_titulo_encuesta.setFont(font)
        self.label_titulo_encuesta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_titulo_encuesta.setObjectName("label_titulo_encuesta")
        
        self.scrollArea.setWidget(self.scroll_widget)
        
        self.lista_abiertas = []
        self.lista_opciones = []
        
        self.recargar_preguntas(datos_preguntas)
        
        ## Otros
        
        self.label_crear = QtWidgets.QLabel(ResponderEncuesta)
        self.label_crear.setGeometry(QtCore.QRect(0, 0, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_crear.setFont(font)
        self.label_crear.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_crear.setObjectName("label_crear")
        
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

    def recargar_preguntas(self, datos_preguntas: tuple[int, str, str, list[ tuple[int, str] | tuple[int, str, bool, list[tuple[int, str]]] ]]):
        
        self.scroll_widget.setParent(None)
        
        self.lista_abiertas = []
        self.lista_opciones = []
        
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setGeometry(QtCore.QRect(0, 0, 709, 649))
        self.scroll_widget.setObjectName("scroll_widget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        _translate = QtCore.QCoreApplication.translate
        if datos_preguntas is not None:
            self.label_titulo_encuesta.setText(_translate("CrearEncuesta", datos_preguntas[1]))
        else:
            self.label_titulo_encuesta.setText(_translate("CrearEncuesta", "Título"))
        
        if datos_preguntas is not None:
            for dato in datos_preguntas[3]:
                if len(dato) == 2:
                    # Group box texto
                    
                    group_box_texto = QtWidgets.QGroupBox(self.scroll_widget)
                    group_box_texto.setMinimumSize(QtCore.QSize(661, 145))
                    group_box_texto.setMaximumSize(QtCore.QSize(661, 145))
                    font = QtGui.QFont()
                    font.setPointSize(17)
                    group_box_texto.setFont(font)
                    group_box_texto.setObjectName("group_box_texto")
                    group_box_texto.setTitle(_translate("CrearEncuesta", str(dato[0])))
                    
                    label_pregunta_texto = QtWidgets.QLabel(group_box_texto)
                    label_pregunta_texto.setGeometry(QtCore.QRect(10, 30, 631, 31))
                    font = QtGui.QFont()
                    font.setPointSize(16)
                    font.setBold(True)
                    label_pregunta_texto.setFont(font)
                    label_pregunta_texto.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                    label_pregunta_texto.setObjectName("label_pregunta_texto")
                    label_pregunta_texto.setText(_translate("CrearEncuesta", str(dato[1])))
                    
                    txt_texto = QtWidgets.QPlainTextEdit(group_box_texto)
                    txt_texto.setGeometry(QtCore.QRect(10, 70, 631, 61))
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    txt_texto.setFont(font)
                    txt_texto.setObjectName("txt_texto")
                    
                    
                    self.verticalLayout.addWidget(group_box_texto)
                
                else:
                    ## Group box om 
                    tam = 81
                    
                    opciones = dato[3]
                    
                    if opciones is not None:
                        if len(opciones) > 0:
                            tam += (len(opciones)*30)
                    
                    group_box_om = QtWidgets.QGroupBox(self.scroll_widget)
                    group_box_om.setMinimumSize(QtCore.QSize(661, tam))
                    group_box_om.setMaximumSize(QtCore.QSize(661, tam))
                    font = QtGui.QFont()
                    font.setPointSize(17)
                    group_box_om.setFont(font)
                    group_box_om.setObjectName("group_box_om")
                    group_box_om.setTitle(_translate("CrearEncuesta", str(dato[0])))
                    
                    label_pregunta_om = QtWidgets.QLabel(group_box_om)
                    label_pregunta_om.setGeometry(QtCore.QRect(10, 30, 631, 31))
                    font = QtGui.QFont()
                    font.setPointSize(16)
                    font.setBold(True)
                    label_pregunta_om.setFont(font)
                    label_pregunta_om.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                    label_pregunta_om.setObjectName("label_pregunta_om")
                    label_pregunta_om.setText(_translate("CrearEncuesta", str(dato[1])))
                    
                    posy = 70
                    if opciones is not None:
                        for op in opciones:
                            if not dato[2]:
                                rdbtn_op = QtWidgets.QRadioButton(group_box_om)
                                rdbtn_op.setGeometry(QtCore.QRect(18, posy, 621, 31))
                                font = QtGui.QFont()
                                font.setPointSize(16)
                                rdbtn_op.setFont(font)
                                rdbtn_op.setObjectName("rdbtn_op")
                                rdbtn_op.setText(_translate("CrearEncuesta", op[1]))
                            else:
                                ckb_op = QtWidgets.QCheckBox(group_box_om)
                                ckb_op.setGeometry(QtCore.QRect(18, posy, 621, 31))
                                ckb_op.setObjectName("ckb_op")
                                ckb_op.setText(_translate("CrearEncuesta", op[1]))
                            posy += 30
                    
                    self.verticalLayout.addWidget(group_box_om)
        
        ## Agrega scroll_widget al scroll Area
        
        self.scrollArea.setWidget(self.scroll_widget)

    def retranslateUi(self, ResponderEncuesta):
        _translate = QtCore.QCoreApplication.translate
        ResponderEncuesta.setWindowTitle(_translate("ResponderEncuesta", "Responder Encuesta"))
        self.label_crear.setText(_translate("ResponderEncuesta", "Respondiendo Encuesta"))
        self.btn_publicar.setText(_translate("ResponderEncuesta", "Responder"))
