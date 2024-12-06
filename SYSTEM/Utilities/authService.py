from ..Utilities.Utilities import *
from ..DAO.userDao import UserDao
from ..DAO.credentialsDao import CredentialsDao
from ..DTO.userDto import UserDto

class AuthService:
    def __init__(self):
        self.__userDao = UserDao()
        self.__credentialsDao = CredentialsDao()

    def signUp(self):
        try:
            name = valid_input(
                "Ingrese su nombre: ", 
                "Nombre no valido. Intente de nuevo.", 
                str, 
                lambda x: bool(validateName(x))
            )
            
            lastName = valid_input(
                "Ingrese su apellido: ", 
                "Apellido no valido. Intente de nuevo.", 
                str, 
                lambda x: bool(validateName(x))
            )
            while True:
                rut = valid_input(
                    "Ingrese su RUT (formato XXXXXXXX-X): ", 
                    "RUT no valido. Intente de nuevo.", 
                    str, 
                    lambda x: bool(validateRut(x))
                )
                if not self.__userDao.findDuplicate("rut", rut, "USER"):
                    break
                print("RUT ya registrado")
                   
                
            while True:
                mail = valid_input(
                    "Ingrese su correo: ", 
                    "Correo electrónico no valido. Intente de nuevo.", 
                    str, 
                    lambda x: bool(validateEmail(x))
                )
                if not self.__userDao.findDuplicate("mail", mail, "USER"):
                    break
                print("Correo ya registrado")
                
            while True:
                username = valid_input(
                    "Ingrese su nombre de usuario: ", 
                    "Nombre de usuario no valido. Intente de nuevo.", 
                    str, 
                    lambda x: bool(validateUsername(x))
                )
                if not self.__userDao.findDuplicate("username", username, "CREDENTIALS"):
                    break
                print("Nombre de usuario ya registrado")
                    
            plainPassword = valid_input(
                "Ingrese su contraseña: ", 
                "Contraseña no valida. Intente de nuevo.", 
                str, 
                lambda x: bool(validatePassword(x))
            )

            hashedPassword = hashPassword(plainPassword)

            user = UserDto(0, name, lastName, rut, mail, typeUser = 'CLIENTE')
            createdUser = self.__userDao.create(user)

            if createdUser:
                self.__credentialsDao.create(
                    userId=createdUser.getUserId(),
                    username=username,
                    password=hashedPassword
                )
                print("Usuario registrado")
                return True
            else:
                print("Error al registrar el usuario")
                return False
        except Exception as e:
            print(f"Error durante el registro: {e}")
            return False
        
    def login(self):
        try:
            username = valid_input(
                "Ingrese su nombre de usuario: ", 
                "Nombre de usuario no válido. Intente de nuevo.", 
                str, 
                lambda x: bool(validateUsername(x))
            )
            plainPassword = input("Ingrese su contraseña: ")

            credentials = self.__userDao.findDuplicate("username", username, "CREDENTIALS")
            if not credentials:
                print("Usuario no encontrado.")
                return False
            if checkPassword(plainPassword, credentials["PASSWORD"]):
                user = self.__userDao.read(credentials["USER_ID"])
                if user is not None:
                    print(f"Bienvenido {user.getName()} {user.getLastName()}")
                    return user
                else:
                    print("Usuario no registrado")
                return False
            
            else:
                print("Contraseña incorrecta.")
                return False
        except Exception as e:
            print(f"Error durante el inicio de sesion: {e}")
            return False
        