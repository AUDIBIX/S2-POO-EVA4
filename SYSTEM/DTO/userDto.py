from typing import Optional
from ..Utilities.Utilities import *
class UserDto:
    def __init__(self, userId: int, name: Optional[str] = None, lastName: Optional[str] = None,                 #java util.Optional indica que un atributo es opcional 
                 rut: Optional[str] = None, mail: Optional[str] = None, typeUser: Optional[str] = 'CLIENTE' ):  #para entender mas los valores a futuro 
        self.__userId = userId
        self.__name = name
        self.__lastName = lastName
        self.__rut = rut
        self.__mail = mail
        self.__typeUser = typeUser

    def getUserId(self):
        return self.__userId
    def getName(self):
        return self.__name
    def getLastName(self):
        return self.__lastName
    def getRut(self):
        return self.__rut
    def getMail(self):
        return self.__mail
    def getTypeUser(self):
        return self.__typeUser
    
    def setUserId(self, userId):
        self.__userId = userId
    def setName(self, name):
        self.__name = name
    def setLastName(self, lastName):
        self.__lastName = lastName
    def setRut(self, rut):
        self.__rut = rut
    def setMail(self, mail):
        self.__mail = mail
    def setTypeUser(self, typeUser):
        self.__typeUser = typeUser

    def __str__(self):
        txt = f"Nombre: {self.__name} {self.__lastName}\n"
        txt += f"Rut: {self.__rut}\n"
        txt += f"Mail: {self.__mail}\n"
        txt += f"Eres: {self.__typeUser}\n"
        return txt
