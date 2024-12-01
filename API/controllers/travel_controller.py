from flask import Blueprint, jsonify, request
from http import HTTPStatus
from typing import List, Dict, Optional

class TravelController:
    def __init__(self, service):
        self.service = service
        self.routes = Blueprint('travel', __name__)
        self._registerRoutes()

    def _registerRoutes(self) -> None:
        # Ruta raíz
        @self.routes.route('/', methods=['GET'])
        def index():
            return self._successResponse({
                'api_name': 'EV4',
                'rutas': {
                    'ciudades': {
                        'actividades': {
                            'ruta': '/api/ciudades/<cityId>/actividades',
                            'método': 'GET'
                        },
                        'autos': {
                            'ruta': '/api/ciudades/<cityId>/autos',
                            'método': 'GET'
                        },
                        'detalles': {
                            'ruta': '/api/ciudades/<cityId>/detalles',
                            'método': 'GET'
                        },
                        'hoteles': {
                            'ruta': '/api/ciudades/<cityId>/hoteles',
                            'método': 'GET'
                        }
                    },
                    'países': {
                        'obtener_todos': {
                            'ruta': '/api/paises',
                            'método': 'GET'
                        },
                        'obtener_por_id': {
                            'ruta': '/api/paises/<id>',
                            'método': 'GET'
                        },
                        'ciudades': {
                            'ruta': '/api/paises/<id>/ciudades',
                            'método': 'GET'
                        }
                    }
                }
            })

        # GET Routes
        @self.routes.route('/api/paises', methods=['GET'])
        def getCountries():
            try:
                countries = self.service.getAll()
                return self._successResponse(countries)
            except Exception as e:
                return self._errorResponse(str(e), 500)

        @self.routes.route('/api/paises/<int:id>', methods=['GET'])
        def getCountry(id):
            try:
                country = self.service.getById(id)
                if country:
                    return self._successResponse(country)
                return self._errorResponse("País no encontrado", 404)
            except Exception as e:
                return self._errorResponse(str(e), 500)

        @self.routes.route('/api/paises/<int:id>/ciudades', methods=['GET'])
        def getCitiesByCountry(id):
            try:
                cities = self.service.getCitiesByCountryId(id)
                if cities:
                    return self._successResponse(cities)
                return self._errorResponse("País no encontrado", 404)
            except Exception as e:
                return self._errorResponse(str(e), 500)

        @self.routes.route('/api/ciudades/<int:cityId>/detalles', methods=['GET'])
        def getCityDetails(cityId):
            try:
                details = self.service.getCityDetails(cityId)
                if details:
                    return self._successResponse(details)
                return self._errorResponse("Ciudad no encontrada", 404)
            except Exception as e:
                return self._errorResponse(str(e), 500)

        @self.routes.route('/api/ciudades/<int:cityId>/hoteles', methods=['GET'])
        def getCityHotels(cityId):
            try:
                hotels = self.service.getCityHotels(cityId)
                if hotels:
                    return self._successResponse(hotels)
                return self._errorResponse("No se encontraron hoteles", 404)
            except Exception as e:
                return self._errorResponse(str(e), 500)

        @self.routes.route('/api/ciudades/<int:cityId>/actividades', methods=['GET'])
        def getCityActivities(cityId):
            try:
                activities = self.service.getCityActivities(cityId)
                if activities:
                    return self._successResponse(activities)
                return self._errorResponse("No se encontraron actividades", 404)
            except Exception as e:
                return self._errorResponse(str(e), 500)

        @self.routes.route('/api/ciudades/<int:cityId>/autos', methods=['GET'])
        def getCityCars(cityId):
            try:
                cars = self.service.getCityCars(cityId)
                if cars:
                    return self._successResponse(cars)
                return self._errorResponse("No se encontraron autos", 404)
            except Exception as e:
                return self._errorResponse(str(e), 500)

        # POST Routes
        @self.routes.route('/api/paises', methods=['POST'])
        def createCountry():
            try:
                data = request.get_json()
                if not data or 'nombre' not in data:
                    return self._errorResponse("Datos inválidos", 400)
                newCountry = self.service.create(data)
                return self._successResponse(newCountry)
            except Exception as e:
                return self._errorResponse(str(e), 400)

        # PUT Routes
        @self.routes.route('/api/paises/<int:id>', methods=['PUT'])
        def updateCountry(id):
            try:
                data = request.get_json()
                updatedCountry = self.service.update(id, data)
                if updatedCountry:
                    return self._successResponse(updatedCountry)
                return self._errorResponse("País no encontrado", 404)
            except Exception as e:
                return self._errorResponse(str(e), 400)

        # DELETE Routes
        @self.routes.route('/api/paises/<int:id>', methods=['DELETE'])
        def deleteCountry(id):
            try:
                result = self.service.delete(id)
                if result:
                    return self._successResponse({'deleted': True})
                return self._errorResponse("País no encontrado", 404)
            except Exception as e:
                return self._errorResponse(str(e), 500)

    def _successResponse(self, data):
        return jsonify({
            'success': True,
            'data': data
        })

    def _errorResponse(self, message, statusCode):
        return jsonify({
            'success': False,
            'error': str(message)
        }), statusCode