from DB import conexion as c
import pymysql


def alta_login(dni, contraseña):
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "INSERT INTO login(dni,contraseña) VALUES (%s,%s)"
        values = (dni, contraseña)
        cursor.execute(query, values)
        a.commit()
        print("se registro usuario correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)


def log_in(dni, contraseña):
    print(dni, contraseña)
    a = c.start_connection()
    try:
        cursor = a.cursor()
        query = "SELECT contraseña FROM login WHERE dni= %s"
        values = dni
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchone()
        password = str(b)
        # contraseña=str(contraseña)
        print(password, b)
        if password == "None":
            print("no se encontro el dni indicado")
            return 2
        else:
            password = str(b[0])
            if contraseña == password:
                print("se inicio sesion correctamente")
                return 1
            else:
                print("contraseña incorrecta")
                return 3

    except pymysql.err.OperationalError as err:
        print("Ha ocurrido un error", err)
    c.close_connection(a)


def mostrar_pass(dni):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT contraseña FROM login WHERE dni=%s"
    cursor.execute(query, dni)
    data = cursor.fetchall()
    a.commit()
    return data


def cambiar_contrasena(dniv, dni, password):
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT idlogin FROM login WHERE dni=%s"
    values = dniv
    cursor.execute(query, values)
    a.commit()
    b = cursor.fetchall()
    idl = str(b[0][0])
    print(idl, dniv, dni, password)
    try:
        cursor = a.cursor()
        query = "UPDATE login SET contraseña=%s WHERE idlogin= %s"
        values = (password, idl)
        cursor.execute(query, values)
        cursor = a.cursor()
        query = "UPDATE login SET dni=%s WHERE idlogin= %s"
        values = (dni, idl)
        cursor.execute(query, values)
        print("Contraseña cambiada exitosamente")
        a.commit()
    except pymysql.err.OperationalError as err:
        print("Ha ocurrido un error", err)
    c.close_connection(a)
