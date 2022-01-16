from lib2to3.pgen2.token import OP
from capas.datos.database import DataBase

db = DataBase()

class Pregunta():
    def __init__(self, pos_pregunta: int, enunciado: str) -> None:
        self.pos_pregunta = pos_pregunta
        self.enunciado = enunciado
    
    def datos_mostrar(self) -> tuple[int, str]:
        return(self.pos_pregunta, str(self.enunciado))

class Abierta(Pregunta):
    def __init__(self, enunciado: str, pos_pregunta: int = 0) -> None:
        super().__init__(pos_pregunta, enunciado)

class Opcion():
    def __init__(self, enunciado: str, pos_opcion: int = 0) -> None:
        self.pos_opcion = pos_opcion
        self.enuciado = enunciado
    
    def datos_mostrar(self) -> tuple[int, str]:
        return (self.pos_opcion, str(self.enuciado))

class Cerrada(Pregunta):
    def __init__(self, enunciado: str, seleccionar_varias: bool = False, pos_pregunta: int = 0) -> None:
        super().__init__(pos_pregunta, enunciado)
        self.seleccionar_varias = seleccionar_varias
        self.opciones = []

    def agregar_opcion(self, opcion: Opcion):
        if len(self.opciones) == 0:
            opcion.pos_opcion = 1
        else:
            opcion.pos_opcion = self.opciones[-1].pos_opcion + 1
        
        self.opciones.append(opcion)

    def datos_mostrar(self) -> tuple[int, str, bool, list[tuple[int, str]]]:
        datos = []
        op: Opcion
        for op in self.opciones:
            datos.append(op.datos_mostrar())
        
        return (self.pos_pregunta, str(self.enunciado), self.seleccionar_varias, datos)

class Encuesta():
    def __init__(self, titulo: str, fecha_creacion: str = '', id_encuesta: int = 0) -> None:
        self.id_encuesta = id_encuesta
        self.fecha_creacion = fecha_creacion
        self.titulo = titulo
        self.preguntas = []

    def agregar_pregunta(self, pregunta: Pregunta):
        if len(self.preguntas) == 0:
            pregunta.pos_pregunta = 1
        else:
            pregunta.pos_pregunta = self.preguntas[-1].pos_pregunta + 1
        
        self.preguntas.append(pregunta)