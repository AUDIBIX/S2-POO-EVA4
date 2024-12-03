import requests 

API_URL = 'http://127.0.0.1:5000/'

class Api:
    def _init_(self):
        pass

    def getCountries():
        url = f"{API_URL}/api/paises"
        response = requests.get (url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener los paises")
        
    def getCountryId(countryId):
        url = f"{API_URL}/api/paises/{countryId}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener los paises")
        
    def getCitiesCountries(countryId):
        url = f"{API_URL}/api/paises/{countryId}/ciudades"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener las ciudades")
        
    def getActivitiesCities(cityId):
        url = f"{API_URL}/api/ciudades/{cityId}/actividades"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener las actividades")
        
    def getCarsCities(cityId):
        url = f"{API_URL}/api/ciudades/{cityId}/autos"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener los autos")
        
    def getHotelsCities(cityId):
        url = f"{API_URL}/api/ciudades/{cityId}/hoteles"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener los hoteles")