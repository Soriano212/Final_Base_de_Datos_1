
from pdb import post_mortem
from select import select
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
    def __init__(self, cedula: str, pos_opcion: int, pos_pregunta: int, id_encuesta: int, texto: str = '') -> None:
        self.cedula = cedula
        self.pos_opcion = pos_opcion
        self.pos_pregunta = pos_pregunta
        self.id_encuesta = id_encuesta
        self.texto = texto

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
        self.usuarios = []

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

    def recuperar(self, id_encuesta: str) -> int:
        datos_res_abierta = db.select('responde_abierta', id_encuesta = id_encuesta)
        self.lista.clear()
        self.usuarios.clear()
        
        if type(datos_res_abierta) is tuple:
            for dato in datos_res_abierta:
                respuesta = RespondeAbierta(dato[0], dato[1], dato[2], dato[3])
                usu = db.select('usuario', 'nombre', cedula = dato[0])
                
                if type(usu) is tuple:
                    if len(usu) == 1:
                        self.usuarios.append((dato[0], usu[0][0]))
                    else:
                        return 1
                
                self.lista.append(respuesta)
        
        datos_esc_opcion = db.select('escoge_opcion', id_encuesta = id_encuesta)
        
        if type(datos_esc_opcion) is tuple:
            for dato in datos_esc_opcion:
                respuesta = EscogeOpcion(dato[0], dato[1], dato[2], dato[3])
                
                datos_opc = db.select('opcion', 'enunciado', pos_opcion = dato[1], pos_pregunta = dato[2], id_encuesta = dato[3])
                
                if type(datos_opc) is tuple:
                    if len(datos_opc) == 1:
                        respuesta.texto = datos_opc[0][0]
                    else:
                        return 1
                
                usu = db.select('usuario', 'nombre', cedula = dato[0])
                
                if type(usu) is tuple:
                    if len(usu) == 1:
                        self.usuarios.append((dato[0], usu[0][0]))
                    else:
                        return 1
                
                self.lista.append(respuesta)
        
        self.usuarios = list(set(self.usuarios))
        return 0

