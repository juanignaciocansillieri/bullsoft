from DB import conexion as c
import pymysql


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
            query = "SELECT l.idproducto,p.descripcion,l.cantidad,l.fechalote,l.vencimiento FROM lote l JOIN productos p ON l.idproducto=p.codigo WHERE idproducto=%s"
            values = idproducto
            cursor.execute(query, values)
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
        n = Lote.contar_filas_producto(idproducto)
        i = 0
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT cantidad FROM lote WHERE idproducto=%s ORDER BY cantidad"
        cursor.execute(query, idproducto)
        cantidad = cursor.fetchall()
        a.commit()
        while i < n:
            cant = cantidad[i][0] + cant
            print(cantidad[i][0])
            i = i + 1
        print(cant)
        c.close_connection(a)
        return cant

    def obtener_fecha(idproducto):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT vencimiento FROM lote WHERE idproducto=%s ORDER BY vencimiento"
            cursor.execute(query, idproducto)
            param = cursor.fetchall()
            param = param[0][0]
            a.commit()
        except pymysql.err.OperationalError as err:
            param = ""
            print("Hubo un error:", err)
        c.close_connection(a)
        return param

    def verificar(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT * FROM lote WHERE fechalote = %s"
        product = cursor.execute(query, param)
        a.commit()
        print("VERRRI", product)
        return product

    def fifo(idproducto, cantidad):
        n = Lote.contar_filas_producto(idproducto)
        i = 0
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idlote FROM lote WHERE idproducto=%s ORDER BY vencimiento"
        cursor.execute(query, idproducto)
        idlote = cursor.fetchall()
        idlote = idlote[0][0]
        if idlote == "none":
            return 0
        else:

            a.commit()

            while i < n:
                query = "SELECT cantidad FROM lote WHERE idproducto=%s ORDER BY vencimiento"
                cursor.execute(query, idproducto)
                n = cursor.fetchall()
                a.commit()
                n = n[0][0]

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
                    if n2 == 0:
                        query = "DELETE FROM lote WHERE idproducto=%s and cantidad=%s"
                        values = (idproducto, n2)
                        cursor.execute(query, values)
                        a.commit()
                    query = "UPDATE lote set cantidad=%s WHERE idproducto=%s and cantidad=%s"
                    values = (n2, idproducto, n)
                    cursor.execute(query, values)
                    a.commit()
                    cantidad = cantidad - n
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
            print(b)
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
