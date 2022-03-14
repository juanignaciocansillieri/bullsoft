
from DB import conexion as c, loginDB
from CLASES import area,estanterias,alojamiento,productos,lotes,matriz,usuarios

c.borrar_tabla()
c.crear_tabla()

matriz.alta_datos_matriz(2,2)

#nombre, identificador,posicion, pasillos, segmentos,entrada,salida

area.Area("p1", "p1","1x1", "2", "4","0","0")
area.Area("p2", "p2","1x2", "1", "2","0","0")
area.Area("p3", "p3","2x1", "1", "2","0","0")
area.Area("p4", "p4","2x2", "1", "2","0","0")

#codigo,area,pasillo,posicion,columnas,niveles

estanterias.Estanterias("p1-1-1","p1","1","1","3","3")
estanterias.Estanterias("p2-1-1","p2","1","1","2","2")
estanterias.Estanterias("p3-1-1","p3","1","1","3","1")

#largo, ancho, alto, area, pasillo, segmento, nivel, limite, columna

#codigo, largo, ancho, alto, limite
alojamiento.Alojamiento.modificar_alojamiento("p1-1-1-1-1",5,5,2,"100")

#codigo, marca, cantidad, descripcion, ubicacion, fechalote, vencimiento, fragil, foto,peso,volumen, precio

productos.Productos("1", "1", "1", "p1", "p1-1-1-1-1", "1", "2020-01-01", "0", "0","1","5", "1")
#productos.Productos("2", "2", "2", "p2", "p1-1-1-2-1", "2", "2020-01-01", "0", "0","2","5", "2")
#productos.Productos("3", "3", "3", "p3", "p1-1-1-2-3", "3", "2020-01-01", "0", "0","3","5", "3")
#productos.Productos("4", "4", "4", "p4", "p3-1-1-2-1", "4", "2020-01-01", "0", "0","4","5", "4")
#productos.Productos("5", "5", "5", "p5", "p2-1-1-1-1", "5", "2020-01-01", "0", "0","5","5", "5")
#productos.Productos("6", "6", "6", "p6", "p3-1-1-3-1", "6", "2020-01-01", "0", "0","6","5", "6")
#productos.Productos("7", "7", "7", "p7", "p1-1-1-2-1", "7", "2020-01-01", "0", "0","7","5", "7")
#productos.Productos("8", "8", "8", "p8", "p1-1-1-1-1", "8", "2020-01-01", "0", "0","8","5", "8")
#productos.Productos("9", "9", "9", "p9", "p2-1-1-1-2", "9", "2020-01-01", "0", "0","9","5", "9")

#idproducto, cantidad, fechalote, vencimiento

lotes.Lote(1,10,10,"2020-01-01")

#nombre, apellido, dni, tipo, puesto, nacimiento, mail, foto

usuarios.Usuarios("p1", "p1", "p1", "1", "1", "2020-01-01", "p1", "p1")
usuarios.Usuarios("p2", "p2", "p2", "0", "2", "2020-01-01", "p2", "p2")
usuarios.Usuarios("p3", "p3", "p3", "0", "2", "2020-01-01", "p3", "p2")
loginDB.alta_login("p1","p1")
loginDB.alta_login("p2","p2")
loginDB.alta_login("p3","p3")
