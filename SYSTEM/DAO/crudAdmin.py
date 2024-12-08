from ..DAO.DB import Db

class PackageDAO:
    def __init__(self):
        self.db = Db()

    def create_package(self, package_data):
        ##crear paquete
        query = """
        INSERT INTO PACKAGE_ADMIN 
        (Name, Description, CountryCode, City, Cost, StartDate, EndDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            package_data['name'],
            package_data['description'],
            package_data['country_code'],
            package_data['city'],
            package_data['cost'],
            package_data['start_date'],
            package_data['end_date']
        )
        conn = self.db.getConnection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid
    
    def get_all_packages(self):
        ##obtener todos los paquetes
        try:
            connection = self.db.getConnection()
            cursor = connection.cursor(dictionary=True)
            
            sql = "SELECT * FROM PACKAGE_ADMIN ORDER BY CreatedAt DESC"
            cursor.execute(sql)
            packages = cursor.fetchall()
            return packages

        except Exception as e:
            raise Exception(f"Error al obtener paquetes: {e}")

    def package_exists(self, package_id):
        ##verificar si el paquete existe
        try:
            connection = self.db.getConnection()
            cursor = connection.cursor()
            
            cursor.execute("SELECT 1 FROM PACKAGE_ADMIN WHERE PackageID = %s", (package_id,))
            result = cursor.fetchone()
            
            return result is not None

        except Exception as e:
            raise Exception(f"Error al verificar si el paquete existe: {e}")

    def delete_package(self, package_id):
        ##eliminar paquete
        try:
            connection = self.db.getConnection()
            cursor = connection.cursor()

            # Eliminar el paquete
            cursor.execute("DELETE FROM PACKAGE_ADMIN WHERE PackageID = %s", (package_id,))
            connection.commit()

            if cursor.rowcount > 0:
                return True
            else:
                return False

        except Exception as e:
            raise Exception(f"Error al eliminar paquete: {e}")
        
    def get_package_by_id(self, package_id):
        ##obtener paquete por id
        query = "SELECT * FROM PACKAGE_ADMIN WHERE PackageID = %s"
        conn = self.db.getConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (package_id,))
        return cursor.fetchone()

