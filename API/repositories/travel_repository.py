from typing import List, Optional, Dict
from mysql.connector import Error
import logging

logger = logging.getLogger(__name__)

class TravelRepository:
    def __init__(self, db_connection):
        self.connection = db_connection
        
    def getAll(self) -> List[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT c.id, c.name as nombre, 
                       GROUP_CONCAT(DISTINCT ci.id) as city_ids,
                       GROUP_CONCAT(DISTINCT ci.name) as city_names
                FROM countries c
                LEFT JOIN cities ci ON c.id = ci.country_id
                GROUP BY c.id
            """)
            countries = cursor.fetchall()
            
            # Formatear los resultados
            formatted_countries = []
            for country in countries:
                city_ids = country['city_ids'].split(',') if country['city_ids'] else []
                city_names = country['city_names'].split(',') if country['city_names'] else []
                
                formatted_countries.append({
                    'id': country['id'],
                    'nombre': country['nombre'],
                    'ciudades': [
                        {'id': int(cid), 'nombre': cname}
                        for cid, cname in zip(city_ids, city_names)
                    ]
                })
            
            return formatted_countries
            
        except Error as e:
            logger.error(f"Error al obtener países: {str(e)}")
            raise
        finally:
            cursor.close()

    def getById(self, id: int) -> Optional[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT c.id, c.name as nombre,
                       ci.id as city_id, ci.name as city_name
                FROM countries c
                LEFT JOIN cities ci ON c.id = ci.country_id
                WHERE c.id = %s
            """, (id,))
            
            rows = cursor.fetchall()
            if not rows:
                return None
                
            country = {
                'id': rows[0]['id'],
                'nombre': rows[0]['nombre'],
                'ciudades': []
            }
            
            for row in rows:
                if row['city_id']:
                    country['ciudades'].append({
                        'id': row['city_id'],
                        'nombre': row['city_name']
                    })
            
            return country
            
        except Error as e:
            logger.error(f"Error al obtener país por ID: {str(e)}")
            raise
        finally:
            cursor.close()

    def create(self, country_data: dict) -> dict:
        try:
            cursor = self.connection.cursor()
            
            # Insertar país
            cursor.execute(
                "INSERT INTO countries (name) VALUES (%s)",
                (country_data['nombre'],)
            )
            country_id = cursor.lastrowid
            
            # Insertar ciudades
            for city in country_data.get('ciudades', []):
                cursor.execute(
                    "INSERT INTO cities (name, country_id) VALUES (%s, %s)",
                    (city['nombre'], country_id)
                )
            
            self.connection.commit()
            return self.getById(country_id)
            
        except Error as e:
            self.connection.rollback()
            logger.error(f"Error al crear país: {str(e)}")
            raise
        finally:
            cursor.close()

    def getCityDetails(self, cityId: int) -> Optional[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT c.id, c.name,
                       h.id as hotel_id, h.name as hotel_name, h.stars, h.price_per_night,
                       a.id as activity_id, a.name as activity_name, a.description,
                       cr.id as car_id, cr.brand, cr.model, cr.type, cr.price_per_day
                FROM cities c
                LEFT JOIN hotels h ON c.id = h.city_id
                LEFT JOIN activities a ON c.id = a.city_id
                LEFT JOIN cars cr ON c.id = cr.city_id
                WHERE c.id = %s
            """, (cityId,))
            
            results = cursor.fetchall()
            if not results:
                return None
                
            city_details = {
                'id': results[0]['id'],
                'name': results[0]['name'],
                'hotels': [],
                'activities': [],
                'cars': []
            }
            
            processed = {'hotels': set(), 'activities': set(), 'cars': set()}
            
            for row in results:
                if row['hotel_id'] and row['hotel_id'] not in processed['hotels']:
                    city_details['hotels'].append({
                        'id': row['hotel_id'],
                        'name': row['hotel_name'],
                        'stars': row['stars'],
                        'price_per_night': row['price_per_night']
                    })
                    processed['hotels'].add(row['hotel_id'])
                
                if row['activity_id'] and row['activity_id'] not in processed['activities']:
                    city_details['activities'].append({
                        'id': row['activity_id'],
                        'name': row['activity_name'],
                        'description': row['description']
                    })
                    processed['activities'].add(row['activity_id'])
                
                if row['car_id'] and row['car_id'] not in processed['cars']:
                    city_details['cars'].append({
                        'id': row['car_id'],
                        'brand': row['brand'],
                        'model': row['model'],
                        'type': row['type'],
                        'price_per_day': row['price_per_day']
                    })
                    processed['cars'].add(row['car_id'])
            
            return city_details
            
        except Error as e:
            logger.error(f"Error al obtener detalles de la ciudad: {str(e)}")
            raise
        finally:
            cursor.close()

    def getCityHotels(self, cityId: int) -> List[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT * FROM hotels WHERE city_id = %s
            """, (cityId,))
            return cursor.fetchall()
        except Error as e:
            logger.error(f"Error al obtener hoteles: {str(e)}")
            raise
        finally:
            cursor.close()

    def getCityActivities(self, cityId: int) -> List[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT * FROM activities WHERE city_id = %s
            """, (cityId,))
            return cursor.fetchall()
        except Error as e:
            logger.error(f"Error al obtener actividades: {str(e)}")
            raise
        finally:
            cursor.close()

    def getCityCars(self, cityId: int) -> List[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT * FROM cars WHERE city_id = %s
            """, (cityId,))
            return cursor.fetchall()
        except Error as e:
            logger.error(f"Error al obtener autos: {str(e)}")
            raise
        finally:
            cursor.close()

    def getAllCities(self) -> List[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT c.id, c.name as nombre, co.name as pais
                FROM cities c
                JOIN countries co ON c.country_id = co.id
            """)
            return cursor.fetchall()
        except Error as e:
            logger.error(f"Error al obtener ciudades: {str(e)}")
            raise
        finally:
            cursor.close()

    def getCityById(self, cityId: int) -> Optional[Dict]:
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT c.id, c.name as nombre, 
                       co.id as pais_id, co.name as pais,
                       COUNT(DISTINCT h.id) as total_hoteles,
                       COUNT(DISTINCT a.id) as total_actividades,
                       COUNT(DISTINCT ca.id) as total_autos
                FROM cities c
                JOIN countries co ON c.country_id = co.id
                LEFT JOIN hotels h ON c.id = h.city_id
                LEFT JOIN activities a ON c.id = a.city_id
                LEFT JOIN cars ca ON c.id = ca.city_id
                WHERE c.id = %s
                GROUP BY c.id
            """, (cityId,))
            
            result = cursor.fetchone()
            if not result:
                return None
            
            return {
                'id': result['id'],
                'nombre': result['nombre'],
                'pais': {
                    'id': result['pais_id'],
                    'nombre': result['pais']
                },
                'resumen': {
                    'hoteles': result['total_hoteles'],
                    'actividades': result['total_actividades'],
                    'autos': result['total_autos']
                }
            }
        except Error as e:
            logger.error(f"Error al obtener ciudad por ID: {str(e)}")
            raise
        finally:
            cursor.close()