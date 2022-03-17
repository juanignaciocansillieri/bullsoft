import pymysql
import os


# AXIOMAS Y OBLIGACIONES A LA HORA DE LA CODIFICACION:
# se abre conexion unicamente cuando estamos por usar la base de datos y al finalizar se la cierra
# cada de vez que se usar el cursor, posteriormente se lo cierra
# para la devolucion de datos de cursor se usara fetchall e intantaneamente se lo convertira


def first_connection():  # inicia conexion a db
    h = 'localhost'
    p = 3306
    u = os.environ.get('USER_MYSQL')
    ps = os.environ.get('PASSWORD_MYSQL')
    db = os.environ.get('sakyra') #aca iba sakyra
    try:
        con = pymysql.Connect(host=h, port=p, user=u, password=ps, database=db)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)

    return con


def start_connection():  # inicia conexion a db
    h = 'localhost'
    p = 3306
    u = os.environ.get('USER_MYSQL')
    ps = os.environ.get('PASSWORD_MYSQL')
    db = os.environ.get('DB_MYSQL')

    try:
        con = pymysql.Connect(host=h, port=p, user=u, password=ps, database=db)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)

    return con


def close_connection(con):  # cierra conexion a db
    try:
        con.close()
        # print("se cerro conexion\n",con)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)


def borrar_tabla():  # borra tablas (posible modificacion futura: ingresar el nombre de la tabla y que la borre)
    # se usa "," para mas de una
    con = start_connection()
    q1 = """drop database if exists bullsoft;"""
    q2 = """create database if not exists bullsoft;"""
    # q = "DROP TABLE IF EXISTS productos, usuarios,alojamiento,login,matriz,datosmatriz;"
    try:
        cur = con.cursor()
        cur.execute(q1)
        cur.execute(q2)
        cur.close()
        print("se borro las tablas con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    close_connection(con)


def crear_tabla():  # crea una tabla (al iniciar por primera vez el programa se crearan todas)
    q0 = """CREATE DATABASE IF NOT EXISTS bullsoft;"""

    q1 = """USE bullsoft;"""

    q2 = """CREATE TABLE IF NOT EXISTS login (
    idlogin INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    dni VARCHAR(20) NOT NULL,
    contraseña VARCHAR(20) NOT NULL
    );"""

    q3 = """CREATE TABLE IF NOT EXISTS tipouser (
    idtipouser INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    identificador VARCHAR(20) NOT NULL
    );"""

    q4 = """CREATE TABLE IF NOT EXISTS usuarios (
    idusuarios INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    alta BINARY(1) NOT NULL,
    puesto VARCHAR(20) NOT NULL,
    nacimiento DATE NOT NULL,
    mail VARCHAR(20) NOT NULL,
    foto VARCHAR(100) NOT NULL
    );"""

    q5 = """CREATE TABLE IF NOT EXISTS lote (
    idlote INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    idproducto VARCHAR(20) NOT NULL,
    cantidad int not null,
    fechalote VARCHAR(20) NOT NULL,
    vencimiento DATE
    );"""

    q6 = """CREATE TABLE IF NOT EXISTS condicion (
    idcondicion INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    identificador VARCHAR(20) NOT NULL
    );"""

    q7 = """CREATE TABLE IF NOT EXISTS alojamiento (
    idalojamiento INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    area VARCHAR(20) NOT NULL,
    pasillo VARCHAR(20) NOT NULL,
    segmento VARCHAR(20) NOT NULL,
    columna VARCHAR(20) NOT NULL,
    nivel VARCHAR(20) NOT NULL,
    codigo VARCHAR(100) NOT NULL,
    posicion VARCHAR(100) NOT NULL,
    largo INT NOT NULL,
    ancho INT NOT NULL,
    alto INT NOT NULL,
    volumen VARCHAR(20) NOT NULL,
    disponibilidad VARCHAR(20) NOT NULL,
    limite VARCHAR(20) NOT NULL
    );"""

    q8 = """ CREATE TABLE IF NOT EXISTS matrizarea (
    idalojamiento INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    area VARCHAR(20) NOT NULL,
    fila VARCHAR(20) NOT NULL,
    columna VARCHAR(20) NOT NULL
    );"""

    q14 = """CREATE TABLE IF NOT EXISTS datosmatrizarea (
    iddatosmatrizarea INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    filas INT NOT NULL,
    columnas INT NOT NULL
    );"""

    q9 = """ CREATE TABLE IF NOT EXISTS matriz (
    idmatriz INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    area VARCHAR(20) NOT NULL,
    segmento VARCHAR(20) NOT NULL,
    fila VARCHAR(20) NOT NULL,
    nivel VARCHAR(20) NOT NULL,
    disponibilidad BINARY(1) NOT NULL
    );"""

    q10 = """CREATE TABLE IF NOT EXISTS datosmatriz (
    iddatosmatriz VARCHAR(20) PRIMARY KEY NOT NULL,
    area VARCHAR(20) NOT NULL,
    segmento VARCHAR(20) NOT NULL,
    filas VARCHAR(20) NOT NULL,
    altura VARCHAR(20) NOT NULL
    );"""

    q11 = """CREATE TABLE IF NOT EXISTS area (
    idarea INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    identificador VARCHAR(20) NOT NULL,
    posicion VARCHAR(20) NOT NULL,
    pasillos VARCHAR(20) NOT NULL,
    segmentos VARCHAR(20) NOT NULL,
    entrada INT,
    salida INT,
    disponibilidad VARCHAR(5) NOT NULL
    );"""

    q12 = """CREATE TABLE IF NOT EXISTS productos (
    idproductos INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    marca VARCHAR(20) NOT NULL,
    descripcion VARCHAR(60) NOT NULL,
    ubicacion VARCHAR(20) NOT NULL,
    fragil BINARY(1) NOT NULL,
    foto VARCHAR(100) NOT NULL,
    peso INT NOT NULL,
    volumen INT NOT NULL,
    precio INT
    );"""

    q13 = """CREATE TABLE IF NOT EXISTS movimientos (
    idmovimientos INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    tipo BINARY(1) NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    cantidad INT NOT NULL,
    motivo VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL
    );"""

    q16 = """CREATE TABLE IF NOT EXISTS estanterias (
    idestanterias INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo VARCHAR(50) NOT NULL,
    area VARCHAR(20) NOT NULL,
    pasillo VARCHAR(20) NOT NULL,
    posicion VARCHAR(20) NOT NULL,
    columnas VARCHAR(20) NOT NULL,
    niveles VARCHAR(20) NOT NULL
    );"""

    con = first_connection()
    cur = con.cursor()
    try:
        cur.execute(q0)
        cur.execute(q1)
        cur.execute(q2)
        # cur.execute(q3)
        cur.execute(q4)
        cur.execute(q5)
        # cur.execute(q6)
        cur.execute(q7)
        cur.execute(q8)
        # cur.execute(q9)
        # cur.execute(q10)
        cur.execute(q11)
        cur.execute(q12)
        cur.execute(q13)
        cur.execute(q14)
        cur.execute(q16)
        cur.close()
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    close_connection(con)

def verificar_deposito():
    a = first_connection()
    cursor = a.cursor()
    try:
        query = "SELECT * FROM area "
        cursor.execute(query)
        a.commit()
        b = cursor.fetchone()
        control1 = str(b)
        if control1 == "None":  # and
            print(control1)
            print("no se encuentra")
            return 0
        else:
            return 1
    except pymysql.err.OperationalError as err:
        print("Ha ocurrido un error", err)

    close_connection(a)
