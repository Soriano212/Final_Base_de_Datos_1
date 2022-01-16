import sys
from PyQt6 import QtCore, QtWidgets
from capas.interfaz.CrearPregunta import Ui_CrearPregunta

from capas.negocios.usuario import Usuario
from capas.negocios.encuesta import *

from capas.interfaz.DialogoAC import Ui_DialogoAC
from capas.interfaz.InicioSesion import Ui_InicioSesion
from capas.interfaz.Menu import Ui_Menu
from capas.interfaz.CrearEncuesta import Ui_CrearEncuesta

class VenInicioSesion(QtWidgets.QTabWidget, Ui_InicioSesion):
    def __init__(self, parent=None) -> None:
        super(VenInicioSesion, self).__init__(parent)
        self.setupUi(self)
        self.ven_dialogo = VenDialogo()
        self.ven_menu = None
        
        #Botones
        self.btn_registro.clicked.connect(self.registrarse)
        self.btn_ingresar.clicked.connect(self.ingresar)

    def registrarse(self):
        ced = self.txt_cedula_registro.text()
        nom = self.txt_nombre_registro.text()
        email = self.txt_email_registro.text()
        contra = self.txt_contrasenia_registro.text()
        
        men = ''
        
        if len(nom) < 3 or len(ced) < 3 or len(email) < 3 or len(contra) < 3:
            men += 'Los campos deben tener un largo mayor a 3.'
        
        if "@" not in email and "." not in email:
            if len(men) > 0: men += '\n'
            men += 'Email invalido.'
        
        if len(men) == 0:
            self.ven_dialogo.dialog("Registro", "Desea registrarse con los datos ingresados.", 0, 3)
            self.ven_dialogo.exec()
            
            if self.ven_dialogo.result() == 1:
                usuario = Usuario(ced, nom, email, contra)
                res = usuario.registrarUsuario()
                
                match res:
                    case 1: 
                        self.ven_dialogo.dialog("Aviso", "Error al conectar con el servidor.\nContacte con el Administrador.", 1, 2)
                        self.ven_dialogo.show()
                    case 2: 
                        self.ven_dialogo.dialog("Aviso", "Ya hay un usuario registrado con ese email.", 1, 0)
                        self.ven_dialogo.show()
                    case 0:
                        self.ven_dialogo.dialog("Aviso", "Usuario registrado correctamente.\nAhora puede iniciar Sesion.", 1, 1)
                        self.ven_dialogo.show()
                        self.limpiar()
                        self.setCurrentIndex(0)
            
        else:
            self.ven_dialogo.dialog("Error", men, 1, 2)
            self.ven_dialogo.show()
            self.ven_dialogo.activateWindow()

    def ingresar(self):
        email = self.txt_email_sesion.text()
        contra = self.txt_contrasenia_sesion.text()
        
        usuario = Usuario.inicioSesion(Usuario, email, contra)
        
        if type(usuario) is Usuario:
            self.ven_dialogo.dialog("Aviso", "Inicio de Sesion correcto.", 1, 1)
            self.ven_menu = VenMenu(self.cerrar_sesion, usuario)
            self.hide()
            self.ven_menu.show()
            self.ven_dialogo.show()
            self.limpiar()
        else:
            match usuario:
                case 1:
                    self.ven_dialogo.dialog("Aviso", "Usuario o contraseña incorrectos.", 1, 2)
                    self.ven_dialogo.show()
                case 2:
                    self.ven_dialogo.dialog("Aviso", "Error al buscar Usuario.", 1, 2)
                    self.ven_dialogo.show()

    def limpiar(self):
        self.txt_email_registro.setText('')
        self.txt_nombre_registro.setText('')
        self.txt_contrasenia_registro.setText('')
        self.txt_cedula_registro.setText('')
        
        self.txt_email_sesion.setText('')
        self.txt_contrasenia_sesion.setText('')

    def cerrar_sesion(self):
        self.ven_menu.close()
        self.ven_menu = None
        self.show()

class VenDialogo(QtWidgets.QDialog, Ui_DialogoAC):
    def __init__(self, parent=None) -> None:
        super(VenDialogo, self).__init__(parent)
        self.setupUi(self)

class VenMenu(QtWidgets.QMainWindow, Ui_Menu):
    def __init__(self, funcion_cerrar, usuario: Usuario, parent=None) -> None:
        super(VenMenu, self).__init__(parent)
        self.setupUi(self)
        self.ven_dialogo = VenDialogo()
        self.usuario = usuario
        self.salir = funcion_cerrar
        
        self.label_Usuario.setText(self.usuario.nombre)
        
        ## Botones
        self.btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.btn_encuesta.clicked.connect(self.crear_encuesta)
        
        ## Menu
        self.action_cerrar_sesion.triggered.connect(self.cerrar_sesion)
        self.action_crear_encuesta.triggered.connect(self.crear_encuesta)

    def crear_encuesta(self):
        self.ven_crear_encuesta = VenCrearEncuesta(self.usuario)
        self.ven_crear_encuesta.show()
        self.ven_crear_encuesta.activateWindow()

    def cerrar_sesion(self):
        self.ven_dialogo.dialog("Aviso", "Desea Cerrar su Sesion actual?", 0, 0)
        self.ven_dialogo.exec()
        
        if self.ven_dialogo.result() == 1:
            self.salir()

class VenCrearPregunta(QtWidgets.QTabWidget, Ui_CrearPregunta):
    def __init__(self, encuesta: Encuesta, funcion_recargar, parent=None) -> None:
        super(VenCrearPregunta, self).__init__(parent)
        self.setupUi(self)
        
        self.ven_dialogo = VenDialogo()
        self.funcion_recargar = funcion_recargar
        
        self.encuesta = encuesta
        self.pregunta_texto = Abierta('Pregunta')
        self.pregunta_vf = Cerrada('Pregunta')
        self.pregunta_om = Cerrada('Pregunta')
        self.lista_opciones = []
        
        ## Botones
        self.btn_cambiar_texto.clicked.connect(self.cambiar_texto)
        self.btn_limpiar_texto.clicked.connect(self.limpiar_texto)
        self.btn_agregar_texto.clicked.connect(self.crear_texto)
        
        self.btn_cambiar_vf.clicked.connect(self.cambiar_vf)
        self.btn_limpiar_vf.clicked.connect(self.limpiar_vf)
        
        self.btn_cambiar_om.clicked.connect(self.cambiar_om)
        self.btn_limpiar_om.clicked.connect(self.limpiar_om)

    def crear_texto(self):
        self.ven_dialogo.dialog("Crear", "Desea crear la pregunta de texto ingresada?", 0, 0)
        self.ven_dialogo.exec()
        
        if self.ven_dialogo.result() == 1:
            self.encuesta.agregar_pregunta(self.pregunta_texto)
            self.funcion_recargar()
            self.close()

    def cambiar_texto(self):
        titulo = self.txt_pregunta_texto.text()
        if len(titulo) > 4:
            self.pregunta_texto.enunciado = titulo
            self.label_pregunta_texto_box.setText(titulo)
            self.txt_pregunta_texto.setText('')
            self.ven_dialogo.dialog("Correcto", "Titulo cambiado correctamente.", 1, 1)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del titulo es de 4.", 1, 2)
            self.ven_dialogo.show()

    def cambiar_vf(self):
        titulo = self.txt_pregunta_vf.text()
        if len(titulo) > 4:
            self.pregunta_vf.enunciado = titulo
            self.label_pregunta_vf_box.setText(titulo)
            self.txt_pregunta_vf.setText('')
            self.ven_dialogo.dialog("Correcto", "Titulo cambiado correctamente.", 1, 1)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del titulo es de 4.", 1, 2)
            self.ven_dialogo.show()

    def cambiar_om(self):
        titulo = self.txt_pregunta_om.text()
        if len(titulo) > 4:
            self.pregunta_om.enunciado = titulo
            self.label_pregunta_om_box.setText(titulo)
            self.txt_pregunta_om.setText('')
            self.ven_dialogo.dialog("Correcto", "Titulo cambiado correctamente.", 1, 1)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del titulo es de 4.", 1, 2)
            self.ven_dialogo.show()

    def limpiar_texto(self):
        self.txt_pregunta_texto.setText('')
        self.label_pregunta_texto_box.setText('Pregunta')
        self.pregunta_texto.enunciado = 'Pregunta'

    def limpiar_vf(self):
        self.txt_pregunta_vf.setText('')
        self.label_pregunta_vf_box.setText('Pregunta')
        self.pregunta_vf.enunciado = 'Pregunta'

    def limpiar_om(self):
        self.txt_pregunta_om.setText('')
        self.txt_opcion_om.setText('')
        self.label_pregunta_om_box.setText('Pregunta')
        self.pregunta_om.enunciado = 'Pregunta'
        self.lista_opciones = []

class VenCrearEncuesta(QtWidgets.QWidget, Ui_CrearEncuesta):
    def __init__(self, usuario: Usuario, parent=None) -> None:
        super(VenCrearEncuesta, self).__init__(parent)
        self.setupUi(self)
        
        self.usuario = usuario
        self.encuesta = Encuesta(self.label_titulo_encuesta.text())
        
        self.ven_dialogo = VenDialogo()
        self.ven_crear_pregunta = None
        
        ## Botones
        
        self.btn_cambiar.clicked.connect(self.titulo)
        self.btn_crear.clicked.connect(self.crear_pregunta)

    def crear_pregunta(self):
        self.ven_crear_pregunta = VenCrearPregunta(self.encuesta, self.recargar)
        self.ven_crear_pregunta.show()

    def titulo(self):
        titulo = self.txt_titulo.text()
        if len(titulo) > 4:
            self.encuesta.titulo = titulo
            self.label_titulo_encuesta.setText(titulo)
            self.txt_titulo.setText('')
            self.ven_dialogo.dialog("Correcto", "Titulo cambiado correctamente.", 1, 1)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del titulo es de 4.", 1, 2)
            self.ven_dialogo.show()

    def recargar(self):
        self.ven_dialogo.dialog("Correcto", "Pregunta Agregada.", 1, 1)
        self.ven_dialogo.show()

def abrir():
        app = QtWidgets.QApplication(sys.argv)
        myApp = VenInicioSesion()
        myApp.show()
        app.exec()