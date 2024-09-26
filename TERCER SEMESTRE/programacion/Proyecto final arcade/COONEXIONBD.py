import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='usuariosemulador'
        )
        self.cursor = self.connection.cursor()

    def select_user_by_credentials(self, usuario, contrasena):
        sql = 'SELECT id, usuario, contrasena FROM usuario WHERE usuario = %s AND contrasena = %s'
        try:
            self.cursor.execute(sql, (usuario, contrasena))
            user = self.cursor.fetchone()
            return user

        except Exception as e:
            raise

    def add_user(self, usuario, contrasena):
        sql = "INSERT INTO usuario (usuario, contrasena) VALUES (%s, %s)"

        try:
            self.cursor.execute(sql, (usuario, contrasena))
            self.connection.commit()
            print("Usuario agregado correctamente.")

        except Exception as e:
            raise

    def delete_user(self, usuario, contrasena):
        sql = 'DELETE FROM usuario WHERE usuario = %s AND contrasena = %s'
        try:
            self.cursor.execute(sql, (usuario, contrasena))
            self.connection.commit()
            print("Usuario eliminado correctamente.")

        except Exception as e:
            self.connection.rollback()
            raise

    def user_exists(self, usuario):
        sql = 'SELECT COUNT(*) FROM usuario WHERE usuario = %s'
        try:
            self.cursor.execute(sql, (usuario,))
            count = self.cursor.fetchone()[0]
            return count > 0

        except Exception as e:
            raise

    def close(self):
        self.connection.close()
