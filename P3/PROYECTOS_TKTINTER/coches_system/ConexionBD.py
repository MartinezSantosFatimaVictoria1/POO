import mysql.connector

class ConexionBD:
    """Clase para gestionar la conexión a la base de datos."""
    
    @staticmethod
    def conectar():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bd_coches" 
            )
            return conexion
        except Exception as e:
            print(f"Error al conectar a la BD: {e}") 
            return None