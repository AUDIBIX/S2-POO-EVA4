import requests
GEONAMES_USERNAME = 'josiastorres20'
GEONAMES_API_URL = 'http://api.geonames.org'

class Api:
    def _init_(self):
        pass

    def getCountries():
        url = f"{GEONAMES_API_URL}/countryInfoJSON"
        params = {"username": GEONAMES_USERNAME}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            countries = response.json().get("geonames", [])
            return [
                {"name": country["countryName"], "code": country["countryCode"]}
                for country in countries
            ]
        else:
            raise Exception("Error al obtener los paises")
        
        
    def getCitiesCountries(countryCode):
        url = f"{GEONAMES_API_URL}/searchJSON"
        params = {
            "country": countryCode,
            "featureClass": "P", 
            "maxRows": 10, 
            "username": GEONAMES_USERNAME
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            cities = response.json().get("geonames", [])
            return [city["name"] for city in cities]
        else:
            raise Exception(f"Error al obtener las ciudades del pais {countryCode}")
