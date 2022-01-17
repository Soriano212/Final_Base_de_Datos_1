## Trabajo Final Bases de Datos
# Alberto Soriano
# Juan Malo

import capas.interfaz.ctrl as ctrl
from capas.negocios.encuesta import Abierta, Pregunta

import capas.negocios.usuario as us

from datetime import date, datetime
import logging
import os

try:
    os.mkdir('Logs')
    print('archivo: Directorio Logs Creado')
except OSError:
    print('archivo: Directorio Logs ya existe')

class logtime(datetime):
    def today():
        fecha = datetime.today()
        return '{d.year}-{d.month}-{d.day}_{d.hour}-{d.minute}-{d.second}'.format(d=fecha)

#logging.basicConfig(filename='Logs/reporte_'+logtime.today()+'.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='Logs/reporte_pruebas.log', encoding='utf-8', level=logging.DEBUG)
logging.info('Log creado el: {}'.format(logtime.today()))

if __name__ == "__main__":
    ctrl.abrir()