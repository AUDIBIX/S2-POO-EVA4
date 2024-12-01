from typing import List, Dict, Optional
from repositories.travel_repository import TravelRepository
import random

class TravelService:
    def __init__(self, repository: TravelRepository):
        self.repository = repository

    def getAll(self) -> List[Dict]:
        return self.repository.getAll()

    def getById(self, id: int) -> Optional[Dict]:
        return self.repository.getById(id)

    def getCitiesByCountryId(self, countryId: int) -> List[Dict]:
        country = self.repository.getById(countryId)
        return country['ciudades'] if country else []

    def getCityDetails(self, cityId: int) -> Optional[Dict]:
        return self.repository.getCityDetails(cityId)

    def getCityHotels(self, cityId: int) -> List[Dict]:
        return self.repository.getCityHotels(cityId)

    def getCityActivities(self, cityId: int) -> List[Dict]:
        return self.repository.getCityActivities(cityId)

    def getCityCars(self, cityId: int) -> List[Dict]:
        return self.repository.getCityCars(cityId)

    def create(self, data: Dict) -> Dict:
        return self.repository.create(data)

    def generarPaquetes(self, paisId, ciudadId, fechaIda, fechaRegreso, tipoPaquete):
        try:
            # Obtener detalles de la ciudad
            ciudad = self.repository.getCityById(ciudadId)
            if not ciudad:
                raise ValueError("Ciudad no encontrada")

            # Obtener actividades (seleccionar 3-5 aleatorias)
            actividades = self.repository.getCityActivities(ciudadId)
            actividades_seleccionadas = random.sample(actividades, min(5, len(actividades)))

            # Obtener opciones según el tipo de paquete
            if tipoPaquete == 'vuelo+hotel':
                opciones = self.repository.getCityHotels(ciudadId)
            else:
                opciones = self.repository.getCityCars(ciudadId)

            # Seleccionar opciones aleatorias (2-10)
            opciones_seleccionadas = random.sample(
                opciones, 
                min(10, max(2, len(opciones)))
            )

            return [{
                'destino': f"{ciudad['pais']['nombre']} - {ciudad['nombre']}",
                'fechaIda': fechaIda,
                'fechaRegreso': fechaRegreso,
                'actividades': actividades_seleccionadas,
                'tipo': tipoPaquete,
                'opciones': opciones_seleccionadas
            }]
        except Exception as e:
            raise Exception(f"Error al generar paquetes: {str(e)}")