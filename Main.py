## Trabajo Final Bases de Datos
# Alberto Soriano
# Juan Malo

import capas.interfaz.manejador as manejador
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

logging.basicConfig(filename='Logs/reporte_'+str(date.today())+'.log', encoding='utf-8', level=logging.DEBUG)

logging.info('\n\n----------------------------------------------\nLog creado el: {}\n'.format(logtime.today()))

if __name__ == "__main__":
    manejador.abrir()