import mysql.connector
from DAO.DB import Db
from DTO.userDto import UserDto
class UsuarioDao:
    def __init__(self):
        self.db = Db()
 
    def create(self, user: UserDto):
        try:
            connection = self.db.getConnection()
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO users (NAME, LAST_NAME, RUT, MAIL, USER_TYPE) 
                           VALUES (%s, %s, %s, %s, %s)""", (user.getName(), user.getLastName(),user.getRut(), user.getMail(), user.getTypeUser()))
            connection.commit()
            user.getUserId = cursor.lastrowid
            cursor.close()
            connection.close()
            return user
        except mysql.connector.Error as e:
            print(f"Error al crear el usuario: {str(e)}")
            return None

        




