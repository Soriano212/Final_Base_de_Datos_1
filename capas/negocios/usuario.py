import hashlib
from varname import nameof

from capas.datos.database import DataBase

db = DataBase()

class Usuario():
    def __init__(self, nombre: str, usuario: str, email: str, contrasenia: str, id: str = None) -> None:
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.email = email
        self.contrasenia = self.sha1(contrasenia)

    def __str__():
        return Usuario

    def registrarUsuario(self) -> int:
        res = db.insert('usuario', nombre = self.nombre, usuario = self.usuario,
                        email = self.email, contrasenia = self.contrasenia)
        match res:
            case 1:
                print('Error al registrar usuario.')
                return 1
            case 2:
                print('El email ya se encuentra registrado.')
                return 2
            case 0:
                print('Usuario registrado.')
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
                usuario = Usuario(datos[0][1], datos[0][2], datos[0][3], datos[0][4], datos[0][0])
                return usuario
            else:
                #No existe el usuario
                return 1
        else:
            #Error al buscar usuario
            return 2


