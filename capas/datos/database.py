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


    def insert(self, tabla: str, **kwargs) -> int:
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

    def select(self, tabla: str, *args ,**kwargs) -> int:
        sql = 'SELECT '
        
        if len(args) == 0:
            sql += '* FROM {}'.format(tabla)
        else:
            for dato in args:
                sql += '{},'.format(dato)
            sql = sql[:-1] + ' FROM {}'.format(tabla)
        
        if len(kwargs) != 0:
            cont = 0
            for dato in kwargs.items():
                if cont == 0:
                    sql += ' WHERE '
                else:
                    sql += ' AND '
                
                sql += r"{}='{}',".format(dato[1])
        
        
        logging.info('Realizando SELECT: '+sql)
        
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