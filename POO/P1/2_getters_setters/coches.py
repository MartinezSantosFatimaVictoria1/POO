import os
os.system ("cls")


class Coches:
    __marca=""
    __color=""
    __modelo="" 
    __velocidad=0
    __caballaje=0
    __plazas=0
    
    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    
coche1=Coches()


coche1.setmarca("VW")
coche1.setcolor("Blanco")
coche1.setmodelo("2022")
coche1.setvelocidad(220)
coche1.setcaballaje(150)
coche1.setplaza(5)

print(f"Datos del Vehiculo: marca{coche1.getmarca()} color{coche1.getcolor()} modelo:{coche1.getmodelo()}velocidad{coche1.velocidad()}caballaje {coche1.getcaballaje}plazas{coche1.getplaza}")

coche2=Coches()

coche1.setmarca("Nissan")
coche1.setcolor("Azul")
coche1.setmodelo("2020")
coche1.setvelocidad(180)
coche1.setcaballaje(150)
coche1.setplaza(6)

#coche1.marca="VW"
#coche1.color="Blanco"
#coche1.modelo="2022" 
#coche1.velocidad=220
#coche1.caballaje=150
#coche1.plazas=5



#coche2.marca="Nissan"
#coche2.color="Azul"
#coche2.modelo="2020" 
#coche2.velocidad=180
#coche2.caballaje=150
#coche2.plazas=6



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