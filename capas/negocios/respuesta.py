
from capas.datos.database import DataBase
import logging

db = DataBase()

class RespondeAbierta():
    def __init__(self, cedula: str, pos_pregunta: int, id_encuesta: int, respuesta: str) -> None:
        self.cedula = cedula
        self.pos_pregunta = pos_pregunta
        self.id_encuesta = id_encuesta
        self.respuesta = respuesta

    def responder(self) -> int:
        res = db.insert('responde_abierta', cedula = self.cedula, pos_pregunta = self.pos_pregunta,
                        id_encuesta = self.id_encuesta, respuesta = self.respuesta)
        
        match res:
            case 1:
                logging.warning('Error al registrar la respuesta abierta.')
                return 1
            case 2:
                logging.warning('Error la clave primaria de la respuesta abierta ya esta registrada.')
                return 2
            case 0:
                logging.info('Respuesta abierta Registrada.')
                return 0

class EscogeOpcion():
    def __init__(self, cedula: str, pos_opcion: int, pos_pregunta: int, id_encuesta: int) -> None:
        self.cedula = cedula
        self.pos_opcion = pos_opcion
        self.pos_pregunta = pos_pregunta
        self.id_encuesta = id_encuesta

    def responder(self) -> int:
        res = db.insert('escoge_opcion', cedula = self.cedula, pos_pregunta = self.pos_pregunta,
                        id_encuesta = self.id_encuesta, pos_opcion = self.pos_opcion)
        
        match res:
            case 1:
                logging.warning('Error al registrar la opcion escogida.')
                return 1
            case 2:
                logging.warning('Error la clave primaria de la opcion escogida ya esta registrada.')
                return 2
            case 0:
                logging.info('La opcion escogida Registrada.')
                return 0

class ListaRespuestas():
    def __init__(self) -> None:
        self.lista = []

    def agregar_respuesta(self, respuesta: RespondeAbierta | EscogeOpcion) -> None:
        self.lista.append(respuesta)

    def respoder(self) -> int:
        
        if len(self.lista) > 0:
            res: RespondeAbierta | EscogeOpcion
            for res in self.lista:
                retorno = res.responder()
                match retorno:
                    case 1:
                        logging.warning('Error al registrar las respuestas.')
                        db.rollback()
                        return 1
                    case 2:
                        logging.warning('Error la clave primaria de una respuesta ya esta registrada.')
                        db.rollback()
                        return 2
            
            db.commit()
            return 0
        else:
            return -1