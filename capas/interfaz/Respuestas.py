# Form implementation generated from reading ui file 'Respuestas.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Respuestas(object):
    def setupUi(self, Respuestas, datos_usuarios: list[tuple[str, str]]):
        Respuestas.setObjectName("Respuestas")
        Respuestas.resize(1079, 776)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/noticias.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Respuestas.setWindowIcon(icon)
        
        self.scrollArea_usuario = QtWidgets.QScrollArea(Respuestas)
        self.scrollArea_usuario.setGeometry(QtCore.QRect(0, 58, 335, 717))
        self.scrollArea_usuario.setMinimumSize(QtCore.QSize(335, 717))
        self.scrollArea_usuario.setMaximumSize(QtCore.QSize(335, 717))
        self.scrollArea_usuario.setWidgetResizable(True)
        self.scrollArea_usuario.setObjectName("scrollArea_usuario")
        
        self.scroll_widget_usuarios = QtWidgets.QWidget()
        self.scroll_widget_usuarios.setGeometry(QtCore.QRect(0, 0, 333, 715))
        self.scroll_widget_usuarios.setObjectName("scroll_widget_usuarios")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scroll_widget_usuarios)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.scrollArea_usuario.setWidget(self.scroll_widget_usuarios)
        
        self.lista_box_usuarios = []
        self.recargar_usuarios(datos_usuarios)
        
        # Siguiente
        
        self.label_respuestas = QtWidgets.QLabel(Respuestas)
        self.label_respuestas.setGeometry(QtCore.QRect(0, 0, 1081, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_respuestas.setFont(font)
        self.label_respuestas.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_respuestas.setObjectName("label_respuestas")
        
        self.line_2 = QtWidgets.QFrame(Respuestas)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 1081, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        
        # Scroll area respuestas
        
        self.scrollArea_respuesta = QtWidgets.QScrollArea(Respuestas)
        self.scrollArea_respuesta.setGeometry(QtCore.QRect(334, 58, 745, 717))
        self.scrollArea_respuesta.setMinimumSize(QtCore.QSize(745, 717))
        self.scrollArea_respuesta.setMaximumSize(QtCore.QSize(745, 717))
        self.scrollArea_respuesta.setWidgetResizable(True)
        self.scrollArea_respuesta.setObjectName("scrollArea_respuesta")
        
        self.scroll_widget_respuesta = QtWidgets.QWidget()
        self.scroll_widget_respuesta.setGeometry(QtCore.QRect(0, 0, 743, 715))
        self.scroll_widget_respuesta.setObjectName("scroll_widget_respuesta")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scroll_widget_respuesta)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.scrollArea_respuesta.setWidget(self.scroll_widget_respuesta)
        

        self.retranslateUi(Respuestas)
        QtCore.QMetaObject.connectSlotsByName(Respuestas)

    def recargar_respuestas(self, datos_respuestas: list[tuple[str, str, str] | tuple[str, str, list[str]]]):
        self.scroll_widget_respuesta.setParent(None)
        
        self.scroll_widget_respuesta = QtWidgets.QWidget()
        self.scroll_widget_respuesta.setGeometry(QtCore.QRect(0, 0, 743, 715))
        self.scroll_widget_respuesta.setObjectName("scroll_widget_respuesta")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scroll_widget_respuesta)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        _translate = QtCore.QCoreApplication.translate
        
        for dato in datos_respuestas:
        
            if type(dato[2]) is str:
            
                group_box_respuesta = QtWidgets.QGroupBox(self.scroll_widget_respuesta)
                group_box_respuesta.setGeometry(QtCore.QRect(9, 302, 711, 155))
                group_box_respuesta.setMinimumSize(QtCore.QSize(711, 155))
                group_box_respuesta.setMaximumSize(QtCore.QSize(711, 155))
                font = QtGui.QFont()
                font.setPointSize(15)
                group_box_respuesta.setFont(font)
                group_box_respuesta.setTitle("")
                group_box_respuesta.setObjectName("group_box_respuesta")
                group_box_respuesta.setTitle(_translate("Respuestas", dato[0]))
                
                label_pregunta_box = QtWidgets.QLabel(group_box_respuesta)
                label_pregunta_box.setEnabled(True)
                label_pregunta_box.setGeometry(QtCore.QRect(10, 11, 691, 51))
                font = QtGui.QFont()
                font.setPointSize(17)
                font.setBold(True)
                label_pregunta_box.setFont(font)
                label_pregunta_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                label_pregunta_box.setObjectName("label_pregunta_box")
                label_pregunta_box.setText(_translate("Respuestas", dato[1]))
                
                plainTextEdit = QtWidgets.QPlainTextEdit(group_box_respuesta)
                plainTextEdit.setEnabled(True)
                plainTextEdit.setGeometry(QtCore.QRect(10, 50, 691, 91))
                plainTextEdit.setReadOnly(True)
                plainTextEdit.setObjectName("plainTextEdit")
                plainTextEdit.setPlainText(_translate("Respuestas", dato[2]))
                
                self.verticalLayout_2.addWidget(group_box_respuesta)
            
            elif type(dato[2]) is list:
            
                group_box_respuesta = QtWidgets.QGroupBox(self.scroll_widget_respuesta)
                group_box_respuesta.setGeometry(QtCore.QRect(9, 302, 711, 155))
                group_box_respuesta.setMinimumSize(QtCore.QSize(711, 155))
                group_box_respuesta.setMaximumSize(QtCore.QSize(711, 155))
                font = QtGui.QFont()
                font.setPointSize(15)
                group_box_respuesta.setFont(font)
                group_box_respuesta.setTitle("")
                group_box_respuesta.setObjectName("group_box_respuesta")
                group_box_respuesta.setTitle(_translate("Respuestas", dato[0]))
                
                label_pregunta_box = QtWidgets.QLabel(group_box_respuesta)
                label_pregunta_box.setEnabled(True)
                label_pregunta_box.setGeometry(QtCore.QRect(10, 11, 691, 51))
                font = QtGui.QFont()
                font.setPointSize(17)
                font.setBold(True)
                label_pregunta_box.setFont(font)
                label_pregunta_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
                label_pregunta_box.setObjectName("label_pregunta_box")
                label_pregunta_box.setText(_translate("Respuestas", dato[1]))
                
                res = ''
                cont = 0
                for da in dato[2]:
                    if cont == 0:
                        res += da
                    else:
                        res += '\n' + da
                    cont += 1
                
                plainTextEdit = QtWidgets.QPlainTextEdit(group_box_respuesta)
                plainTextEdit.setEnabled(True)
                plainTextEdit.setGeometry(QtCore.QRect(10, 50, 691, 91))
                plainTextEdit.setReadOnly(True)
                plainTextEdit.setObjectName("plainTextEdit")
                plainTextEdit.setPlainText(_translate("Respuestas", res))
                
                self.verticalLayout_2.addWidget(group_box_respuesta)
        
        self.scrollArea_respuesta.setWidget(self.scroll_widget_respuesta)

    def recargar_usuarios(self, datos_usuarios: list[tuple[str, str]]):
        
        self.scroll_widget_usuarios.setParent(None)
        self.lista_box_usuarios = []
        
        self.scroll_widget_usuarios = QtWidgets.QWidget()
        self.scroll_widget_usuarios.setGeometry(QtCore.QRect(0, 0, 333, 715))
        self.scroll_widget_usuarios.setObjectName("scroll_widget_usuarios")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scroll_widget_usuarios)
        self.verticalLayout.setObjectName("verticalLayout")
        
        _translate = QtCore.QCoreApplication.translate
        
        for dato in datos_usuarios:
            
            group_box_usuario = QtWidgets.QGroupBox(self.scroll_widget_usuarios)
            group_box_usuario.setMinimumSize(QtCore.QSize(300, 141))
            group_box_usuario.setMaximumSize(QtCore.QSize(300, 141))
            font = QtGui.QFont()
            font.setPointSize(17)
            group_box_usuario.setFont(font)
            group_box_usuario.setTitle("")
            group_box_usuario.setObjectName("group_box_usuario")
            
            btn_ver_box = QtWidgets.QPushButton(group_box_usuario)
            btn_ver_box.setGeometry(QtCore.QRect(200, 100, 91, 31))
            btn_ver_box.setObjectName("btn_ver_box")
            btn_ver_box.setCheckable(True)
            btn_ver_box.setText(_translate("Respuestas", "Ver"))
            
            label_nombre_box = QtWidgets.QLabel(group_box_usuario)
            label_nombre_box.setGeometry(QtCore.QRect(10, 0, 281, 51))
            font = QtGui.QFont()
            font.setPointSize(17)
            font.setBold(True)
            label_nombre_box.setFont(font)
            label_nombre_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_nombre_box.setObjectName("label_nombre_box")
            label_nombre_box.setText(_translate("Respuestas", dato[1]))
            
            label_cedula_box = QtWidgets.QLabel(group_box_usuario)
            label_cedula_box.setGeometry(QtCore.QRect(10, 50, 281, 51))
            font = QtGui.QFont()
            font.setPointSize(17)
            font.setBold(False)
            label_cedula_box.setFont(font)
            label_cedula_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
            label_cedula_box.setObjectName("label_cedula_box")
            label_cedula_box.setText(_translate("Respuestas", dato[0]))
            
            self.lista_box_usuarios.append((dato[0], btn_ver_box))
            self.verticalLayout.addWidget(group_box_usuario)
        
        self.scrollArea_usuario.setWidget(self.scroll_widget_usuarios)

    def retranslateUi(self, Respuestas):
        _translate = QtCore.QCoreApplication.translate
        Respuestas.setWindowTitle(_translate("Respuestas", "Respuestas"))
        
        self.label_respuestas.setText(_translate("Respuestas", "Repuestas"))
