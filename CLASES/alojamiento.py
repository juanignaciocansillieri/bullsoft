import pymysql

from CLASES import area
from DB import conexion as c
from CLASES import productos as p
from CLASES import area as a




class Alojamiento:
    def __init__(self, largo, ancho, alto, area, pasillo, segmento, nivel, limite, columna):
        self.columna = columna
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.area = area
        self.segmento = segmento
        self.columna = columna
        self.nivel = nivel
        self.volumen = self.largo * self.ancho * self.alto
        self.disponibilidad = 100
        self.posicion = str(
            str(area) + "-" + str(pasillo) + "-" + str(self.segmento) + "-"+ str(columna) + "-" + str(
                nivel))
        self.pasillo = pasillo
        self.limite = limite
        self.codigo = str(
            str(area) + "-" + str(pasillo) + "-" + str(self.segmento) + "-" + str(columna) + "-" + str(
                nivel))
        print(self.codigo)
        self.alta_alojamiento()
        print("se creo alojamiento correctamente")

    def alta_alojamiento(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO alojamiento(codigo,area,largo,ancho,alto,volumen,disponibilidad,posicion,pasillo," \
                    "segmento,nivel,limite,columna) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            values = (
                self.codigo, self.area, self.largo, self.ancho, self.alto, self.volumen, self.disponibilidad,
                self.posicion,
                self.pasillo, self.segmento, self.nivel, self.limite, self.columna)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta alojamiento correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def ab_alojamiento(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "UPDATE alojamiento set disponibilidad= IF(disponibilidad = '0', disponibilidad + 1, disponibilidad-1) WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO alojamiento correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    @staticmethod
    def modificar_alojamiento(codigo, largo, ancho, alto, limite):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "UPDATE alojamiento set largo=%s WHERE codigo=%s"
            values = (largo, codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE alojamiento set ancho=%s WHERE codigo=%s"
            values = (ancho, codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE alojamiento set alto=%s WHERE codigo=%s"
            values = (alto, codigo)
            cursor.execute(query, values)
            a.commit()
            volumen = largo * ancho * alto
            query = "UPDATE alojamiento set volumen=%s WHERE codigo=%s"
            values = (volumen, codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE alojamiento set limite=%s WHERE codigo=%s"
            values = (limite, codigo)
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO alojamiento correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def elim_pos_area(area):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "DELETE  FROM alojamiento WHERE area=%s"
            values = area
            cursor.execute(query, values)
            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    # agragar areas en el futuro

    def buscar_aloj(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = (
            "SELECT codigo,largo,ancho,alto,volumen,pasillo,segmento,disponibilidad,posicion,limite,columna FROM alojamiento WHERE codigo=%s")
        cursor.execute(query, (param, param, param, param))
        data = cursor.fetchall()
        a.commit()
        return data

    def buscar_aloj_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = (
            "SELECT codigo,largo,ancho,alto,volumen,pasillo,segmento,disponibilidad,posicion,limite,columna FROM alojamiento WHERE codigo=%s")
        data = cursor.execute(query, param)
        a.commit()
        return data

    def mostrar_aloj(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = (
            "SELECT codigo,largo,ancho,alto,volumen,pasillo,alojamiento,disponibilidad,posicion,limite,columna FROM "
            "alojamiento WHERE codigo=%s")
        cursor.execute(query, codigo)
        data = cursor.fetchall()
        a.commit()
        if data == "None":
            print("no se encontro el alojamietno indicado")
            return 0
        else:
            return data

    @staticmethod
    def listar_alojamiento():
        a = c.start_connection() #creo un objeto conexion a DB
        cursor = a.cursor() #creo un cursor (puntero a espacio de memoria a la pc) de la DB
        try:
            query = "SELECT codigo,largo,ancho,alto,volumen,pasillo,disponibilidad,posicion,limite,columna FROM " \
                    "alojamiento "
            cursor.execute(query) #en la variable cursor ejecuto el query
            alojamientos = cursor.fetchall()
            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return alojamientos


    def listar_posicion_alojamiento(area):
        print(area)
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = f"SELECT codigo,pasillo,segmento,limite FROM alojamiento WHERE area='{area}'"
            cursor.execute(query)
            alojamientos = cursor.fetchall()
            a.commit()
        except pymysql.err.OperationalError as err:
            print("Ocurrió un error: ", err)
        c.close_connection(a)
        return alojamientos



def contar_filas():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM alojamiento"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

    def listar_alojamiento_disponibles_area(area):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT codigo,largo,ancho,alto,volumen,pasillo,disponibilidad,posicion,limite FROM alojamiento WHERE disponibilidad=0 and area=%s"
            cursor.execute(query, area)
            productos = cursor.fetchall()

            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return productos

    def contar_filas_disponibles_area(area):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM alojamiento where disponibilidad=0 and area=%s"
        cursor.execute(query, area)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

def mostrar_filas_area(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT codigo FROM alojamiento WHERE area=%s"
    cursor.execute(query,area)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

    def listar_alojamiento_disponibles_area(area):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT codigo,largo,ancho,alto,volumen,pasillo,disponibilidad,posicion,limite FROM alojamiento WHERE disponibilidad=0 and area=%s"
            cursor.execute(query, area)
            productos = cursor.fetchall()

            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return productos

    def contar_filas_disponibles_area(area):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM alojamiento where disponibilidad=0 and area=%s"
        cursor.execute(query, area)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

def contar_nivel(nombre):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT niveles FROM area WHERE nombre=%s"
    cursor.execute(query,nombre)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def ver_codigo(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM alojamiento"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    i = 0
    codigo = "(('" + codigo + "',),)"
    while i < n:
        query = "SELECT codigo FROM alojamiento WHERE idalojamiento = %s"
        values = i
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        b = str(b)
        print(b)
        if b == codigo:
            i = n + 1
        else:
            i += 1
    if i == n + 1:
        c.close_connection(a)
        # codigo existe
        return 1
    else:
        c.close_connection(a)
        return 0

def ver_dispo(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT disponibilidad FROM alojamiento WHERE codigo=%s"
    cursor.execute(query, codigo)
    data = cursor.fetchall()
    a.commit()
    if data == "None":
        print("no se encontro el alojamietno indicado")
        return 0
    else:
        return data

def verificar_posicion(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT volumen FROM alojamiento WHERE codigo=%s"
    cursor.execute(query, codigo)
    data = cursor.fetchall()
    a.commit()
    if data == 0:
        return 1
    else:
        return 0

def pick(producto):
    nal=contar_filas()
    ial=0
    nar=a.contar_filas()
    iar=0
    nseg=a.contar_segmentos()
    iseg=0
    ncol=a.contar_columnas()
    icol=0
    nniv=contar_nivel()
    iniv=0
    inicio=a.ver_e()
    posicioninicio=a.ver_posicion(inicio)
    print(posicioninicio)
    #while iar<nar:
     #   while iseg<nseg:










def modificar_dispo_ingreso(codigo,volumen):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT disponibilidad FROM alojamiento WHERE codigo=%s"
        cursor.execute(query, codigo)
        data = cursor.fetchall()
        a.commit()
        dispo=data[0]
        if(dispo<100):

            query = "SELECT volumen FROM alojamiento WHERE codigo=%s"
            cursor.execute(query, codigo)
            data = cursor.fetchall()
            a.commit()
            vol=data[0]

            x=(vol*100)/volumen

            dispo=dispo-x
            if (dispo <100):

                query = "UPDATE alojamiento set disponibilidad=%s WHERE codigo=%s"
                values = (dispo, codigo)
                cursor.execute(query, values)
                a.commit()
                print("se MODIFICO alojamiento correctamente")
            else:
                print("no hay disponibilidad suficiente")
                return 1

        else:
            print("no hay disponibilidad")
            return 0
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def modificar_dispo_egreso(codigo,prod,cantidad):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT disponibilidad FROM alojamiento WHERE codigo=%s"
        cursor.execute(query, codigo)
        data = cursor.fetchall()
        a.commit()
        dispo = data[0]
        if (dispo < 100):

            query = "SELECT volumen FROM producto WHERE codigo=%s"
            cursor.execute(query, prod)
            data = cursor.fetchall()
            a.commit()
            vol = data[0]*cantidad

            x = (vol * 100) / vol

            dispo = dispo + x

            query = "UPDATE alojamiento set disponibilidad=%s WHERE codigo=%s"
            values = (x, codigo)
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO alojamiento correctamente")

        else:
            print("no hay disponibilidad")
            return 0
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def busc_pos(area,segmento,columna):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT * FROM alojamiento WHERE segmento=%s AND columna=%s AND area=%s"
    cursor.execute(query, (segmento,columna,area))
    data = cursor.fetchall()
    a.commit()
    if data == "None":
        print("no se encontro el alojamietno indicado")
        return 0
    else:
        return data



"""
def asignacion_de_ubicacion():
    a=c.start_connection()
    cursor=a.cursor()
    try:
        query = "SELECT COUNT (*) FROM alojamiento where disponibilidad = %s"
        values = 1
        cursor.execute(query,values)
        a.commit()
        n=int(cursor.fetchall())
        i=0
        ii=0
        while i<n:
            query = "SELECT codigo FROM alojamiento WHERE idmatriz = %s and disponibilidad = 1"
            values = ii
            cursor.execute(query,values)
            a.commit()
            codigo=cursor.fetchall()
            codigo=str(codigo[0][0])
            if i==n-1 and codigo == "none":
                print("no hay alojamiento disponibles")
                pass
            else: 
                query = "UPDATE alojamiento SET disponibilidad=0 WHERE codigo=%s"
                values = codigo
                cursor.execute(query,values)
                a.commit()
                return codigo        
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)
        """
