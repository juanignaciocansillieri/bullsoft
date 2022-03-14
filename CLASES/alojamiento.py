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
        self.volumen = int(self.largo) * int(self.ancho) * int(self.alto)
        self.disponibilidad = 100
        self.posicion = str(
            str(area) + "-" + str(pasillo) + "-" + str(segmento) + "-"+ str(columna) + "-" + str(
                nivel))
        self.pasillo = pasillo
        self.limite = limite
        self.codigo = str(
            str(area) + "-" + str(pasillo) + "-" + str(segmento) + "-" + str(columna) + "-" + str(
                nivel))
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
        if data == "()":
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
    data = cursor.fetchall()
    c.close_connection(a)
    return data

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
    query = "SELECT COUNT(*) FROM alojamiento where area=%s"
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
    data = cursor.fetchone()
    a.commit()
    if data == None:
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
    data=int(data[0][0])
    if data == 0:
        return 1
    else:
        return 0

def listar_alojamiento_disponibles_area(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT codigo FROM alojamiento WHERE area=%s and disponibilidad=100"
    cursor.execute(query, area)
    a.commit()
    data = cursor.fetchall()
    c.close_connection(a)
    return data

def ver_area(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT area FROM alojamiento WHERE codigo=%s"
    cursor.execute(query, codigo)
    a.commit()
    data = cursor.fetchall()
    data=data[0][0]
    c.close_connection(a)
    return data

def select_from_area(area):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT codigo FROM alojamiento WHERE area=%s"
    cursor.execute(query, area)
    a.commit()
    data = cursor.fetchall()
    c.close_connection(a)
    return data

def pick_recorrido(): #obetiene recorrido de posiciones en orden
    recorrido_areas = area.ver_recorrido()
    n = len(recorrido_areas)
    final = recorrido_areas[n - 1]
    inicio = recorrido_areas[n - 2]
    recorrido_alojamiento=[]
    n = n - 2
    i = 0
    while i < n:
        recorrido_alojamiento.append(select_from_area(area.ver_area_posicion(recorrido_areas[i])))
        i += 1
    recorrido_alojamiento2=[]
    for data in recorrido_alojamiento:
        for data2 in data:
            recorrido_alojamiento2.append(data2[0])
    return recorrido_alojamiento2

def pick_(lp):
    pick=[]
    lr=pick_recorrido()
    for i in lr:
        for j in lp:
            if i==j:
                pick.append(j)
    return pick


def modificar_dispo_ingreso(prod,cantidad):
    cantidad=int(cantidad)
    codigo=p.ver_posicion(prod)
    v=p.ver_vol(prod)
    v=int(v)
    volumen=v*cantidad
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT disponibilidad FROM alojamiento WHERE codigo=%s"
        cursor.execute(query, codigo)
        data = cursor.fetchall()
        a.commit()
        dispo=int(data[0][0])
        if(int(dispo)<=100):

            query = "SELECT volumen FROM alojamiento WHERE codigo=%s"
            cursor.execute(query, codigo)
            data = cursor.fetchall()
            a.commit()
            vol=int(data[0][0])
            print(volumen,vol)
            x=(volumen*100)/int(vol)

            dispo=dispo-int(x)
            if (dispo >0):

                query = "UPDATE alojamiento set disponibilidad=%s WHERE codigo=%s"
                values = (dispo, codigo)
                cursor.execute(query, values)
                a.commit()
                print("se MODIFICO alojamiento correctamente")
            else:
                print("no hay espacio suficiente")
                return 1

        else:
            print("no hay espacio")
            return 0
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def modificar_dispo_egreso(prod,cantidad):
    cantidad=int(cantidad)
    codigo = p.ver_posicion(prod)
    v = int(p.ver_vol(prod))
    volumen = v * cantidad
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT disponibilidad FROM alojamiento WHERE codigo=%s"
        cursor.execute(query, codigo)
        data = cursor.fetchall()
        a.commit()
        dispo = int(data[0][0])
        if (dispo <= 100):

            query = "SELECT volumen FROM alojamiento WHERE codigo=%s"
            cursor.execute(query, codigo)
            data = cursor.fetchall()
            a.commit()
            data=int(data[0][0])
            vol = int(data*cantidad)
            x=int((volumen*100))/int(vol)
            dispo = dispo + x

            query = "UPDATE alojamiento set disponibilidad=%s WHERE codigo=%s"
            values = (dispo, codigo)
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

def mostrar_al(area,posicion,columna):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT codigo,volumen,limite,disponibilidad,nivel FROM alojamiento WHERE area=%s and segmento=%s and columna=%s"
    cursor.execute(query, (area, posicion, columna))
    data = cursor.fetchall()
    a.commit()
    c.close_connection(a)
    return data


