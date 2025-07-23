from flask import render_template, request, jsonify
from app import app
from app.db import get_connection  # Asegúrate de que la conexión esté bien importada

@app.route('/')
def index():
    # Conectar a la base de datos
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # Esto asegura que los resultados sean diccionarios (clave=nombre de columna)

    # Obtener todos los usuarios
    cursor.execute("SELECT * FROM usuarios")
    users = cursor.fetchall()

    # Cerrar la conexión
    conn.close()

    # Pasar los usuarios a la plantilla
    return render_template('index.html', users=users)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    nombre = data.get('nombre')
    edad = data.get('edad')
    correo = data.get('correo')
    clasificacion = data.get('clasificacion')

    # Conectar a la base de datos MySQL
    conn = get_connection()
    cursor = conn.cursor()

    # Insertar datos en la tabla usuarios
    cursor.execute("INSERT INTO usuarios (nombre, edad, correo, clasificacion) VALUES (%s, %s, %s, %s)", 
                   (nombre, edad, correo, clasificacion))
    
    # Confirmar la transacción y cerrar la conexión
    conn.commit()
    conn.close()

    return jsonify({"message": "¡Datos guardados correctamente!"})
