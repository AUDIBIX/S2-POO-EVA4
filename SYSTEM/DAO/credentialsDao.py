import mysql.connector
from ..DAO.DB import Db
from typing import Optional
class CredentialsDao:
    def __init__(self):
        self.db = Db()

    def create(self, userId: Optional[int], username: Optional[str], password: Optional[str]):
        try:
            connection = self.db.getConnection()
            cursor = connection.cursor()
            query = """
            INSERT INTO CREDENTIALS (USER_ID, USERNAME, PASSWORD)
            VALUES (%s, %s, %s)
            """

            cursor.execute(query, (userId, username, password))
            connection.commit()

            cursor.close()
            connection.close()

            return True
        except mysql.connector.Error as e:
            print(f"Error al crear usuario o contrasena: {str(e)}")
            return False