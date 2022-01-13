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

    def toDB(self) -> dict:
        diccionario = {nameof(self.nombre): self.nombre,
                    nameof(self.usuario): self.usuario,
                    nameof(self.email): self.email,
                    nameof(self.contrasenia): self.contrasenia}
        return diccionario

def inicioSecion(email: str, contrasenia: str):
    pass

def registrarUsuario(usuario: Usuario):
    db.ingresar('usuario', nombre = usuario.nombre,
                usuario = usuario.usuario,
                email = usuario.email,
                contrasenia = usuario.contrasenia)

if __name__ == "__main__":
    usu = Usuario('Alberto', 'Albe212', 'morir@gmail.com', 'hola')
    registrarUsuario(usu)
