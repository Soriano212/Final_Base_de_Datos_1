from datetime import datetime
import logging
import re
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

    def publicar(self, id_encuesta: int) -> int:
        res = db.insert('abierta', id_encuesta = id_encuesta, pos_pregunta = self.pos_pregunta, enunciado = self.enunciado)
        
        match res:
            case 1:
                logging.warning('Error al registrar pregunta abierta.')
                return 1
            case 2:
                logging.warning('Error la clave primaria de la pregunta abierta ya esta registrada.')
                return 2
            case 0:
                logging.info('Pregunta abierta Registrada.')
                return 0

class Opcion():
    def __init__(self, enunciado: str, pos_opcion: int = 0) -> None:
        self.pos_opcion = pos_opcion
        self.enunciado = enunciado

    def datos_mostrar(self) -> tuple[int, str]:
        return (self.pos_opcion, str(self.enunciado))

    def publicar(self, pos_pregunta: int, id_encuesta: int) -> int:
        res = db.insert('opcion', pos_pregunta = pos_pregunta, pos_opcion = self.pos_opcion, enunciado = self.enunciado,
                        id_encuesta = id_encuesta)
        
        match res:
            case 1:
                logging.warning('Error al registrar opcion.')
                return 1
            case 2:
                logging.warning('Error la clave primaria de la opcion ya esta registrada.')
                return 2
            case 0:
                logging.info('Opcion Registrada.')
                return 0

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

    def publicar(self, id_encuesta: int) -> int:
        res = db.insert('cerrada', id_encuesta = id_encuesta, pos_pregunta = self.pos_pregunta, enunciado = self.enunciado,
                        seleccionar_varias = int(self.seleccionar_varias))
        
        match res:
            case 1:
                logging.warning('Error al registrar pregunta cerrada.')
                return 1
            case 2:
                logging.warning('Error la clave primaria de la pregunta cerrada ya esta registrada.')
                return 2
            case 0:
                logging.info('Pregunta cerrada Registrada.')
                
                op: Opcion
                for op in self.opciones:
                    if op.publicar(self.pos_pregunta, id_encuesta) != 0:
                        return 3
                
                return 0

class Encuesta():
    def __init__(self, titulo: str, fecha_creacion: datetime = None, id_encuesta: int = 0, cedula: str = '') -> None:
        self.id_encuesta = id_encuesta
        self.fecha_creacion = fecha_creacion
        self.titulo = titulo
        self.cedula = cedula
        self.preguntas = []

    def agregar_pregunta(self, pregunta: Pregunta):
        if len(self.preguntas) == 0:
            pregunta.pos_pregunta = 1
        else:
            pregunta.pos_pregunta = self.preguntas[-1].pos_pregunta + 1
        
        self.preguntas.append(pregunta)

    def datos_mostrar(self) -> tuple[int, str, str, list[ tuple[int, str] | tuple[int, str, bool, list[tuple[int, str]]] ]]:
        datos = []
        pre: Pregunta
        for pre in self.preguntas:
            datos.append(pre.datos_mostrar())
        return (self.id_encuesta, self.titulo, self.fecha_creacion, datos)

    def __str__(self):
        return 'Encuesta(Id: {e.id_encuesta}, Titulo: {e.titulo}, Fecha_Creacion: {e.fecha_creacion}, Numero_Preguntas: {l})'.format(e=self, l=len(self.preguntas))

    def publicar(self, cedula: str) -> int:
        res = db.insert('encuesta', titulo = self.titulo, cedula = cedula)
        
        match res:
            case 1:
                logging.warning('Error al registrar la encuesta.')
                db.rollback()
                return 1
            case 2:
                logging.info('Error la clave primaria de la encuesta ya esta registrada o titulo por usuario ya registrado.')
                db.rollback()
                return 2
            case 0:
                logging.info('Encuesta Registrada.')
                
                id_encuesta = db.llave_ultimo_insert()
                
                if type(id_encuesta) is tuple and len(id_encuesta) == 1:
                    id_encuesta = int(id_encuesta[0])
                    logging.info('Aviso: id_encuesta obtenido: {}'.format(id_encuesta))
                else:
                    logging.warning('Error al obtener id de encuesta')
                    db.rollback()
                    return 3
                
                pre: Abierta | Cerrada
                for pre in self.preguntas:
                    res_pre = pre.publicar(id_encuesta)
                    match res_pre:
                        case 1:
                            db.rollback()
                            return -1
                        case 2:
                            db.rollback()
                            return -2
                        case 3:
                            db.rollback()
                            return -3
                
                db.commit()
                return 0

class ListaEncuestas():
    def __init__(self):
        self.lista = []

    def datos_mostrar(self) -> list[tuple[str, str, str, str]]:
        datos = []
        dato: Encuesta
        for dato in self.lista:
            tupla = (dato.id_encuesta, dato.titulo, str(dato.fecha_creacion), dato.cedula)
            datos.append(tupla)
        return datos

    def cargar(self, cedula: str = '', titulo: str = '', fecha: str = ''):
        
        self.lista.clear()
        cedula = '%'+cedula+'%'
        titulo = '%'+titulo+'%'
        fecha = '%'+fecha+'%'
        
        datos = db.select('encuesta', cedula = cedula, titulo = titulo, fecha = fecha)
        
        if type(datos) is tuple:
            
            for dato in datos:
                encuesta = Encuesta(dato[1], dato[2], dato[0], dato[3])
                self.lista.append(encuesta)
            return 0
        else:
            #Error al cargar encuestas
            return 1
