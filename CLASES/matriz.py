from sys import setprofile
from typing import NoReturn
import pymysql
import os
from DB import conexion as c
from CLASES import area as ar

import numpy as np

def crear_matriz_areas(x,y):
    codigo=str(str(x)+"x"+str(y))
    ar.Area(codigo,codigo,codigo,0,0,0,0,0,0)
    print(x,y)
    print("se dio de alta a la matriz correctamente")
        
    

def alta_datos_matriz(ancho,largo):
    a=c.start_connection()
    cursor=a.cursor()
    try:
        query = "INSERT INTO datosmatrizarea(filas,columnas) VALUES (%s,%s)"
        values = (ancho,largo)
        cursor.execute(query, values)
        a.commit()
        print("se cargaron datos de la matriz correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def importar_datos_matriz():
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT filas, columnas FROM datosmatrizarea"
        cursor.execute(query)
        data = cursor.fetchall()
        a.commit()
        print("se importaron datos de la matriz correctamente")
        return data
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)


