from SYSTEM.Utilities.Utilities import *
from SYSTEM.DAO.Api import Api
import datetime

class Package:
    def __init__(self, name, description, cost, id=None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__destinations = {}
        self.__start_date = self.setStartDate()
        self.__end_date = self.setEndDate()
        self.__cost = cost

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getDestinations(self):
        return self.__destinations

    def getStartDate(self):
        return self.__start_date

    def getEndDate(self):
        return self.__end_date

    def getCost(self):
        return self.__cost

    def setName(self, name):
        self.__name = name

    def setDescription(self, description):
        self.__description = description

    def setCost(self, cost):
        self.__cost = cost
    
    
    def setStartDate(self):
        fecha = None
            
        if self.__destinations is not None:
            for destination in self.__destinations.values():
                start_date = destination.getStartDate()
                if isinstance(start_date, datetime.datetime):
                    if start_date < fecha or fecha is None:
                        fecha = start_date
        return fecha
    
    
    def setEndDate(self):
        fecha = None
            
        if self.__destinations is not None:
            for destination in self.__destinations.values():
                end_date = destination.getEndDate()
                if isinstance(end_date, datetime.datetime):
                    if end_date > fecha or fecha is None:
                        fecha = end_date        
        return fecha
    
    
    def addDestination(self, destination):
        if destination.getId() is None:
            destination.setId(1)
            
        destinationIds = []
        for dest in self.__destinations.values():
            destinationIds.append(dest.getId())
            
        if destination.getId() in destinationIds:
            destination.setId(destination.getId() + 1)
        
        self.__destinations[destination.getId()] = destination
    
    def removeDestination(self, destination):
        self.__destinations.pop(destination.getId())

    def __str__(self):
        txt = f"Nombre: {self.__name}"
        txt += f"\nDescripcion: {self.__description}"
        txt += f"\nCantidad de destinos: {len(self.__destinations.values())}"
        txt += f"\nCosto: {self.__cost}"
        txt += f"\nFecha de inicio: {self.__start_date}"
        txt += f"\nFecha de fin: {self.__end_date}"
        return txt
    
    
    def edit(self):
        while True:
            print("Que desea modificar? 0 para salir")
            print_options(["Nombre", "Descripcion", "Costo", "Destinos"])
            opcion = input("Opcion: ")
            
            if opcion == "1":
                self.setName(input("Ingrese el nuevo nombre: "))
                
            elif opcion == "2":
                self.setDescription(input("Ingrese la nueva descripcion: "))
                
            elif opcion == "3":
                self.setCost(input("Ingrese el nuevo costo: "))
                
            elif opcion == "4":
                print("Que desea hacer con los destinos?")
                print_options(["Agregar", "Eliminar"])
                opcion = input("Opcion: ")
                
                if opcion == "1":
                    self.generateDestination()
                
                elif opcion == "2":
                    if not self.__destinations:
                        print("No hay destinos para eliminar")
                        break
                    
                    for destination in self.__destinations.values():
                        print(f"ID: {destination.getId()} - Nombre: {destination.getName()}")
                    id = input("Ingrese el ID del destino a eliminar: ")
                    
                    if id in self.__destinations:
                        self.removeDestination(self.__destinations[id])
                    else:
                        print("ID no valido")
                else:
                    print("Opcion no valida")
                
            elif opcion == "0":
                return
            else:
                print("Opcion no valida")
    
    def generateDestination(self):
        from SYSTEM.DTO.Destination import Destination
        import random
        while True:
            try:
                response = Api.getCountries()
                if not response.get("success", False):
                    print("No se pudieron obtener los paises")
                    return
                countries = [(country['id'], country['nombre']) for country in response['data']]
                for index, (countryId ,countryName )in enumerate(countries, start=1):
                    print(f"{index}. {countryName}")
                selectCountries = int(input("Seleccione el pais: ")) - 1
                selectedCountry = countries[selectCountries] #elejimos el elemento de lista segun la eleccion
                countryId = selectedCountry[0] # futuros usos extraemos el id


                cityResponse = Api.getCitiesCountries(countryId)
                if not cityResponse.get("success", False):
                    print("No se pudieron obtener las ciudades")
                    return

                cities = [(city['id'], city['nombre']) for city in cityResponse['data']]
                for index, (cityId, cityName) in enumerate(cities, start=1):
                    print(f"{index}. {cityName}")

                selectCities = int(input("Seleccione la ciudad: ")) - 1
                selectedCity = cities[selectCities]
                cityId = selectedCity[0]


                dateStart = input("Ingrese la fecha de ida: ")
                dateEnd = input("Ingrese la fecha de regreso: ")


                print_options(["Vuelo + Hotel", "Vuelo + Auto"])
                selectType = valid_input("Seleccione el tipo de paquete: ", "Opcion no valida", int, lambda x: x in [1, 2]) - 1


                destinations = []
                numberDestinations = random.randint(2, 5)


                for _ in range(numberDestinations):
                    activitiesResponse = Api.getActivitiesCities(cityId)
                    if not activitiesResponse.get("success", False):
                        print("No se pudieron obtener las actividades")
                        return

                    activities = activitiesResponse['data']
                    selectedActivities = random.sample(activities, min(3, len(activities)))
                    destination = {
                        "fecha_inicio": dateStart,
                        "fecha_fin": dateEnd,
                        "actividades": [activity['name'] for activity in selectedActivities]}

                    if selectType == 0:
                        hotelsResponse = Api.getHotelsCities(cityId)
                        if not hotelsResponse.get("success", False):
                            print("No se pudieron obtener los hoteles")
                            return
                        hotels = hotelsResponse['data']
                        selected_hotels = random.sample(hotels, min(1, len(hotels)))
                        destination["hoteles"] = [{"nombre": hotel["name"], 
                                            "precio_noche": hotel["price_per_night"], 
                                            "estrellas": hotel["stars"]} for hotel in selected_hotels]
                        
                    elif selectType == 1:
                        carsResponse = Api.getCarsCities(cityId)
                        if not carsResponse.get("success", False):
                            print("No se pudieron obtener los autos")
                            return
                        cars = carsResponse['data']
                        selected_cars = random.sample(cars, min(1, len(cars)))
                        destination["autos"] = [{"nombre": car["model"], 
                                            "marca": car["brand"], 
                                            "precio_dia": car["price_per_day"]} for car in selected_cars]
                    destinations.append(destination)
                
                destination_objects = []
                for index, dst in enumerate(destinations, start=1):
                    dst['nombre'] = f"Destino {index}"
                    destination_objects.append(Destination(dst['nombre'], "", 
                                                        "Vuelo + Hotel" if selectType == 0 else "Vuelo + Auto",
                                                        selectedCountry, selectedCity, 0,
                                                        dst["fecha_inicio"], dst["fecha_fin"],
                                                        activities=dst["actividades"],
                                                        cars=dst["autos"] if "autos" in dst else {},
                                                        hotels=dst["hoteles"] if "hoteles" in dst else {}))
                    
                    for destination in destination_objects:
                        print(destination)
                    
                    destination_names = [destination.getName() for destination in destination_objects]
                    
                if valid_input("Desea reservar un paquete? (s/n): ", "Opcion no valida", str, lambda x: x.lower() in ['s', 'n']) == "s":
                    print_options(destination_names)
                    selectedDestination = valid_input("Seleccione el destino: ", "Opcion no valida", int, lambda x: x in range(1, len(destination_names) + 1))
                    selectedDestination = destination_objects[selectedDestination - 1]
                    print(selectedDestination)
                    if valid_input("Confirme su seleccion para reservar el paquete (s/n): ", "Opcion no valida", str, lambda x: x.lower().strip() in ['s', 'n']):
                        self.addDestination(selectedDestination)
                        print("Paquete reservado con exito")
                    
                continuar = valid_input("Desea revisar otras opciones? (s/n): ", "Opcion no valida", str, lambda x: x.lower().strip() in ['s', 'n'])
                if continuar == "n":
                    break
            except ValueError as ve:
                print(f"Error de entrada: {ve}")
            except Exception as e:
                print(f"Error inesperado: {e}")