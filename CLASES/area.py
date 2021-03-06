import pymysql

from CLASES import alojamiento as aloj
from CLASES import  matriz as mz
from DB import conexion as c


class Area:

    def __init__(self, nombre, identificador,posicion, pasillos, segmentos,entrada,salida):
        self.nombre = nombre
        self.identificador = identificador
        self.posicion=posicion
        self.pasillos = pasillos
        self.segmentos = segmentos
        self.entrada=entrada
        self.salida=salida
        self.disponibilidad = 100
        print("se creo area correctamente")
        self.alta_area()

    def alta_area(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO area(nombre,identificador,posicion,pasillos,segmentos,disponibilidad) VALUES (%s,%s,%s,%s,%s,%s) "
            values = (self.nombre, self.identificador,self.posicion, self.pasillos, self.segmentos,self.disponibilidad)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_area(nombre, iden , posicion, pasillos, segmentos, entrada, salida):
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
        data = cursor.fetchone()
        a.commit()
        if data == None:
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
        if data == "()":
            print("no se encontro el area indicado")
            return 0
        else:
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
    i = 1
    nombre = "(('" + nombre + "',),)"
    while i <= n:
        query = "SELECT nombre FROM area WHERE idarea = %s"
        values = i
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        b = str(b)
        if str(b) == str(nombre):
            i = n + 2
        else:
            i += 1
    if i == n + 2:
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
        #print(b)
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

def contar_columnas(area):
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
    #print (b,posicion)
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
    print (b)
    if str(b) == "()":
        return 0
    else:
        nombre=str(b[0][0])
    c.close_connection(a)
    return nombre

def ver_area_posicion(posicion):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT nombre FROM area where posicion=%s"
    cursor.execute(query,posicion)
    a.commit()
    b = cursor.fetchall()
    nombre=str(b[0][0])
    c.close_connection(a)
    return nombre

def ver_e():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT nombre FROM area where entrada=1"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    if str(b) == "()":
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
    if str(b) == "()":
        return 0
    else:
        return b
    c.close_connection(a)

def ver_segmentos(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT segmentos FROM area where nombre=%s"
    cursor.execute(query,area)
    a.commit()
    b = cursor.fetchall()
    data=str(b[0][0])
    c.close_connection(a)
    return data

def ver_pasillos(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT pasillos FROM area where nombre=%s"
    cursor.execute(query,area)
    a.commit()
    b = cursor.fetchall()
    data=int(b[0][0])
    c.close_connection(a)
    return data


def ver_recorrido():
    a = c.start_connection()
    cursor = a.cursor()
    n=contar_filas()
    inicio=ver_e()
    if inicio==0:
        query = "SELECT posicion FROM area where idarea=%s"
        cursor.execute(query, 1)
        a.commit()
        b = cursor.fetchall()
        inicio = str(b[0][0])
    final=ver_s()
    if final==0:
        query = "SELECT posicion FROM area where idarea=%s"
        cursor.execute(query, n)
        a.commit()
        b = cursor.fetchall()
        final = str(b[0][0])

    query = "SELECT posicion FROM area where idarea=%s"
    cursor.execute(query, n)
    a.commit()
    b = cursor.fetchall()
    xy2 = str(b[0][0])
    xy2=xy2.split(sep="x")
    x2=int(xy2[0])
    y2=int(xy2[1])

    posiciones=[]
    i=0
    x,y=1,1
    while y<=y2:
        if x<x2:
            while x<=x2:
                xy=str(str(x)+"x"+str(y))
                posiciones.append(xy)
                x=x+1
        else:
            while x>=1:
                xy = str(str(x) + "x" + str(y))
                posiciones.append(xy)
                x=x-1
        if x>x2:
            x=x-1
        else:
            x=x+1
        y=y+1
    posiciones.append(inicio)
    posiciones.append(final)
    c.close_connection(a)
    return posiciones