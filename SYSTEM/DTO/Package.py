from SYSTEM.Utilities.Utilities import *
import datetime

class Package:
    def __init__(self, id, name, description, cost):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__destinations = []
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
            for destination in self.__destinations:
                start_date = destination.getStartDate()
                if isinstance(start_date, datetime.datetime):
                    if start_date < fecha or fecha is None:
                        fecha = start_date        
        return fecha
    
    def setEndDate(self):
        fecha = None
            
        if self.__destinations is not None:
            for destination in self.__destinations:
                end_date = destination.getEndDate()
                if isinstance(end_date, datetime.datetime):
                    if end_date > fecha or fecha is None:
                        fecha = end_date        
        return fecha
    
    def addDestination(self, destination):
        self.__destinations.append(destination)
    
    def removeDestination(self, destination):
        self.__destinations.remove(destination)

    def __str__(self):
        txt = f"Nombre: {self.__name}"
        txt += f"\nDescripcion: {self.__description}"
        txt += f"\nCantidad de destinos: {len(self.__destinations)}"
        txt += f"\nCosto: {self.__cost}"
        txt += f"\nFecha de inicio: {self.__start_date}"
        txt += f"\nFecha de fin: {self.__end_date}"
        return txt
    
    def edit(self):
        print("Que desea modificar?")
        print_options(["Nombre", "Descripcion", "Costo"])
        opcion = input("Opcion: ")
        if opcion == "1":
            self.setName(input("Ingrese el nuevo nombre: "))
        elif opcion == "2":
            self.setDescription(input("Ingrese la nueva descripcion: "))
        elif opcion == "3":
            self.setCost(input("Ingrese el nuevo costo: "))
        else:
            print("Opcion no valida")