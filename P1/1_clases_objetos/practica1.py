"""
Practica 1, Implementar paradigma estructurado vs OO 
Crear un programa que obtenga el area de un rectangulo.
"""


#1.-Estructurado

import os
os.system("cls")

def areaRectangulo(base,altura):
    area=base*altura
    return area

base=5
altura=6
print(f"El area del rectangulo es: {areaRectangulo(base,altura)}")


#2.-OO

class AreaRectangulo:
    def areaRectangulo(self,base,altura):
        area=base*altura
        return area
    
rectangulo=AreaRectangulo() #instanciar un objeto de la clase "AreaRectangulo"
print(f"El area del rectangulo es: {rectangulo.areaRectangulo(base,altura)}")





class AreaRectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        
    def areaRectangulo(self):
        area=self.base*self.altura
        return area
    
rectangulo=AreaRectangulo() #instanciar un objeto de la clase "AreaRectangulo"
print(f"El area del rectangulo es: {rectangulo.areaRectangulo()}")

