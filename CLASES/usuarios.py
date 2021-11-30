
import pymysql

from DB import conexion as c


class Usuarios:

    def __init__(self, nombre, apellido, dni, tipo, puesto, nacimiento, mail, foto):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.alta = 1
        self.puesto = puesto
        self.nacimiento = nacimiento
        self.mail = mail
        self.foto = foto
        self.alta_usuario()

    def alta_usuario(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO usuarios(nombre,apellido,dni,tipo,alta,puesto,nacimiento,mail,foto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (
                self.nombre, self.apellido, self.dni, self.tipo, self.alta, self.puesto, self.nacimiento, self.mail,
                self.foto)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def buscar_user(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT dni,nombre,apellido,tipo,nacimiento FROM usuarios WHERE dni=%s or nombre=%s or apellido=%s"
        cursor.execute(query, (param, param, param))
        data = cursor.fetchall()
        a.commit()
        return data

    def buscar_user_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT dni,nombre,apellido,tipo,nacimiento FROM usuarios WHERE dni=%s or nombre=%s or apellido=%s"
        data = cursor.execute(query, (param, param, param))
        a.commit()
        return data

    def mostrar_user(dni):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT dni,nombre,apellido,tipo,nacimiento,puesto,alta,mail,foto FROM usuarios WHERE dni=%s"
        cursor.execute(query, dni)
        data = cursor.fetchall()
        a.commit()
        return data

    def ab_usuario(dni):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "UPDATE usuarios set alta= IF(alta = '0', alta + 1, alta-1) WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_datos_user(dniv, dnin, nombre, apellido, tipo, puesto, nacimiento, mail, foto):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idusuarios FROM usuarios WHERE dni=%s"
        values = dniv
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        idu = str(b[0][0])
        try:
            query = "UPDATE usuarios SET nombre=%s WHERE idusuarios=%s"
            values = (nombre, idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET apellido=%s WHERE idusuarios=%s"
            values = (apellido, idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET dni=%s WHERE idusuarios=%s"
            values = (dnin, idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET nacimiento=%s WHERE idusuarios=%s"
            values = (nacimiento, idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET tipo=%s WHERE idusuarios=%s"
            values = (tipo, idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET puesto=%s WHERE idusuarios=%s"
            values = (puesto, idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET mail=%s WHERE idusuarios=%s"
            values = (mail, idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET foto=%s WHERE idusuarios=%s"
            values = (foto, idu)
            cursor.execute(query, values)
            a.commit()
            print("se modifico  usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def verificar(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT * FROM usuarios WHERE dni = %s"
        product = cursor.execute(query, param)
        a.commit()
        print("VERRRI", product)
        return product


def contar_filas():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM usuarios WHERE alta = 1"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n


def listar_user():
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT dni,nombre,apellido,tipo,nacimiento FROM usuarios WHERE alta = 1"
        cursor.execute(query)
        user = cursor.fetchall()
        a.commit()
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)
    return user


def ver_dni(dni):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM usuarios"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    i = 0
    dni = "(('" + dni + "',),)"
    while i < n:
        query = "SELECT dni FROM usuarios WHERE idusuarios = %s"
        values = i
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        b = str(b)
        print(b)
        if b == dni:
            i = n + 1
        else:
            i += 1
    if i == n + 1:
        c.close_connection(a)
        # dni existe
        return 1
    else:
        c.close_connection(a)
        return 0


def ver_tipo(dni):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT tipo FROM usuarios where dni=%s"
    values = dni
    cursor.execute(query, values)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    if b == "1":
        admin = True
    else:
        admin = False
    return admin
