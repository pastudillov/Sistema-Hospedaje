import mysql.connector

# Función para conectar a la base de datos
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Hospedaje"
    )
    return conexion

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conexion):
    conexion.close()