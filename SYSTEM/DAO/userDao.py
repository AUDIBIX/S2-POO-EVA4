import mysql.connector
from typing import Optional
from ..DAO.DB import Db
from ..DTO.userDto import UserDto
class UserDao:
    def __init__(self):
        self.__db = Db()
 
    def findDuplicate(self, column: Optional[str], value: Optional[str], table: Optional[str]):
        try:
            connection = self.__db.getConnection()
            cursor = connection.cursor(dictionary=True)
            query = f"SELECT * FROM {table} WHERE {column} = %s LIMIT 1"
            cursor.execute(query, (value,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except mysql.connector.Error as e:
            return None 
    
    def create(self, user: UserDto):
        try:
            connection = self.__db.getConnection()
            cursor = connection.cursor()
            query =("""
            INSERT INTO user (NAME, LAST_NAME, RUT, MAIL, USER_TYPE) 
            VALUES (%s, %s, %s, %s, %s)
            """)
            values = (
                user.getName(),
                user.getLastName(),
                user.getRut(),
                user.getMail(),
                user.getTypeUser()
            )
            cursor.execute(query, values)
            connection.commit()

            userId = cursor.lastrowid
            user.setUserId(userId)

            cursor.close()
            connection.close()

            return user
        except mysql.connector.Error as e:
            print(f"Error al crear el usuario: {str(e)}")
            return None
    def read(self, userId: Optional[int]):
        try:
            connection = self.__db.getConnection()
            cursor = connection.cursor(dictionary=True)
            query = """
            SELECT u.USER_ID, u.NAME, u.LAST_NAME, u.RUT, u.MAIL, u.USER_TYPE
            FROM USER u
            JOIN CREDENTIALS c ON u.USER_ID = c.USER_ID
            WHERE u.USER_ID = %s"""
            cursor.execute(query, (userId,))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return UserDto(
                    user['USER_ID'],
                    user['NAME'],
                    user['LAST_NAME'],
                    user['RUT'],
                    user['MAIL'],
                    user['USER_TYPE']
                )
            else:
                return None 
        except mysql.connector.Error as e:
            print(f"Error al ver su perfil: {str(e)}")
            return None
        
    def update(self, user: UserDto):
        try:
            connection = self.__db.getConnection()
            cursor = connection.cursor()
            query =("""
            UPDATE user
            SET NAME = %s, LAST_NAME = %s, RUT = %s, MAIL = %s, USER_TYPE = %s
            WHERE ID = %s
            """)
            values = (
                user.getName(),
                user.getLastName(),
                user.getRut(),
                user.getMail(),
                user.getTypeUser(),
                user.getUserId()
            )
            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()
            return user
        except mysql.connector.Error as e:
            print(f"Error al actualizar el usuario: {str(e)}")
            return None
        
    def delete(self, userId: Optional[int]):
        try:
            connection = self.__db.getConnection()
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (userId,))
            connection.commit()

            cursor.close()
            connection.close()

            return True
        except mysql.connector.Error as e:
            print(f"Error al eliminar el usuario: {str(e)}")
            return False

        




