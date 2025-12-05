import mysql.connector # type: ignore
from tkinter import messagebox

class Model:
    def __init__(self):
        try:
            
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="", 
                database="bd_coches"
            )
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Error Crítico", f"No hay conexión con la BD: {err}")

    
    def guardar_auto(self, datos):
        sql = "INSERT INTO autos (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, datos)
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error SQL: {err}")
            return False

    def obtener_autos(self):
        sql = "SELECT * FROM autos"
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except mysql.connector.Error:
            return []

    def modificar_auto(self, datos):
        sql = "UPDATE autos SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s"
        try:
            self.cursor.execute(sql, datos)
            self.conexion.commit()
            return True
        except mysql.connector.Error:
            return False

    def eliminar_auto(self, id_auto):
        sql = "DELETE FROM autos WHERE id = %s"
        try:
            self.cursor.execute(sql, (id_auto,))
            self.conexion.commit()
            return True
        except mysql.connector.Error:
            return False
