import pymysql
import logging

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='admin',
                database='soriano_malo_final'
            )
        
        self.cursor = self.connection.cursor()


    def ingresar(self, tabla: str, **kwargs) -> int:
        sql = 'INSERT INTO {}('.format(tabla)
        
        for dato in kwargs.items():
            sql += '{},'.format(dato[0])
        
        sql = sql[:-1] + ') VALUES ('
        for dato in kwargs.items():
            sql += r"'{}',".format(dato[1])
        
        sql = sql[:-1] + ')'
        
        logging.info('Realizando INSERT: '+sql)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        
        except pymysql.err.OperationalError as e:
            logging.warning("Error De Operacion: " + str(e))
            return 1
        
        except pymysql.err.IntegrityError as e:
            logging.info("Error de Integridad: " + str(e))
            return 2
        
        return 0


