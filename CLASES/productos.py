import pymysql

from CLASES import lotes, alojamiento
from DB import conexion as c


class Productos:
    def __init__(self, codigo, marca, cantidad, descripcion, ubicacion, fechalote, vencimiento, fragil, foto,
                 peso,volumen, precio):
        self.codigo = codigo
        self.marca = marca
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.foto = foto
        self.fechalote = fechalote
        self.vencimiento = vencimiento
        self.fragil = fragil
        self.peso = peso
        self.volumen=volumen
        self.precio=precio
        self.alta_producto()

    def alta_producto(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO productos (codigo, marca, descripcion,ubicacion,fragil,foto,peso," \
                    "volumen,precio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            values = (self.codigo, self.marca, self.descripcion, self.ubicacion, self.fragil, self.foto,
                      self.peso, self.volumen,self.precio)
            cursor.execute(query, values)
            a.commit()
            lotes.Lote(self.codigo, self.cantidad, self.fechalote, self.vencimiento)
            print("se dio alta producto correctamente")

        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

def borrar_producto(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "DELETE from productos WHERE codigo =%s"
    cursor.execute(query, codigo)
    a.commit()
    lotes.Lote.eliminar_prod_lote(codigo)
    print("Se elimino producto correctamente")

def modificar_produc(codigov, codigon, marca, descripcion, ubicacion, fragil, foto, peso,volumen, precio):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT idproductos FROM productos WHERE codigo=%s"
    values = codigov
    cursor.execute(query, values)
    a.commit()
    b = cursor.fetchone()
    if b == None:
        print("no se encontro el producto indicado")
        return 0
    else:
        #idp = b[0][0]
        idp = b

        try:
            query = "UPDATE productos set codigo=%s WHERE idproductos=%s"
            values = (codigon, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set marca=%s WHERE idproductos=%s"
            values = (marca, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set descripcion=%s WHERE idproductos=%s"
            values = (descripcion, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set foto=%s WHERE idproductos=%s"
            values = (foto, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set fragil=%s WHERE idproductos=%s"
            values = (fragil, idp)
            cursor.execute(query, values)
            a.commit()
            query = "SELECT ubicacion from productos  WHERE idproductos=%s"
            values = idp
            cursor.execute(query, values)
            ubicacionv = cursor.fetchall()
            ubicacionv = str(ubicacionv[0][0])
            a.commit()
            query = "UPDATE productos set ubicacion=%s WHERE idproductos=%s"
            values = (ubicacion, idp)
            cursor.execute(query, values)
            a.commit()
            #
            query = "UPDATE productos set peso=%s WHERE idproductos=%s"
            values = (peso, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set volumen=%s WHERE idproductos=%s"
            values = (volumen, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set precio=%s WHERE idproductos=%s"
            values = (precio, idp)
            cursor.execute(query, values)
            a.commit()
            lotes.mod_idpruct(codigov, codigon)
            print("se MODIFICO producto correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

def buscar_product(param):
    a = c.start_connection()
    cursor = a.cursor()
    query = ("SELECT codigo,descripcion,marca FROM productos WHERE codigo=%s or descripcion=%s or marca=%s")
    cursor.execute(query, (param, param, param))
    data = cursor.fetchall()
    a.commit()
    return data


def buscar_product_rows(param):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT codigo,descripcion,marca FROM productos WHERE codigo=%s or descripcion=%s or marca=%s"
    data = cursor.execute(query, (param, param, param))
    a.commit()
    return data

def mostrar_product(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = (
        "SELECT p.codigo, p.marca, l.cantidad, p.descripcion,p.ubicacion, l.fechalote, l.vencimiento,p.fragil,p.foto,p.peso,p.volumen,p.precio FROM productos p JOIN lote l ON p.codigo = l.idproducto WHERE codigo=%s")
    cursor.execute(query, codigo)
    data = cursor.fetchall()
    a.commit()

    if data == "()":
        print("no se encontro el producto indicado")
        return 0
    else:
        return data


def listar_prod():
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT codigo,descripcion,marca FROM productos"
        cursor.execute(query)
        productos = cursor.fetchall()
        a.commit()
    except pymysql.err.OperationalError as err:
        productos = ""
        print("Hubo un error:", err)
    c.close_connection(a)
    return productos


def contar_filas():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM productos"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n


def ver_cod(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM productos"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    i = 0
    codigo = "(('" + codigo + "',),)"
    while i <= n:
        query = "SELECT codigo FROM productos WHERE idproductos = %s"
        values = i
        cursor.execute(query, values)
        a.commit()
        cod = cursor.fetchall()
        cod = str(cod)
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

def ver_desc(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT descripcion FROM productos WHERE codigo=%s"
    cursor.execute(query,str(codigo))
    data = cursor.fetchall()
    a.commit()
    if str(data) == "()":
        print("no se encontro el producto indicado")
        return 0
    else:
        c.close_connection(a)
        return data[0][0]


def ver_vol(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT volumen FROM productos WHERE codigo=%s"
    cursor.execute(query,codigo)
    data = cursor.fetchall()
    a.commit()
    if data == "()":
        print("no se encontro el producto indicado")
        return 0
    else:
        data=data[0][0]
        return data
    c.close_connection(a)

def pick_posiciones(lc): #se le da una lsita de codigos y devuelve las posiciones
    rp=[]
    for data in lc:
        p = ver_posicion(data)
        rp.append(p)
    return rp

def pick_productos(lc,pick): #confirma el codigo del prodcuto con las posiciones (arregla los que son dobles)
    l=[]
    i=0
    j=0
    n1=int(len(lc))
    n2=int(len(pick))
    while i<n2:
        while j<n1:
            p=buscar_prod_pick(pick[i],lc[j])
            if p==0:
                j+=1
            else:
                #print("p,",p)
                l.append(p)
                lc[j]=""
                #print(lc)
                j=0
        j=0
        i+=1

    return l


def buscar_prod_pick(posicion,codigo): #trae el codigo mientras exista coincidencia en posicion y codigo
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT codigo FROM productos WHERE codigo=%s AND ubicacion=%s"
    cursor.execute(query, (codigo,posicion))
    data = cursor.fetchall()
    a.commit()
    data
    if str(data)== "()":
        return 0
    else: return data[0][0]
    c.close_connection(a)
    return data

def buscar_prod_pos(posicion):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT codigo FROM productos WHERE ubicacion=%s"
    cursor.execute(query, posicion)
    data = cursor.fetchall()
    a.commit()
    #print(data)
    data = data
    c.close_connection(a)
    return data

def ver_precio(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT precio FROM productos WHERE codigo=%s"
    cursor.execute(query, codigo)
    data = cursor.fetchone()
    a.commit()
    if data == None:
        print("no se encontro el producto indicado")
        return 0
    else:
        data = data[0]
        return data
    c.close_connection(a)

def ver_posicion(codigo):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT ubicacion FROM productos WHERE codigo=%s"
    cursor.execute(query, codigo)
    data = cursor.fetchone ()
    a.commit()
    #print("DATA, ",data)
    data = str(data[0])
    c.close_connection(a)
    return data


def ver_area(codigo):
    posicion=ver_posicion(codigo)
    area=alojamiento.ver_area(posicion)
    return area


def contar_productos_ubicacion(ubicacion):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT count(*) FROM productos WHERE ubicacion=%s"
    cursor.execute(query, ubicacion)
    data = cursor.fetchall()
    a.commit()
    data=int(data[0][0])
    c.close_connection(a)
    return data

def listar_productos_ubicacion(ubicacion):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT p.codigo, p.descripcion, p.marca, l.cantidad,l.vencimiento FROM productos p JOIN lote l ON p.codigo = l.idproducto WHERE ubicacion=%s"
    cursor.execute(query, ubicacion)
    data = cursor.fetchall()
    data=data[0][0]
    a.commit()
    c.close_connection(a)
    return data

def contar_productos_ubicacion(ubicacion):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT count(*) FROM productos WHERE ubicacion=%s"
        cursor.execute(query, ubicacion)
        data = cursor.fetchall()
        a.commit()
        data = int(data[0][0])
        c.close_connection(a)
        return data

def listar_productos_ubicacion(ubicacion):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT p.codigo, p.descripcion, p.marca, l.cantidad,l.vencimiento FROM productos p JOIN lote l ON p.codigo = l.idproducto WHERE ubicacion=%s"
        cursor.execute(query, ubicacion)
        data = cursor.fetchall()
        a.commit()
        c.close_connection(a)
        return data