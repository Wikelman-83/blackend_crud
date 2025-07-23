import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",        # Si usas XAMPP, el host es localhost
        user="root",             # Usuario por defecto de XAMPP
        password="",             # Contraseña vacía por defecto en XAMPP
        database="crud_db"       # Nombre de la base de datos creada
    )
