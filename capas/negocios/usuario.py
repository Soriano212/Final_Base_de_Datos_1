import hashlib
from varname import nameof

from capas.datos.database import DataBase

db = DataBase()

class Usuario():
    def __init__(self, nombre: str, usuario: str, email: str, contrasenia: str) -> None:
        self.nombre = nombre
        self.usuario = usuario
        self.email = email
        encode = contrasenia.encode()
        hash_contra = hashlib.sha1(encode)
        pbHash = hash_contra.hexdigest()
        self.contrasenia = pbHash

    def __str__():
        return Usuario

    def registrarUsuario(self) -> int:
        res = db.ingresar('usuario', nombre = self.nombre, usuario = self.usuario,
                        email = self.email, contrasenia = self.contrasenia)
        return res

    def inicioSecion(cls, email: str, contrasenia: str):
        pass


