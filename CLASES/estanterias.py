import pymysql

from CLASES import lotes, alojamiento, area
from DB import conexion as c


class Estanterias:
    def __init__(self, codigo,area,pasillo,segmento,columnas,niveles):
        self.codigo=codigo
        self.area=area
        self.pasillo=pasillo
        self.segmento = segmento
        self.columnas=columnas
        self.niveles=nivels
        self.alta_estanteria()
        self.crear_alojamientos()

    def alta_estanteria(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO estanterias (codigo, area, pasillo,segmento,columnas,niveles) VALUES (%s,%s,%s,%s,%s,%s) "
            values = (self.codigo, self.area,self.pasillo,self.segmento,self.columnas,self.niveles)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta estanteria correctamente")

        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def borrar_estanteria(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = "DELETE from estanterias WHERE codigo =%s"
        cursor.execute(query, codigo)
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
        if b == "None":
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
                print("se MODIFICO estanteria correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)

    def crear_alojamientos(self):
        iniveles=0
        icolumnas=0
        while icolumnas<self.columnas:
            while iniveles<self.niveles:
                alojamiento.Alojamiento(0,0,0,self.area,self.pasillo,self.segmento,iniveles,0,icolumnas)
                iniveles=iniveles+1
            iniveles=0
            icolumnas=icolumnas+1

    def contar_niveles(area, posicion):
                a = c.start_connection()
                cursor = a.cursor()
                query = "SELECT niveles FROM estanterias where area=%s and posicion=%s"
                cursor.execute(query, (area, posicion))
                a.commit()
                b = cursor.fetchall()
                b = b[0][0]
                c.close_connection(a)
                return b