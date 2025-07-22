
from flask import render_template, request, jsonify
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    nombre = data.get('nombre')
    edad = data.get('edad')
    correo = data.get('correo')
    clasificacion = data.get('clasificacion')

    print(f"Recibido: {nombre}, {edad} años, {correo}, clasif.: {clasificacion}")
    return jsonify({"message": "¡Datos recibidos correctamente!"})
