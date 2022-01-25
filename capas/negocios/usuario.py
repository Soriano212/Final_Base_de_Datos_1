import hashlib
import logging
from capas.datos.database import DataBase

db = DataBase()

class Usuario():
    def __init__(self, cedula: str, nombre: str, email: str, contrasenia: str) -> None:
        self.cedula = cedula
        self.nombre = nombre
        self.email = email
        self.contrasenia = self.sha1(contrasenia)

    def __str__(self):
        return 'Usuario(Cedula: {u.cedula}, Nombre: {u.nombre}, Email: {u.email}, Contraseña: {u.contrasenia})'.format(u = self)

    def registrarUsuario(self) -> int:
        res = db.insert('usuario', cedula = self.cedula, nombre = self.nombre, email = self.email, contrasenia = self.contrasenia)
        
        match res:
            case 1:
                logging.info('Error al registrar usuario.')
                db.rollback()
                return 1
            case 2:
                logging.info('El email ya se encuentra registrado.')
                db.rollback()
                return 2
            case 0:
                logging.info('Usuario registrado.')
                db.commit()
                return 0

    def sha1(cls, contrasenia: str):
        encode = contrasenia.encode()
        hash_contra = hashlib.sha1(encode)
        pbHash = hash_contra.hexdigest()
        return pbHash

    def inicioSesion(cls, email: str, contrasenia: str) -> object | int:
        datos = db.select('usuario', email = email, contrasenia = cls.sha1(cls, contrasenia))
        
        if type(datos) is tuple:
            if len(datos) == 1:
                usuario = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3])
                return usuario
            else:
                #No existe el usuario
                return 1
        else:
            #Error al buscar usuario
            return 2

    def pruedeCrearEncuesta(self) -> int:
        datos = db.puede_crear_encuesta(self.cedula)
        
        if type(datos) is tuple:
            if len(datos) == 1:
                return datos[0]
            else:
                #Se obtuvieron otros datos
                return -1
        else:
            #Error al ejecutar
            return -2

    def cambioUsuario(cls, tipo: int):
        if tipo == 1:
            db.usuario_inicio()
        elif tipo == 2:
            db.usuario_encuestado()
        elif tipo == 3:
            db.usuario_creador()

class ListaUsuarios():
    def __init__(self) -> None:
        self.lista = []

    def cargar(self):
        self.lista.clear()
        datos = db.select('usuario', 'cedula', 'nombre')
        
        if type(datos) is tuple:
            for dato in datos:
                usuario = Usuario(dato[0], dato[1], '', '')
                self.lista.append(usuario)
            return 0
        else:
            return 1

    def diccionario(self) -> dict[str, str]:
        datos = []
        usu: Usuario
        for usu in self.lista:
            datos.append((usu.cedula, usu.nombre))
        return dict(datos)

    def buscar_cedula(self, cedula: str) -> Usuario | None:
        usu: Usuario
        for usu in self.lista:
            if usu.cedula == cedula:
                return usu
        
        return None