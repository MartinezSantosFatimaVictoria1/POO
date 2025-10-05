import os
os.system ("cls")


class Coches:
    #Metodo constructor.-con este metodo se inicializa un objeto cuando es creado con valores iniciales
    
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas
        
    
    
    def acelerar(self):
        pass
    
    def frenar(self):
        pass

#multiples objetos
    
coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)
coche3=Coches("Honda","","",0,0,0)


print(f"Datos del Vehiculo: marca:{coche1.getmarca()} color:{coche1.getcolor()}modelo:{coche1.getmodelo()}velocidad:{coche1.velocidad()}caballaje: {coche1.getcaballaje}plazas:{coche1.getplaza}")


print(f"El coche 1 es un {coche1.marca} de color {coche1.color} y su velocidad es {coche1.velocidad}km/h y su ")
print(f"El coche 2 es un {coche2.marca} de color {coche2.color} y su velocidad es {coche2.velocidad}km/h y su ")
"""
Crear los métodos getter y setter. Estos métodos son importantes y necesarios en todas las clases para que el programador interactue con
los valores de los atributos a través de estos métodos. Digamos que es la manera más adecuada y recomendada para solicitar
un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo particular de la clase a través de un objeto.

En teoría se debería crear un método getters y setters por cada atributo que contenga la clase

Los métodos get siempre regresan valor, es decir, el valor de la propiedad a través del return.
Por otro lado el método set siempre recibe parámetros para cambiar o modificar el valor del atributo o propiedad en cuestión

"""
def getMarca(self):
    return self.__marca

def setMarca(self,marca):
    self.marca=marca
    
def getColor(self):
    return self.__color

def SetColor(self,color):
    self.color=color

def getModelo(self):
    return self.__modelo

def setModelo(self,modelo):
    self.modelo=modelo

def getVelocidad(self):
    return self.__velocidad

def setVelocidad(self,velocidad):
    self.velocidad=velocidad

def getCaballaje(self):
    return self.__caballaje

def setCaballaje(self,caballaje):
    self.caballaje=caballaje