import pymysql

from CLASES import alojamiento as aloj
from DB import conexion as c


class Area:

    def __init__(self, nombre, identificador, pasillos, segmentos, longitud, ancho, alto):
        self.nombre = nombre
        self.identificador = identificador
        self.pasillos = pasillos
        self.segmentos = segmentos
        self.longitud = longitud
        self.ancho = ancho
        self.alto = alto
        self.disponibilidad = 0
        print("se creo area correctamente")
        self.alta_area()

    def alta_area(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO area(nombre,identificador,pasillos,segmentos,longitud,ancho,alto,disponibilidad) " \
                    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            values = (
            self.nombre, self.identificador, self.pasillos, self.segmentos, self.disponibilidad, self.longitud,
            self.ancho, self.alto)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_area(nombre, iden, pasillos, segmentos, longitud, ancho, alto):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idarea FROM area WHERE nombre=%s"
        values = nombre
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        ida = str(b[0][0])
        try:
            query = "UPDATE area SET nombre=%s WHERE idarea=%s"
            values = (nombre, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET identificador=%s WHERE idarea=%s"
            values = (iden, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET pasillos=%s WHERE idarea=%s"
            values = (pasillos, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET segmentos=%s WHERE idarea=%s"
            values = (segmentos, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET longitud=%s WHERE idarea=%s"
            values = (longitud, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET ancho=%s WHERE idarea=%s"
            values = (ancho, ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET alto=%s WHERE idarea=%s"
            values = (alto, ida)
            cursor.execute(query, values)
            a.commit()
            print("se modifico area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def eliminar_area(nombre):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "DELETE FROM area WHERE nombre=%s"
            values = nombre
            cursor.execute(query, values)
            a.commit()
            aloj.Alojamiento.elim_pos_area(nombre)
            print("se elimino area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    @staticmethod
    def contar_filas():
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM area"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

    @staticmethod
    def listar_area():
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT nombre,identificador,pasillos,segmentos,disponibilidad FROM area"
            cursor.execute(query)
            area = cursor.fetchall()
            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return area

    def mostrar_identificador(nombre):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT nombre FROM area WHERE identificador=%s"
        cursor.execute(query, nombre)
        data = cursor.fetchall()
        a.commit()
        return data

    def mostrar_area(nombre):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT nombre,identificador,pasillos,segmentos,longitud,ancho,alto FROM area WHERE nombre=%s"
        cursor.execute(query, nombre)
        data = cursor.fetchall()
        a.commit()
        return data


def ver_nombre(nombre):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM area"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    i = 0
    nombre = "(('" + nombre + "',),)"
    while i < n:
        query = "SELECT nombre FROM area WHERE idarea = %s"
        values = i
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        b = str(b)
        print(b)
        if b == nombre:
            i = n + 1
        else:
            i += 1
    if i == n + 1:
        c.close_connection(a)
        # nombre existe
        return 1
    else:
        c.close_connection(a)
        return 0


def ver_iden(iden):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM area"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    i = 0
    iden = "(('" + iden + "',),)"
    while i < n:
        query = "SELECT iden FROM area WHERE idarea = %s"
        values = i
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        b = str(b)
        print(b)
        if b == iden:
            i = n + 1
        else:
            i += 1
    if i == n + 1:
        c.close_connection(a)
        # identificador existe
        return 1
    else:
        c.close_connection(a)
        return 0
