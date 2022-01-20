import pymysql
import logging

class DataBase:
    __instance = None
    
    def __new__(cls):
        if DataBase.__instance is None:
            print('Nueva instancia')
            DataBase.__instance = object.__new__(cls)
        
        return DataBase.__instance
    
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
        
        except pymysql.err.OperationalError as e:
            logging.warning("Error De Operacion: " + str(e))
            return 1
        except pymysql.err.IntegrityError as e:
            logging.info("Error de Integridad: " + str(e))
            return 2
        
        return 0

    def select(self, tabla: str, *args ,**kwargs) -> tuple[tuple, ...] | int:
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
                    sql = sql[:-1]
                    sql += ' AND '
                cont += 1
                
                if str(dato[1])[0] == '%' or str(dato[1])[-1] == '%':
                    sql += r"{} LIKE '{}',".format(dato[0], dato[1])
                else:
                    sql += r"{}='{}',".format(dato[0], dato[1])
            sql = sql[:-1]
        
        logging.info('Realizando SELECT: '+sql)
        
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            return datos
        
        except pymysql.err.OperationalError as e:
            logging.warning("Error De Operacion: " + str(e))
            return 1
        
        except pymysql.err.IntegrityError as e:
            logging.warning("Error de Integridad: " + str(e))
            return 2

    def llave_ultimo_insert(self) -> tuple | int:
        sql = "SELECT LAST_INSERT_ID()"
        
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()
            return datos
        
        except pymysql.err.OperationalError as e:
            logging.warning("Error De Operacion: " + str(e))
            return 1

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()