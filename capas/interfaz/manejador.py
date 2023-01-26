import sys
from PyQt6 import QtCore, QtWidgets
from capas.interfaz.Cuenta import Ui_Cuenta

from capas.interfaz.DialogoAC import Ui_DialogoAC
from capas.interfaz.InicioSesion import Ui_InicioSesion
from capas.interfaz.Menu import Ui_Menu
from capas.interfaz.CrearEncuesta import Ui_CrearEncuesta
from capas.interfaz.CrearPregunta import Ui_CrearPregunta
from capas.interfaz.MisEncuestas import Ui_MisEncuestas
from capas.interfaz.ResponderEncuesta import Ui_ResponderEncuesta
from capas.interfaz.Respuestas import Ui_Respuestas
from capas.interfaz.TodasEncuestas import Ui_TodasEncuestas

from capas.negocios.usuario import *
from capas.negocios.encuesta import *
from capas.negocios.respuesta import *

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
        
        if "@" not in email or "." not in email:
            if len(men) > 0: men += '\n'
            men += 'Email invalido.'
        
        valced = lambda id: sum([ x if x <= 9 else x-9 for x in [ int(id[i]) * ([2,1]*len(id))[i] for i in range(len(id)) ] ]) % 10 == 0 and len(id) == 10
        
        if not valced(ced):
            if len(men) > 0: men += '\n'
            men += 'Cedula invalida.'
        
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
                        self.ven_dialogo.dialog("Aviso", "Ya hay un usuario registrado con ese email\n o con esa cedula.", 1, 0)
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
            self.ven_menu = VenMenu(self.cerrar_sesion, usuario)
            self.hide()
            if self.comboBox.currentIndex() == 0:
                self.ven_dialogo.dialog("Aviso", "Inicio de Sesion correcto.\nSesion de Encuestado", 1, 1)
                Usuario.cambioUsuario(Usuario, 2)
                self.ven_menu.btn_mis_encuestas.setEnabled(False)
                self.ven_menu.btn_encuesta.setEnabled(False)
                self.ven_menu.action_crear_encuesta.setEnabled(False)
                self.ven_menu.action_mis_Encuestas.setEnabled(False)
            else:
                self.ven_dialogo.dialog("Aviso", "Inicio de Sesion correcto.\nSesion de Creador", 1, 1)
                Usuario.cambioUsuario(Usuario, 3)
                self.ven_menu.btn_mis_encuestas.setEnabled(True)
                self.ven_menu.btn_encuesta.setEnabled(True)
                self.ven_menu.action_crear_encuesta.setEnabled(True)
                self.ven_menu.action_mis_Encuestas.setEnabled(True)
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
        Usuario.cambioUsuario(Usuario, 1)
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
        self.btn_todas_encuestas.clicked.connect(self.todas_encuestas)
        self.btn_mis_encuestas.clicked.connect(self.mis_encuestas)
        
        ## Menu
        self.action_cerrar_sesion.triggered.connect(self.cerrar_sesion)
        self.action_crear_encuesta.triggered.connect(self.crear_encuesta)
        self.action_todas_ecuestas.triggered.connect(self.todas_encuestas)
        self.action_mis_Encuestas.triggered.connect(self.mis_encuestas)
        self.action_administrar.triggered.connect(self.cuenta)

    def crear_encuesta(self):
        res = self.usuario.pruedeCrearEncuesta()
        if res == 1:
            self.ven_crear_encuesta = VenCrearEncuesta(self.usuario, self.publicar_encuesta)
            self.ven_crear_encuesta.show()
            self.ven_crear_encuesta.activateWindow()
        elif res == 0:
            self.ven_dialogo.dialog("Aviso", "El usuario ya no puede crear mas encuestas.\nLimite: 3", 1, 2)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "Error en la base de datos.", 1, 4)
            self.ven_dialogo.show()

    def todas_encuestas(self):
        self.ven_todas_encuestas = VenTodasEncuestas(self.usuario.cedula)
        self.ven_todas_encuestas.show()
        self.ven_todas_encuestas.activateWindow()

    def mis_encuestas(self):
        self.ven_mis_encuestas = VenMisEncuestas(self.usuario)
        self.ven_mis_encuestas.show()
        self.ven_mis_encuestas.activateWindow()

    def cerrar_sesion(self):
        self.ven_dialogo.dialog("Aviso", "Desea Cerrar su Sesion actual?", 0, 0)
        self.ven_dialogo.exec()
        
        if self.ven_dialogo.result() == 1:
            self.salir()

    def publicar_encuesta(self):
        self.ven_dialogo.dialog("Correcto", "Encuesta publicada Correctamente.", 1, 1)
        self.ven_dialogo.show()

    def cuenta(self):
        self.ven_cuenta = VenCuenta(self.usuario, self.cambio_nombre)
        self.ven_cuenta.show()

    def cambio_nombre(self):
        self.label_Usuario.setText(self.usuario.nombre)

class VenCuenta(QtWidgets.QWidget, Ui_Cuenta):
    def __init__(self, usuario: Usuario, funcion_cambio, parent=None) -> None:
        super(VenCuenta, self).__init__(parent)
        self.setupUi(self)
        self.ven_dialogo = VenDialogo()
        self.usuario = usuario
        self.cambio = funcion_cambio
        self.datos()
        
        self.btn_cambiar.clicked.connect(self.cambiar)

    def datos(self):
        self.label_cedula.setText(self.usuario.cedula)
        self.label_nombre.setText(self.usuario.nombre)
        self.label_email.setText(self.usuario.email)

    def cambiar(self):
        texto = self.txt_nuevo.text()
        if len(texto)>=3:
            index = self.combo_box.currentIndex()
            val = True
            
            if index == 1:
                if "@" not in texto or "." not in texto: val = False
            
            if val:
                self.ven_dialogo.dialog("Aviso", "Desea cambiar su "+self.combo_box.currentText()+" con:\n'"+texto+"'.", 0, 0)
                self.ven_dialogo.exec()
                
                if self.ven_dialogo.result() == 1:
                    res = self.usuario.actualizar(index, texto)
                    match res:
                        case 0:
                            self.ven_dialogo.dialog("Correcto", "Valores actualizados correctamente.", 1, 1)
                            self.ven_dialogo.show()
                            self.txt_nuevo.setText('')
                            self.cambio()
                            self.datos()
                        case 1:
                            self.ven_dialogo.dialog("Error", "Error en la base de datos.", 1, 2)
                            self.ven_dialogo.show()
                        case 2:
                            self.ven_dialogo.dialog("Error", "El email nuevo ya esta usado por otro usuario.", 1, 2)
                            self.ven_dialogo.show()
                        case -1:
                            self.ven_dialogo.dialog("Error", "Error al enviar datos.", 1, 2)
                            self.ven_dialogo.show()
            else:
                self.ven_dialogo.dialog("Error", "Email invalido.", 1, 2)
                self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El nuevo valor debe tener un largo minimo de 3.", 1, 2)
            self.ven_dialogo.show()

class VenCrearPregunta(QtWidgets.QTabWidget, Ui_CrearPregunta):
    def __init__(self, encuesta: Encuesta, funcion_recargar, parent=None) -> None:
        super(VenCrearPregunta, self).__init__(parent)
        self.setupUi(self, None)
        
        self.ven_dialogo = VenDialogo()
        self.funcion_recargar = funcion_recargar
        
        self.encuesta = encuesta
        self.pregunta_texto = Abierta('Pregunta')
        self.pregunta_vf = Cerrada('Pregunta')
        self.pregunta_om = Cerrada('Pregunta')
        
        ## Botones
        self.btn_cambiar_texto.clicked.connect(self.cambiar_texto)
        self.btn_limpiar_texto.clicked.connect(self.limpiar_texto)
        self.btn_agregar_texto.clicked.connect(self.crear_texto)
        
        self.btn_cambiar_vf.clicked.connect(self.cambiar_vf)
        self.btn_limpiar_vf.clicked.connect(self.limpiar_vf)
        self.btn_agregar_vf.clicked.connect(self.crear_vf)
        
        self.btn_cambiar_om.clicked.connect(self.cambiar_om)
        self.btn_limpiar_om.clicked.connect(self.limpiar_om)
        self.btn_agregarop_om.clicked.connect(self.agregar_opcion)
        self.ckb_varias.clicked.connect(self.seleccionar_varias)
        self.btn_agregar_om.clicked.connect(self.crear_om)

    def agregar_opcion(self):
        titulo = self.txt_opcion_om.text()
        if len(titulo) >= 1:
            op = Opcion(titulo)
            self.pregunta_om.agregar_opcion(op)
            self.recargar_om()
            self.txt_opcion_om.setText('')
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del texto de la opcion es de 1.", 1, 2)
            self.ven_dialogo.show()

    def recargar_om(self):
        self.recargar_opciones(self.pregunta_om.datos_mostrar())

    def seleccionar_varias(self):
        if self.ckb_varias.isChecked():
            self.pregunta_om.seleccionar_varias = True
        else:
            self.pregunta_om.seleccionar_varias = False
        self.recargar_om()

    def crear_texto(self):
        self.ven_dialogo.dialog("Crear", "Desea crear la pregunta de Texto?", 0, 3)
        self.ven_dialogo.exec()
        
        if self.ven_dialogo.result() == 1:
            self.encuesta.agregar_pregunta(self.pregunta_texto)
            self.funcion_recargar()
            self.close()

    def crear_vf(self):
        self.ven_dialogo.dialog("Crear", "Desea crear la pregunta de Verdadero y Falso?", 0, 3)
        self.ven_dialogo.exec()
        
        if self.ven_dialogo.result() == 1:
            opcion_v = Opcion('Verdadero')
            opcion_f = Opcion('Falso')
            self.pregunta_vf.agregar_opcion(opcion_v)
            self.pregunta_vf.agregar_opcion(opcion_f)
            self.encuesta.agregar_pregunta(self.pregunta_vf)
            self.funcion_recargar()
            self.close()

    def crear_om(self):
        if len(self.pregunta_om.opciones) > 0:
            self.ven_dialogo.dialog("Crear", "Desea crear la pregunta de Opcion Multiple?", 0, 3)
            self.ven_dialogo.exec()
            
            if self.ven_dialogo.result() == 1:
                self.encuesta.agregar_pregunta(self.pregunta_om)
                self.funcion_recargar()
                self.close()
        else:
            self.ven_dialogo.dialog("Error", "No puede agregar una pregunta sin opciones.", 1, 2)
            self.ven_dialogo.show()

    def cambiar_texto(self):
        titulo = self.txt_pregunta_texto.text()
        if len(titulo) >= 1:
            self.pregunta_texto.enunciado = titulo
            self.label_pregunta_texto_box.setText(titulo)
            self.txt_pregunta_texto.setText('')
            self.ven_dialogo.dialog("Correcto", "Enunciado cambiado correctamente.", 1, 1)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del Enunciado es de 1.", 1, 2)
            self.ven_dialogo.show()

    def cambiar_vf(self):
        titulo = self.txt_pregunta_vf.text()
        if len(titulo) >= 1:
            self.pregunta_vf.enunciado = titulo
            self.label_pregunta_vf_box.setText(titulo)
            self.txt_pregunta_vf.setText('')
            self.ven_dialogo.dialog("Correcto", "Enunciado cambiado correctamente.", 1, 1)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del Enunciado es de 1.", 1, 2)
            self.ven_dialogo.show()

    def cambiar_om(self):
        titulo = self.txt_pregunta_om.text()
        if len(titulo) >= 1:
            self.pregunta_om.enunciado = titulo
            self.label_pregunta_om_box.setText(titulo)
            self.txt_pregunta_om.setText('')
            self.ven_dialogo.dialog("Correcto", "Enunciado cambiado correctamente.", 1, 1)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Error", "El largo minimo del Enunciado es de 1.", 1, 2)
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
        self.ckb_varias.setChecked(False)
        self.pregunta_om = Cerrada('Pregunta')
        self.recargar_om()

class VenCrearEncuesta(QtWidgets.QWidget, Ui_CrearEncuesta):
    def __init__(self, usuario: Usuario, funcion_publicar, parent=None) -> None:
        super(VenCrearEncuesta, self).__init__(parent)
        self.setupUi(self, None)
        
        self.funcion_publicar = funcion_publicar
        self.usuario = usuario
        self.encuesta = Encuesta(self.label_titulo_encuesta.text())
        
        self.ven_dialogo = VenDialogo()
        self.ven_crear_pregunta = None
        
        ## Botones
        
        self.btn_cambiar.clicked.connect(self.titulo)
        self.btn_crear.clicked.connect(self.crear_pregunta)
        self.btn_publicar.clicked.connect(self.publicar)
        self.btn_eliminar.clicked.connect(self.eliminar)

    def crear_pregunta(self):
        self.ven_crear_pregunta = VenCrearPregunta(self.encuesta, self.recargar)
        self.ven_crear_pregunta.show()

    def eliminar(self):
        pos = self.txt_numero.text()
        self.ven_dialogo.dialog("Eliminar", "Desea eliminar la pregunta "+pos+"?", 0, 4)
        self.ven_dialogo.exec()
        
        if self.ven_dialogo.result() == 1:
            res = self.encuesta.eliminar_pregunta(pos)
            if res:
                self.ven_dialogo.dialog("Correcto", "Pregunta eliminada correctamente.", 1, 1)
                self.ven_dialogo.show()
                self.recargar_preguntas(self.encuesta.datos_mostrar())
            else:
                self.ven_dialogo.dialog("Error", "Posicion de la pregunta erronea.", 1, 2)
                self.ven_dialogo.show()
        self.txt_numero.setText('')

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
        self.recargar_preguntas(self.encuesta.datos_mostrar())

    def publicar(self):
        res = self.encuesta.publicar(self.usuario.cedula)
        if res == 2:
            self.ven_dialogo.dialog("Error", "El titulo de la encuesta ya esta registrado por el\nmismo Usuario.", 1, 2)
            self.ven_dialogo.show()
        elif res != 0:
            self.ven_dialogo.dialog("Error", "Error al ingresar la encuesta a la base de datos.", 1, 2)
            self.ven_dialogo.show()
        else:
            self.ven_dialogo.dialog("Publicar", "Desea publicar esta encuesta?\nYa no se podra modificar en un futuro.", 0, 3)
            self.ven_dialogo.exec()
            
            if self.ven_dialogo.result() == 1:
                self.funcion_publicar()
                self.close()

class VenTodasEncuestas(QtWidgets.QWidget, Ui_TodasEncuestas):
    def __init__(self, cedula:str, parent = None) -> None:
        super(VenTodasEncuestas, self).__init__(parent)
        self.setupUi(self, [], {})
        self.ven_dialogo = VenDialogo()
        self.cedula = cedula
        
        self.usuarios = ListaUsuarios()
        self.usuarios.cargar()
        
        self.encuestas = ListaEncuestas()
        self.listar_usuarios()
        
        self.buscar()
        
        ## Botones
        self.btn_buscar.clicked.connect(self.buscar)

    def listar_usuarios(self):
        usu: Usuario
        self.combo_box_usuarios.addItem('Todos')
        
        for usu in self.usuarios.lista:
            self.combo_box_usuarios.addItem(usu.nombre)
        
        self.combo_box_usuarios.setCurrentIndex(0)

    def buscar(self):
        index = self.combo_box_usuarios.currentIndex()
        if index != 0 and index != -1:
            cedula = self.usuarios.lista[index-1].cedula
        else:
            cedula = ''
        
        titulo = self.txt_nombre.text()
        
        if self.ckb_activar.isChecked():
            fecha_py = self.date_edit.date().toPyDate()
            fecha = str(fecha_py)
        else:
            fecha = ''
        
        self.encuestas.cargar(cedula, titulo, fecha)
        
        self.recargar_encuesta(self.encuestas.datos_mostrar(), self.usuarios.diccionario())
        self.botones()

    def botones(self):
        for grupo in self.lista_box:
            grupo[1].clicked.connect(self.reaccion)

    def reaccion(self):
        
        for grupo in self.lista_box:
            if grupo[1].isChecked():
                grupo[1].setChecked(False)
                
                res = Encuesta.usuarioResEncuesta(Encuesta, self.cedula, grupo[0])
                if res == 0:
                    self.ven_responder_encuesta = VenResponderEncuesta(grupo[0], self.cedula, self.mensaje, self.correcto)
                    self.ven_responder_encuesta.show()
                    return True
                elif res == 1:
                    self.ven_dialogo.dialog("Aviso", "El usuario ya respondio esta encuesta", 1, 2)
                    self.ven_dialogo.show()
                    return False
                else:
                    self.ven_dialogo.dialog("Error", "Error en la base de datos.", 1, 4)
                    self.ven_dialogo.show()
                    return False
                
        return False

    def mensaje(self):
        self.ven_responder_encuesta.close()
        self.ven_dialogo.dialog("Error", "Error al cargar la encuesta.", 1, 4)
        self.ven_dialogo.show()

    def correcto(self):
        self.ven_responder_encuesta.close()
        self.ven_dialogo.dialog("Correcto", "Datos ingresado correctamente.", 1, 1)
        self.ven_dialogo.show()

class VenMisEncuestas(QtWidgets.QWidget, Ui_MisEncuestas):
    def __init__(self, usuario: Usuario, parent = None) -> None:
        super(VenMisEncuestas, self).__init__(parent)
        self.setupUi(self, [])
        
        self.usuario = usuario
        self.encuestas = ListaEncuestas()
        self.ven_dialogo = VenDialogo()
        
        self.buscar()
        
        self.btn_buscar.clicked.connect(self.buscar)

    def buscar(self):
        titulo = self.txt_nombre.text()
        
        if self.ckb_activar.isChecked():
            fecha_py = self.dateEdit.date().toPyDate()
            fecha = str(fecha_py)
        else:
            fecha = ''
        
        self.encuestas.cargar(self.usuario.cedula, titulo, fecha)
        
        self.recargar_encuesta(self.encuestas.datos_mostrar())
        self.botones()

    def botones(self):
        for grupo in self.lista_box:
            grupo[1].clicked.connect(self.reaccion)

    def reaccion(self):
        
        for grupo in self.lista_box:
            if grupo[1].isChecked():
                grupo[1].setChecked(False)
                
                respuestas = ListaRespuestas()
                val = respuestas.recuperar(grupo[0])
                if val == 0:
                    self.ven_respuestas = VenRespuestas(respuestas)
                    self.ven_respuestas.show()
                else:
                    self.ven_dialogo.dialog("Error", "Error al cargar respuestas.", 1, 4)
                    self.ven_dialogo.show()
                
                return True
        return False

class VenResponderEncuesta(QtWidgets.QWidget, Ui_ResponderEncuesta):
    def __init__(self, id_encuesta: str, cedula: str, funcion_mensaje, funcion_correcto, parent = None) -> None:
        super(VenResponderEncuesta, self).__init__(parent)
        self.encuesta = Encuesta.recuperar(Encuesta, id_encuesta)
        self.cedula = cedula
        self.ven_dialogo = VenDialogo()
        
        if type(self.encuesta) is Encuesta:
            self.setupUi(self, self.encuesta.datos_mostrar())
            self.btn_publicar.clicked.connect(self.responder)
            self.funcion_correcto = funcion_correcto
        else:
            funcion_mensaje()

    def responder(self):
        lista = ListaRespuestas()
        
        for grupo in self.lista_abiertas:
            if len(grupo[2].toPlainText()) > 0:
                respuesta = RespondeAbierta(self.cedula, grupo[0], grupo[1], grupo[2].toPlainText())
                lista.agregar_respuesta(respuesta)
            else:
                self.ven_dialogo.dialog("Error", "Rellene todos los campos de texto.", 1, 2)
                self.ven_dialogo.show()
                return
        
        
        for grupo in self.lista_opciones:
            if grupo[3].isChecked():
                respuesta = EscogeOpcion(self.cedula, grupo[0], grupo[1], grupo[2])
                lista.agregar_respuesta(respuesta)
        
        res = lista.respoder()
        
        match res:
            case 1:
                self.ven_dialogo.dialog("Error", "Error al guardar los datos.", 1, 4)
                self.ven_dialogo.show()
            case 2:
                self.ven_dialogo.dialog("Error", "El usuario ya ha respondido esta encuesta.", 1, 4)
                self.ven_dialogo.show()
            case -1:
                self.ven_dialogo.dialog("Error", "Rellene minimo una pregunta.", 1, 2)
                self.ven_dialogo.show()
            case 0:
                self.funcion_correcto()

class VenRespuestas(QtWidgets.QWidget, Ui_Respuestas):
    def __init__(self, respuestas: ListaRespuestas, parent=None):
        super(VenRespuestas, self).__init__(parent)
        self.setupUi(self, respuestas.usuarios)
        self.respuestas = respuestas
        
        self.botones()

    def botones(self):
        for grupo in self.lista_box_usuarios:
            grupo[1].clicked.connect(self.reaccion)

    def reaccion(self):
        for grupo in self.lista_box_usuarios:
            if grupo[1].isChecked():
                grupo[1].setChecked(False)
                
                respuestas = self.respuestas.datos_mostrar(grupo[0])
                self.recargar_respuestas(respuestas)
                
                return True
        return False

def abrir():
        app = QtWidgets.QApplication(sys.argv)
        myApp = VenInicioSesion()
        myApp.show()
        app.exec()