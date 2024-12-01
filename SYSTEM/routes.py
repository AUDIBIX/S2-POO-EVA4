from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
from datetime import datetime
import random 
app = Flask(__name__)
CORS(app)

API_BASE_URL = "http://127.0.0.1:5000"

@app.template_filter('date')
def format_date(value, format='%Y-%m-%d'):
    if isinstance(value, datetime):
        return value.strftime(format)
    return value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/paises', methods=['GET'])
def get_paises():
    try:
        response = requests.get(f"{API_BASE_URL}/api/paises")
        response.raise_for_status()
        paises = response.json()
        return jsonify(paises.get("data", []))
    except Exception as e:
        app.logger.error(f"Error al obtener países: {str(e)}")
        return jsonify({"error": "Error al obtener países"}), 500

@app.route('/api/paises/<int:pais_id>/ciudades', methods=['GET'])
def get_ciudades(pais_id):
    try:
        response = requests.get(f"{API_BASE_URL}/api/paises/{pais_id}/ciudades")
        response.raise_for_status()
        ciudades = response.json()
        return jsonify(ciudades.get("data", []))
    except Exception as e:
        app.logger.error(f"Error al obtener ciudades para país {pais_id}: {str(e)}")
        return jsonify({"error": "Error al obtener ciudades"}), 500

@app.route('/api/generar-paquetes', methods=['POST'])
def generar_paquetes():
    number = random.randint(2, 5)
    try:
        data = request.get_json()
        pais = data.get('pais', '')
        ciudad = data.get('ciudad', '')
        fecha_ida = data.get('fechaIda', '')
        fecha_regreso = data.get('fechaRegreso', '')
        tipo_paquete = data.get('tipoPaquete', '')
        if not pais or not ciudad or not fecha_ida or not fecha_regreso or not tipo_paquete:
            return jsonify({"error": "Todos los campos son obligatorios"}), 400

        paquetes = [
            {
                'Destino': f'{pais} - {ciudad}',
                'descripcion': f'Paquete {tipo_paquete} para visitar {ciudad}. Salida: {fecha_ida} - Regreso: {fecha_regreso}',
                'precio': round(1000 + i * 500, 2), 
                'fecha_salida': fecha_ida,
                'fecha_regreso': fecha_regreso
            }
            for i in range(number) 
        ]
        return jsonify({'paquetes': paquetes})
    except Exception as e:
        app.logger.error(f"Error al generar paquetes: {str(e)}")
        return jsonify({"error": "Error al generar paquetes"}), 500

@app.route('/', methods=['POST'])
def root_post():
    return jsonify({"error": "Esta ruta no acepta solicitudes POST para este proposito."}), 405

if __name__ == '__main__':
    app.run(debug=True, port=5001)
