import pymysql

from CLASES import alojamiento as aloj
from CLASES import  matriz as mz
from DB import conexion as c


class Area:

    def __init__(self, nombre, identificador,posicion, pasillos, segmentos,columnas,niveles,entrada,salida):
        self.nombre = nombre
        self.identificador = identificador
        self.posicion=posicion
        self.pasillos = pasillos
        self.segmentos = segmentos
        self.columnas=columnas
        self.niveles=niveles
        self.entrada=entrada
        self.salida=salida
        self.disponibilidad = 100
        print("se creo area correctamente")
        self.alta_area()

    def alta_area(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO area(nombre,identificador,posicion,pasillos,segmentos,columnas,niveles,disponibilidad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
            values = (self.nombre, self.identificador,self.posicion, self.pasillos, self.segmentos, self.columnas,self.niveles,self.disponibilidad)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_area(nombre, iden , posicion, pasillos, segmentos,columnas,niveles, entrada, salida):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idarea FROM area WHERE nombre=%s"
        values = posicion
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        if b == "None":
            print("no se encontro el area indicado")
            return 0
        else:
            ida = str(b[0][0])
            try:
                #query = "UPDATE matrizarea SET area=%s WHERE codigo=%s"
                #values = (nombre, posicion)
                #cursor.execute(query, values)
                #a.commit()
                query = "UPDATE area SET nombre=%s WHERE idarea=%s"
                values = (nombre, ida)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE area SET identificador=%s WHERE idarea=%s"
                values = (iden, ida)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE area SET posicion=%s WHERE idarea=%s"
                values = (posicion, ida)
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
                query = "UPDATE area SET columnas=%s WHERE idarea=%s"
                values = (columnas, ida)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE area SET niveles=%s WHERE idarea=%s"
                values = (niveles, ida)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE area SET entrada=%s WHERE idarea=%s"
                values = (entrada, ida)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE area SET salida=%s WHERE idarea=%s"
                values = (salida, ida)
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
    def listar_area():
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT nombre,identificador,posicion FROM area"
            cursor.execute(query)
            area = cursor.fetchall()
            a.commit()
            if area == "None":
                print("no se encontro el area indicado")
                return 0
            else:
                return area
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


    def mostrar_identificador(nombre):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT nombre FROM area WHERE identificador=%s"
        cursor.execute(query, nombre)
        data = cursor.fetchall()
        a.commit()
        if area == "None":
            print("no se encontro el area indicado")
            return 0
        else:
            return data

    def mostrar_area(nombre):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT nombre,identificador,posicion,pasillos,segmentos FROM area WHERE nombre=%s"
        cursor.execute(query, nombre)
        data = cursor.fetchall()
        a.commit()
        #if area == "None":
        #    print("no se encontro el area indicado")
        #    return 0
        #else:
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

def contar_segmentos(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT segmentos FROM area WHERE=%s"
    cursor.execute(query,area)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def contar_columnas(are):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT columnas FROM area WHERE=%s"
    cursor.execute(query, area)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def contar_niveles(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT niveles FROM area WHERE=%s"
    cursor.execute(query, area)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n


def confirmar_area_disponible(posicion):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT nombre FROM area where posicion=%s"
    cursor.execute(query,posicion)
    a.commit()
    b = cursor.fetchall()
    b=str(b[0][0])
    print (b,posicion)
    if posicion!=b:
        return 0
    else:
        return 1
    c.close_connection(a)


def ver_posicion(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT posicion FROM area where nombre=%s"
    cursor.execute(query,area)
    a.commit()
    b = cursor.fetchall()
    nombre=str(b[0][0])
    c.close_connection()
    return nombre

def ver_e():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT nombre FROM area where entrada=1"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    if b == "None":
        return 0
    else:
        return b
    c.close_connection(a)

def ver_s():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT nombre FROM area where entrada=1"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    if b == "None":
        return 0
    else:
        return b
    c.close_connection(a)

def ver_segmentos(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT segmento FROM area where nombre=%s"
    cursor.execute(query,area)
    a.commit()
    b = cursor.fetchall()
    nombre=str(b[0][0])
    c.close_connection(a)
    return nombre

def ver_pasillos(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT pasillo FROM area where nombre=%s"
    cursor.execute(query,area)
    a.commit()
    b = cursor.fetchall()
    nombre=str(b[0][0])
    c.close_connection(a)
    return nombre

def ver_area_siguiente(area):
    data=mz.importar_datos_matriz()
    nfilas=data[0][0]
    ifilas=0
    ncolumnas=data[0][1]
    icol=0
    data=ver_posicion(area)

    if fila!=nfilas:
        while ifilas>nfilas:
            if(icol==ncolumnas):
                icol=ncolumnas*2
                while icol>ncolumnas:
                    icol=icol-1
                    pos = str(str(ifilas) + "x" + str(icol))
                    return ver_area_posicion(pos)
            else:
                while icol<ncolumnas:
                    icol=icol+1
                    pos = str(str(ifilas) + "x" + str(icol))
                    return ver_area_posicion(pos)
            ifilas=ifilas+1

