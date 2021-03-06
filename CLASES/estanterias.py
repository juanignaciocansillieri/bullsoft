import pymysql

from CLASES import lotes, alojamiento, area
from DB import conexion as c


class Estanterias:
    def __init__(self, codigo,area,pasillo,posicion,columnas,niveles):
        self.codigo=codigo
        self.area=area
        self.pasillo=pasillo
        self.segmento = posicion
        self.columnas=columnas
        self.niveles=niveles
        self.alta_estanteria()
        self.crear_alojamientos()

    def alta_estanteria(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO estanterias (codigo, area, pasillo,posicion,columnas,niveles) VALUES (%s,%s,%s,%s,%s,%s) "
            values = (self.codigo, self.area,self.pasillo,self.segmento,self.columnas,self.niveles)
            cursor.execute(query, values)
            a.commit()

        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def borrar_estanteria(area):
        a = c.start_connection()
        cursor = a.cursor()
        query = "DELETE from estanterias WHERE area =%s"
        cursor.execute(query, area)
        a.commit()
        print("Se elimino estanterias correctamente")

    def modificar_estanteria(codigov, codigon, area, pasillo,segmento,columnas,niveles):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idestanterias FROM estanterias WHERE codigo=%s"
        values = codigov
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        if b == "()":
            print("no se encontro la estanteria indicado")
            return 0
        else:
            idp = str(b[0][0])

            try:
                query = "UPDATE estanterias set codigo=%s WHERE idestanterias=%s"
                values = (codigon, idp)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE estanterias set area=%s WHERE idestanterias=%s"
                values = (area, idp)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE estanterias set pasillo=%s WHERE idestanterias=%s"
                values = (pasillo, idp)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE estanterias set segmento=%s WHERE idestanterias=%s"
                values = (segmento, idp)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE estanterias set columnas=%s WHERE idestanterias=%s"
                values = (columnas, idp)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE estanterias set niveles=%s WHERE idestanterias=%s"
                values = (niveles, idp)
                cursor.execute(query, values)
                a.commit()
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)

    def crear_alojamientos(self):
        iniveles=0
        icolumnas=0
        while int(icolumnas)<int(self.columnas):
            while int(iniveles)<int(self.niveles):
                alojamiento.Alojamiento(0,0,0,self.area,self.pasillo,self.segmento,iniveles+1,0,icolumnas+1)
                iniveles=iniveles+1
            iniveles=0
            icolumnas=icolumnas+1

def verificar_segmentos(area,posicion):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT * FROM estanterias where area=%s and posicion=%s"
    cursor.execute(query,(area,posicion))
    a.commit()
    b = cursor.fetchall()
    #print(area,posicion,b)
    if str(b) == "()":
        c.close_connection(a)
        return 1
    else:
        c.close_connection(a)
        return 0




def contar_estanterias_area(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT count(*) FROM estanterias where area=%s"
    cursor.execute(query, area)
    a.commit()
    b = cursor.fetchall()
    b = b[0][0]
    n = int(b)
    c.close_connection(a)
    return n

def mostrar_columnas(area,posicion):
    posicion = int(posicion)
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT columnas FROM estanterias where area=%s and posicion=%s"
    cursor.execute(query, (area, posicion))
    a.commit()
    b = cursor.fetchall()
    while str(b) == "()":
        posicion += 1
        query = "SELECT columnas FROM estanterias where area=%s and posicion=%s"
        cursor.execute(query, (area, posicion))
        a.commit()
        b = cursor.fetchall()

    b = b[0][0]
    c.close_connection(a)
    return [b, posicion]

def contar_niveles(area,posicion):
    print(posicion)
    posicion = int(posicion)
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT niveles FROM estanterias where area=%s and posicion=%s"
    cursor.execute(query, (area, posicion))
    a.commit()
    b = cursor.fetchall()
    while str(b) == "()":
        posicion += 1
        query = "SELECT niveles FROM estanterias where area=%s and posicion=%s"
        cursor.execute(query, (area, posicion))
        a.commit()
        b = cursor.fetchall()
    b = b[0][0]
    c.close_connection(a)
    return b

def ver_posicion(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT posicion FROM estanterias where area=%s ORDER by posicion"
    cursor.execute(query,area)
    a.commit()
    data = cursor.fetchall()
    c.close_connection(a)
    return data


