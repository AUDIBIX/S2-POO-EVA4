from SYSTEM.Utilities.Utilities import *

class Destination:
    def __init__(self, name, description, type, country, city, cost, start_date, end_date, id=None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__type = type
        self.__country = country
        self.__city = city
        self.__cost = cost
        self.__start_date = start_date
        self.__end_date = end_date
    
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
        
    def setCost(self, cost):
        self.__cost = cost
        
    def setStartDate(self, start_date):
        self.__start_date = start_date
        
    def setEndDate(self, end_date):
        self.__end_date = end_date
    
    def __str__(self):
        txt = f"Nombre: {self.__name}"
        txt += f"\nDescripcion: {self.__description}"
        txt += f"\nPais: {self.__country}"
        txt += f"\nCiudad: {self.__city}"
        txt += f"\nTipo: {self.__type}"
        txt += f"\nCosto: {self.__cost}"
        txt += f"\nFecha de inicio: {self.__start_date}"
        txt += f"\nFecha de fin: {self.__end_date}"
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