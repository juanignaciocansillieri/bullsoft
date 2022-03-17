from DB import conexion as c
import pymysql
from CLASES import alojamiento, productos



class Lote:

    def __init__(self, idproducto, cantidad, fechalote, vencimiento):
        self.idproducto = idproducto
        self.cantidad = cantidad
        self.fechalote = fechalote
        self.vencimiento = vencimiento
        print("se creo lote correctamente")
        self.alta_lote()

    def alta_lote(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO lote(idproducto,cantidad,fechalote,vencimiento) VALUES (%s,%s,%s,%s)"
            values = (self.idproducto, self.cantidad, self.fechalote, self.vencimiento)
            cursor.execute(query, values)
            a.commit()
            vol=productos.ver_vol(self.idproducto)*self.cantidad
            pos=productos.ver_posicion(self.idproducto)
            print("se dio alta al lote correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

def eliminar_lote(fechalote, idproducto):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "DELETE FROM lote WHERE idproducto=%s and fechalote=%s"
        values = (idproducto, fechalote)
        cursor.execute(query, values)
        a.commit()
        print("se elimino lote correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def eliminar_prod_lote(idproducto):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "DELETE FROM lote WHERE idproducto=%s"
        values = idproducto
        cursor.execute(query, values)
        a.commit()
        print("se elimino lote correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def modificar_cantidad(idproducto, fechalote, cantidad):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "UPDATE lote set cantidad=%s WHERE idproducto=%s and fechalote=%s"
        values = (cantidad, idproducto, fechalote)
        cursor.execute(query, values)
        a.commit()
        print("se elimino lote correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def mod_idpruct(codigov, codigon):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT idlote FROM lote WHERE idproducto=%s"
    values = codigov
    cursor.execute(query, values)
    a.commit()
    b = cursor.fetchall()
    idl = str(b[0][0])
    try:
        query = "UPDATE lote set idproducto=%s WHERE idlote=%s"
        values = (codigon, idl)
        cursor.execute(query, values)
        a.commit()

        print("se MODIFICO lote correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

@staticmethod
def contar_filas():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM lote"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def contar_filas_producto(idproducto):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM lote WHERE idproducto=%s"
    values = idproducto
    cursor.execute(query, values)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def listar_lote(idproducto):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT l.idproducto,p.descripcion,l.cantidad,l.fechalote,l.vencimiento FROM lote l JOIN productos p ON l.idproducto=p.codigo WHERE l.idproducto=%s"
        #values = idproducto,idproducto
        cursor.execute(query, idproducto)
        area = cursor.fetchall()
        a.commit()
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)
    return area

def mostrar_lote(idproducto):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT idproducto,cantidad,fechalote,vencimiento FROM lote WHERE idproducto=%s"
    cursor.execute(query, idproducto)
    data = cursor.fetchall()
    a.commit()
    return data

def obtener_cantidades(idproducto):
    cantidad = 0
    cant = 0
    n = contar_filas_producto(idproducto)
    i = 0
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT cantidad FROM lote WHERE idproducto=%s ORDER BY cantidad"
    cursor.execute(query, idproducto)
    cantidad = cursor.fetchall()
    a.commit()
    while i < n:
        cant = cantidad[i][0] + cant
        #print(cantidad[i][0])
        i = i + 1
    #print(cant)
    c.close_connection(a)
    return cant

def obtener_fecha(idproducto):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT vencimiento FROM lote WHERE idproducto=%s ORDER BY vencimiento"
        cursor.execute(query, idproducto)
        param = cursor.fetchone()
        a.commit()
        if param == None:
            return "No hay productos"
        else:
            param=param[0]
            return param
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def verificar(param):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT * FROM lote WHERE fechalote = %s"
    cursor.execute(query, param)
    a.commit()
    data=cursor.fetchall()
    if str(data)=="()":
        return 1
    else: return 0

def fifo(idproducto, cantidad):
    print("fifo")
    cantidad=int(cantidad)
    n = contar_filas_producto(idproducto)
    i = 0
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT idlote FROM lote WHERE idproducto=%s ORDER BY vencimiento"
    cursor.execute(query, idproducto)
    cantidad_total=0
    idlote = cursor.fetchall()
    idlote = idlote[0][0]

    query = "SELECT cantidad FROM lote WHERE idproducto=%s ORDER BY vencimiento"
    cursor.execute(query, idproducto)
    data = cursor.fetchall()
    data = data
    for x in data:
        cantidad_total = cantidad_total + x[0]
    print("cantidad_total ", cantidad_total)
    print("cantidad a sacar ", cantidad)
    #print("n3 ",n3)
    if cantidad_total < cantidad:
        return 1

    if idlote == "()":
        return 0
    else:

        a.commit()

    while i < n:
        print("i ",i)
        query = "SELECT cantidad FROM lote WHERE idproducto=%s ORDER BY vencimiento"
        cursor.execute(query, idproducto)
        data = cursor.fetchall()
        n=data[0][0]
        print("cantidad de lote ", n)
        a.commit()
        if n < cantidad:
            query = "DELETE FROM lote WHERE idproducto=%s and cantidad=%s"
            values = (idproducto, n)
            cursor.execute(query, values)
            a.commit()
            cantidad = cantidad - n
            idlote += 1
            i = i + 1
        else:
            n2 = n - cantidad
            print("n2 ",n2)
            if n2 == 0:

                query = "DELETE FROM lote WHERE idproducto=%s and cantidad=%s"
                values = (idproducto,n)
                cursor.execute(query, values)
                a.commit()

            query = "UPDATE lote set cantidad=%s WHERE idproducto=%s and cantidad=%s and idlote=%s"
            values = (n2, idproducto, n,idlote)
            cursor.execute(query, values)
            a.commit()
            cantidad = cantidad - n
            print("cantidad a sacar con lo sacado ",cantidad)

            idlote += 1
            i = n

def ver_lote(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM lote"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        i = 1
        codigo = "(('" + codigo + "',),)"
        while i < n:
            query = "SELECT fechalote FROM lote WHERE idlote = %s"
            values = i
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            b = str(b)
            #print(b)
            if b == codigo:
                i = n + 1
            else:
                i += 1
        if i == n + 1:
            c.close_connection(a)
            # existe
            return 1
        else:
            c.close_connection(a)
            return 0

def lote_codigo(idproducto):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT fechalote FROM lote WHERE idproducto=%s ORDER BY vencimiento"
        cursor.execute(query, str(idproducto))
        param = cursor.fetchall()
        a.commit()
        print(param)
        c.close_connection(a)
        if str(param) == "()":
            return 0
        else:
            param = param[0][0]
            return param
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)

