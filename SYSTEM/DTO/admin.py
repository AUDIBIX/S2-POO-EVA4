
from datetime import datetime, timedelta
from ..DAO.Api import Api
from ..DAO.crudAdmin import PackageDAO
from ..DTO.Destination import Destination

class AdminDto:
    def __init__(self):
        self.packages = []
        self.package_dao = PackageDAO()

    def assemblePackage(self):
        while True:
            try:
                namePackage = input("Ingrese el nombre del paquete a crear: ").strip()
                if not namePackage:
                    raise ValueError("El nombre del paquete no puede estar vacío.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                descriptionPackage = input("Ingrese la descripción del paquete: ").strip()
                if not descriptionPackage:
                    raise ValueError("La descripción del paquete no puede estar vacía.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                costPackage = input("Ingrese el costo del paquete: ").strip()
                if not costPackage.isdigit() or int(costPackage) <= 0:
                    raise ValueError("El costo del paquete debe ser un número positivo.")
                costPackage = float(costPackage)
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Obtener países
        showCountries = Api.getCountries()
        print("\nPaíses disponibles:")
        for country in showCountries:
            print(f"- {country['name']} ({country['code']})")

        while True:
            try:
                selectCountry = input("\nSeleccione el código de un país: ").strip().upper()
                if not any(country['code'] == selectCountry for country in showCountries):
                    raise ValueError("Código de país inválido. Intente de nuevo.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Obtener ciudades
        try:
            showCities = Api.getCitiesCountries(selectCountry)
            if not showCities:
                print(f"No se encontraron ciudades para el país {selectCountry}.")
                return
        except Exception as e:
            print(f"Error al obtener ciudades: {e}")
            return

        print("\nCiudades disponibles:")
        for city in showCities:
            print(f"- {city}")

        while True:
            try:
                selectCity = input("\nSeleccione una ciudad: ").strip().lower()
                normalized_cities = [city.lower() for city in showCities]  
                if selectCity not in normalized_cities:
                    raise ValueError("Ciudad inválida. Intente de nuevo.")
                selectCity = showCities[normalized_cities.index(selectCity)]  
                break
            except ValueError as e:
                print(f"Error: {e}")

        # Validar fechas
        def get_valid_date(prompt, min_date=None):
            while True:
                try:
                    date_input = input(prompt).strip()
                    date_obj = datetime.strptime(date_input, "%Y-%m-%d")
                    if min_date and date_obj <= min_date:
                        raise ValueError(f"La fecha debe ser posterior a {min_date.strftime('%Y-%m-%d')}.")
                    return date_obj
                except ValueError as e:
                    print(f"Error: {e}. Use el formato YYYY-MM-DD.")

        today = datetime.now()
        start_date = get_valid_date(
            "Ingrese la fecha de inicio del paquete (YYYY-MM-DD): ",
            min_date=today - timedelta(days=1)
        )
        end_date = get_valid_date(
            "Ingrese la fecha de fin del paquete (YYYY-MM-DD): ",
            min_date=start_date
        )

        # Crear objeto Destination usando los datos proporcionados
        selected_destination = Destination(
            name=namePackage,
            description=descriptionPackage,
            type="vacation",
            country=selectCountry,
            city=selectCity,
            cost=costPackage,
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d")
        )

        # Preparar datos del paquete para insertar en la BD
        package_data = {
            "name": namePackage,
            "description": descriptionPackage,
            "country_code": selectCountry,
            "city": selectCity,
            "cost": costPackage,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
        }

        try:
            # Guardar el paquete en la BD
            package_id = self.package_dao.create_package(package_data)

            if package_id:  # Validar que se haya guardado correctamente
                print("\n===============================")
                print("¡Paquete guardado con éxito en la BD!")
                print(f"ID del paquete: {package_id}")
                print("===============================\n")
            else:
                raise Exception("No se pudo guardar el paquete en la BD.")
                
        except Exception as e:
            print(f"Error al guardar el paquete en la BD: {e}")

        # Mostrar el paquete creado en la consola
        print("=" * 40)
        print("\nPaquete creado con éxito:")
        print("=" * 40)
        print(f"Nombre del Paquete: {selected_destination.getName()}")
        print(f"Descripción: {selected_destination.getDescription()}")
        print(f"País: {selectCountry}")
        print(f"Ciudad: {selectCity}")
        print(f"Costo: ${costPackage}")
        print(f"Fecha de Inicio: {start_date.strftime('%Y-%m-%d')}")
        print(f"Fecha de Fin: {end_date.strftime('%Y-%m-%d')}")
        print("Actividades:")
        for activity in selected_destination.getActivities():
            print(f"- {activity}")
        print("Autos Disponibles:")
        for car in selected_destination.getAutos():
            print(f"- {car}")
        print("Hoteles Disponibles:")
        for hotel in selected_destination.getHoteles():
            print(f"- {hotel}")
        print("=" * 40)

    def showPackages(self):
    ##mostrar paquetes
        try:
            packages = self.package_dao.get_all_packages()

            if not packages:
                print("No hay paquetes creados aún.")
                return

            print("=" * 40)
            print("Lista de Paquetes Creados:")
            for package in packages:
                print(f"ID: {package['PackageID']}")
                print(f"Nombre: {package['Name']}")
                print(f"Descripción: {package['Description']}")
                print(f"País: {package['CountryCode']}")
                print(f"Ciudad: {package['City']}")
                print(f"Costo: ${package['Cost']}")
                print(f"Fecha de Inicio: {package['StartDate']}")
                print(f"Fecha de Fin: {package['EndDate']}")
                print(f"Creado el: {package['CreatedAt']}")
                print("-" * 40)

        except Exception as e:
            print(f"Error al mostrar paquetes: {e}")

    def deletePackage(self):
        while True:
            try:
                package_id = input("Ingrese el ID del paquete a eliminar: ").strip()

                if not package_id.isdigit():
                    print("El ID debe ser un numero válido.")
                    continue  

                package_id = int(package_id)

                # Verificar si el paquete existe
                if not self.package_dao.package_exists(package_id):
                    print(f"No se encontró un paquete con ID {package_id}.")
                    continue  

                while True:
                    confirmation = input(f"¿Está seguro de que desea eliminar el paquete con ID {package_id}? (si/no): ").strip().lower()
                    
                    if confirmation == 'si':
                        # Eliminar paquete
                        result = self.package_dao.delete_package(package_id)

                        if result:
                            print(f"Paquete con ID {package_id} eliminado con exito.")
                        else:
                            print(f"No se pudo eliminar el paquete con ID {package_id}.")
                        break  # Salir del bucle después de eliminar

                    elif confirmation == 'no':
                        print("Operación cancelada.")
                        break  # Salir si la respuesta es "no"
                    else:
                        print("Por favor, ingrese 'si' o 'no' para confirmar la eliminacion.")
                
                break  # Salir después de intentar eliminar o cancelar

            except Exception as e:
                print(f"Error al eliminar paquete: {e}")
