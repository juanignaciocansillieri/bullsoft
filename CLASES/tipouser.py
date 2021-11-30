import pymysql
from DB import conexion as c


class Tipouser:

    def __init__(self, tipo, identificador):
        self.tipo = tipo
        self.identificador = identificador
        print("se creo tipouser correctamente")
        self.alta_tipouser()

    def alta_tipouser(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO tipouser(tipo,identificador) VALUES (%s,%s)"
            values = (self.tipo, self.identificador)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al tipouser correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_tipouser(identv, idenn, tipo):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idtipouser FROM tipouser WHERE identificador=%s"
        values = identv
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        ida = str(b[0][0])
        try:
            query = "UPDATE tipouser SET tipo=%s WHERE idtipouser=%s"
            values = (tipo, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE tipouser SET identificador=%s WHERE idtipouser=%s"
            values = (idenn, ida)
            cursor.execute(query, values)
            a.commit()
            print("se modifico tipouser correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def eliminar_tipouser(identificador):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "DELETE FROM tipouser WHERE identificador=%s"
            values = identificador
            cursor.execute(query, values)
            a.commit()
            print("se elimino tipouser correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    @staticmethod
    def contar_filas():
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM tipouser"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

    @staticmethod
    def listar_tipouser():
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT tipo,identificador FROM tipouser"
            cursor.execute(query)
            area = cursor.fetchall()
            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return area

    def mostrar_tipouser(iden):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT tipo,identificador FROM tipouser WHERE identificador=%s"
        cursor.execute(query, iden)
        data = cursor.fetchall()
        a.commit()
        return data
