from SYSTEM.Utilities.Utilities import *

class Destination:
    def __init__(self, name, description, type, country, city, cost, start_date, end_date, id=None, activities=[], cars:list=[{}], hotels:list=[{}]):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__type = type
        self.__country = country
        self.__city = city
        self.__activities = activities
        self.__cost = cost
        self.__start_date = start_date
        self.__end_date = end_date
        self.__cars = cars
        self.__hotels = hotels
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getType(self):
        return self.__type
    
    def getCountry(self):
        return self.__country
    
    def getCity(self):
        return self.__city
    
    def getCost(self):
        return self.__cost
    
    def getStartDate(self):
        return self.__start_date
    
    def getEndDate(self):
        return self.__end_date
    
    def getActivities(self):
        return self.__activities

    def getAutos(self):
        return self.__cars
    
    def getHoteles(self):
        return self.__hotels
    
    def setId(self, id):
        self.__id = id
    
    def setName(self, name):
        self.__name = name
        
    def setDescription(self, description):
        self.__description = description
        
    def setType(self, type):
        self.__type = type
        
    def setCountry(self, country):
        self.__country = country
        
    def setCity(self, city):
        self.__city = city
    
    def setActivities(self, activities=[]):
        self.__activities = activities
        
    def setAutos(self, cars={}):
        self.__cars = cars
        
    def setHoteles(self, hotels={}):
        self.__hotels = hotels
        
    def setCost(self, cost):
        self.__cost = cost
        
    def setStartDate(self, start_date):
        self.__start_date = start_date
        
    def setEndDate(self, end_date):
        self.__end_date = end_date
    
    def addActivity(self, activity):
        self.__activities.append(activity)
        
    def __str__(self):
        txt = f"\nNombre: {self.__name}\n"
        txt += f"Descripcion: {self.__description}\n"
        txt += f"Tipo: {self.__type}\n"
        txt += f"Pais: {self.__country}\n"
        txt += f"Ciudad: {self.__city}\n"
        txt += f"Costo: {self.__cost}\n"
        txt += f"Fecha de inicio: {self.__start_date}\n"
        txt += f"Fecha de fin: {self.__end_date}\n"
        txt += "Actividades: \n"
        for activity in self.__activities:
            txt += f" -{activity}\n"
        if cars :=self.__cars:
            txt += "Autos: \n"
            for car in cars:
                txt += f" -{car}\n"
        elif hotels := self.__hotels:
            txt += "Hoteles: \n"
            for hotel in hotels:
                txt += f" > {hotel["nombre"]} <\n"
                txt += f" -Precio por noche: ${hotel['precio_noche']}\n"
                txt += f" -Cantidad de estrellas: ✰{hotel['estrellas']}\n"
        return txt
    
    
    
    def edit(self):
        print("Que desea modificar?")
        print_options(["Nombre", "Descripcion", "Pais", "Ciudad", "Tipo", "Costo", "Fecha de inicio", "Fecha de fin"])
        opcion = input("Opcion: ")
        if opcion == "1":
            self.setName(input("Ingrese el nuevo nombre: "))
        elif opcion == "2":
            self.setDescription(input("Ingrese la nueva descripcion: "))
        elif opcion == "3":
            self.setCountry(input("Ingrese el nuevo pais: "))
        elif opcion == "4":
            self.setCity(input("Ingrese la nueva ciudad: "))
        elif opcion == "5":
            self.setType(input("Ingrese el nuevo tipo: "))
        elif opcion == "6":
            self.setCost(input("Ingrese el nuevo costo: "))
        elif opcion == "7":
            self.setStartDate(input("Ingrese la nueva fecha de inicio: "))
        elif opcion == "8":
            self.setEndDate(input("Ingrese la nueva fecha de fin: "))
        else:
            print("Opcion no valida")
        return self