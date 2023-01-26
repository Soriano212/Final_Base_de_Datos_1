from datetime import datetime
import logging
from capas.datos.database import DataBase

db = DataBase()

class Pregunta():
    def __init__(self, pos_pregunta: int, enunciado: str) -> None:
        self.pos_pregunta = pos_pregunta
        self.enunciado = enunciado

    def datos_mostrar(self) -> tuple[int, str]:
        return(self.pos_pregunta, str(self.enunciado))

    def __gt__(self, otro):
        return self.pos_pregunta > otro.pos_pregunta

class Abierta(Pregunta):
    def __init__(self, enunciado: str, pos_pregunta: int = 0) -> None:
        super().__init__(pos_pregunta, enunciado)

    def publicar(self, id_encuesta: int) -> int:
        res = db.insert_ant('abierta', id_encuesta = id_encuesta, pos_pregunta = self.pos_pregunta, enunciado = self.enunciado)
        
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
        res = db.insert_ant('opcion', pos_pregunta = pos_pregunta, pos_opcion = self.pos_opcion, enunciado = self.enunciado,
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

    def __gt__(self, otro):
        return self.pos_opcion > otro.pos_opcion

class Cerrada(Pregunta):
    def __init__(self, enunciado: str, seleccionar_varias: bool = False, pos_pregunta: int = 0) -> None:
        super().__init__(pos_pregunta, enunciado)
        self.seleccionar_varias = seleccionar_varias
        self.opciones = []

    def agregar_opcion(self, opcion: Opcion):
        if opcion.pos_opcion == 0:
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
        res = db.insert_ant('cerrada', id_encuesta = id_encuesta, pos_pregunta = self.pos_pregunta, enunciado = self.enunciado,
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

    def ordenar_opciones(self):
        self.opciones = sorted(self.opciones)

class Encuesta():
    def __init__(self, titulo: str, fecha_creacion: datetime = None, id_encuesta: int = 0, cedula: str = '') -> None:
        self.id_encuesta = id_encuesta
        self.fecha_creacion = fecha_creacion
        self.titulo = titulo
        self.cedula = cedula
        self.preguntas = []

    def agregar_pregunta(self, pregunta: Pregunta):
        if pregunta.pos_pregunta == 0:
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

    def ordenar_preguntas(self):
        self.preguntas = sorted(self.preguntas)

    def eliminar_pregunta(self, pos_pregunta: str):
        pre: Pregunta
        cambio = False
        for pre in self.preguntas:
            if str(pre.pos_pregunta) == pos_pregunta:
                borrar = pre
                cambio = True
            if cambio:
                pre.pos_pregunta -= 1
        
        if cambio:
            self.preguntas.remove(borrar)
            
        
        self.ordenar_preguntas()
        
        return cambio

    def publicar(self, cedula: str) -> int:
        res = db.insert_ant('encuesta', titulo = self.titulo, cedula = cedula)
        
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

    def recuperar(cls, id_encuesta: str) -> object | int:
        datos_encuesta = db.select('encuesta', id_encuesta = id_encuesta)

        if type(datos_encuesta) is tuple:
            if len(datos_encuesta) == 1:
                encuesta = Encuesta(datos_encuesta[0][1], datos_encuesta[0][2], datos_encuesta[0][0], datos_encuesta[0][3])
                
                datos_abierta = db.select('abierta', id_encuesta = id_encuesta)
                
                if type(datos_abierta) is tuple:
                    for dato in datos_abierta:
                        abierta = Abierta(dato[2], dato[0])
                        encuesta.agregar_pregunta(abierta)
                else:
                    #Error al cargar pregunta Abierta
                    return 1
                
                datos_cerrada = db.select('cerrada', id_encuesta = id_encuesta)
                
                if type(datos_cerrada) is tuple:
                    for dato in datos_cerrada:
                        cerrada = Cerrada(dato[2], dato[3], dato[0])
                        pos_pregunta = cerrada.pos_pregunta
                        
                        datos_opcion = db.select('opcion', pos_pregunta = pos_pregunta, id_encuesta = id_encuesta)
                        
                        if type(datos_opcion) is tuple:
                            for op in datos_opcion:
                                opcion = Opcion(op[3], op[0])
                                cerrada.agregar_opcion(opcion)
                            cerrada.ordenar_opciones()
                        else:
                            #Error al cargar Opcion
                            return 1
                        
                        encuesta.agregar_pregunta(cerrada)
                else:
                    #Error al cargar pregunta Cerrada
                    return 1
                
                encuesta.ordenar_preguntas()
                return encuesta
                
            else:
                #No existe la encuesta
                return 1
        else:
            #Error al buscar encuesta
            return 2

    def usuarioResEncuesta(cls, cedula: str, id_encuesta: str) -> int:
        datos = db.usuario_res_encuesta(cedula, int(id_encuesta))
        
        if type(datos) is tuple:
            if len(datos) == 1:
                return datos[0]
            else:
                #Se obtuvieron otros datos
                return -1
        else:
            #Error al ejecutar
            return -2

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
