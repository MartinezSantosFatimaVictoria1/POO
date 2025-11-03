from conexionBD import *

class Autos:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas

    def insertar(self):
        try:
           cursor.execute(
               "insert into autos values(null,%s,%s,%s,%s,%s,%s)",
               (self._marca,self._color,self._modelo,self._velocidad,self._caballaje,self._plazas)
               )
           conexion.commit()
           return True
        except:  
           return False   

class Camionetas:
    @staticmethod #invocar un metodo sin hacer un objeto, para poder utilizarlos
    #se quita el self porque ya los reconoce, y marca error de que falta un parametro, apaarte de que ya es un metodo estático
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        try:
            cursor.execute("insert into camionetas values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                           marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            conexion.commit()
            return True
        except:
            return False    

class Camiones:
    @staticmethod
    def insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        try:
            cursor.execute("insert into camiones values(null,%s,%s,%s,%s,%s,%s,%s,%s)",
                           marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
            conexion.commit()
            return True
            
        except:
            return False    