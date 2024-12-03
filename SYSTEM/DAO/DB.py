import mysql.connector
import json, os
from mysql.connector import Error

# usar un instance de java con db corte singleton para que solo se conecte una vez
class Db:
    __instance = None 
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, configDb= "SYSTEM/DAO/configDb.json"):
        if not hasattr(self, "__initialized"):
            self.__configDb = configDb
            self.__connection = None
            self.__initialized = True # pa saber que se inicio

    def getConnection(self):
        if self.__connection is None or not self.__connection.is_connected():
            self.connect()
        return self.__connection
    def loadConfig(self):  
        try:
            with open(self.__configDb, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception("No se encuentra el archivo de configuracion para base de datos")
        except json.JSONDecodeError:
            raise Exception("El archivo de configuracion para base de datos no es valido")
        
    def connect(self):
        try:
            config = self.loadConfig()
            self.__connection = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"]
            )
            if not self.__connection.is_connected():
                raise Exception("No se pudo conectar con la base de datos")
        except Error as e:
            raise Exception(f"Error al conectar con MySQL: {str(e)}")
    def close(self):
        
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()
            self.__connection = None