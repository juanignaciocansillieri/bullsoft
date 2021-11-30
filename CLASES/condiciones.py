import pymysql

from DB import conexion as c


class Condicion:

    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador
        print("se creo condicion correctamente")
        self.alta_condicion()

    def alta_condicion(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO condicion(nombre,identificador) VALUES (%s,%s)"
            values = (self.nombre, self.identificador)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al condicion correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_condicion(identv, idenn, nombre):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idcondicion FROM condicion WHERE identificador=%s"
        values = identv
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        ida = str(b[0][0])
        try:
            query = "UPDATE condicion SET nombre=%s WHERE idcondicion=%s"
            values = (nombre, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE condicion SET identificador=%s WHERE idcondicion=%s"
            values = (idenn, ida)
            cursor.execute(query, values)
            a.commit()
            print("se modifico condicion correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def eliminar_condicion(identificador):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "DELETE FROM condicion WHERE identificador=%s"
            values = identificador
            cursor.execute(query, values)
            a.commit()
            print("se elimino condicion correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    @staticmethod
    def contar_filas():
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM condicion"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

    @staticmethod
    def listar_condicion():
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT nombre,identificador FROM condicion"
            cursor.execute(query)
            area = cursor.fetchall()
            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return area

    def mostrar_condicion(iden):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT nombre,identificador FROM condicion WHERE identificador=%s")
        cursor.execute(query, iden)
        data = cursor.fetchall()
        a.commit()
        return data
