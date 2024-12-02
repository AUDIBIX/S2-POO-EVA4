from flask import Flask, jsonify
from flask_cors import CORS
from repositories import TravelRepository
from services import TravelService
from controllers import TravelController
import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='travel_agency',
            collation='utf8mb4_general_ci'
        )
        return connection
    except Error as e:
        logger.exception(f"Error al conectar con MySQL: {str(e)}")
        raise

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    try:
        db_connection = get_db_connection()
        repository = TravelRepository(db_connection)
        service = TravelService(repository)
        controller = TravelController(service)
        app.register_blueprint(controller.routes)
        
    except Exception as e:
        logger.exception("Error al inicializar la aplicación")
        raise
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)