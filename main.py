from SYSTEM.DTO.Package import *
from SYSTEM.DTO.Destination import *
from SYSTEM.Utilities.authService import AuthService

class Main:
    @staticmethod
    def show_main_menu():
        options = ["Ver paquetes", "Iniciar sesión/Registrarse"]
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        selection = int(input("Seleccione una opción: "))
        if selection == 1:
            Main.view_packages()
        elif selection == 2:
            Main.auth_menu()

    @staticmethod
    def view_packages():
        package = Package(None, None, None, None)
        package.generateDestination()
        print(package) 

    @staticmethod
    def auth_menu():
        options = ["Registrarse", "Iniciar sesión"]
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        selection = int(input("Seleccione una opción: "))
        auth_service = AuthService()  # Crear una instancia de AuthService
        if selection == 1:
            auth_service.signUp()  # Usar la instancia para llamar al método
        elif selection == 2:
            auth_service.login()  # Usar la instancia para llamar al método

if __name__ == "__main__":
    Main.show_main_menu()
