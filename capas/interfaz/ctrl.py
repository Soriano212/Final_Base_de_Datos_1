import imp
import sys
from PyQt6 import QtCore, QtWidgets

from capas.negocios.usuario import Usuario

from capas.interfaz.DialogoAC import Ui_DialogoAC
from capas.interfaz.InicioSesion import Ui_InicioSesion
from capas.interfaz.Menu import Ui_Menu

usuario_cargado = None

class VenInicioSesion(QtWidgets.QTabWidget, Ui_InicioSesion):
    def __init__(self, parent=None) -> None:
        super(VenInicioSesion, self).__init__(parent)
        self.setupUi(self)
        self.ven_dialogo = VenDialogo()
        
        #Botones
        self.btn_registro.clicked.connect(self.registrarse)
        self.btn_ingresar.clicked.connect(self.ingresar)

    def registrarse(self):
        nom = self.txt_nombre_registro.text()
        usu = self.txt_usuario_registro.text()
        email = self.txt_email_registro.text()
        contra = self.txt_contrasenia_registro.text()
        
        men = ''
        
        if len(nom) < 3 or len(usu) < 3 or len(email) < 3 or len(contra) < 3:
            men += 'Los campos deben tener un largo mayor a 3.'
        
        if "@" not in email and "." not in email:
            if len(men) > 0: men += '\n'
            men += 'Email invalido.'
        
        if len(men) == 0:
            self.ven_dialogo.dialog("Registro", "Desea registrarse con los\ndatos ingresados", 0, 3)
            self.ven_dialogo.exec()
            
            if self.ven_dialogo.result() == 1:
                usuario = Usuario(nom, usu, email, contra)
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
        self.txt_usuario_registro.setText('')
        
        self.txt_email_sesion.setText('')
        self.txt_contrasenia_sesion.setText('')

class VenDialogo(QtWidgets.QDialog, Ui_DialogoAC):
    def __init__(self, parent=None) -> None:
        super(VenDialogo, self).__init__(parent)
        self.setupUi(self)

class VenMenu(QtWidgets.QMainWindow, Ui_Menu):
    pass

def abrir():
        app = QtWidgets.QApplication(sys.argv)
        myApp = VenInicioSesion()
        myApp.show()
        app.exec()