"""
    Ejercicio Practico 2 "Modelar y Diagramar en POO"
"""
import os
os.system("cls")

#Clase de coches
class Coches:
    #metodo constructor que inicializa cuando se instancia un objeto de la clase
    def __init__(self,color,marca,velocidad):
        self.color=color #Atributos del objeto
        self.marca=marca
        self.velocidad=velocidad

    #Metodos del objeto
    def acelerar(self,incremento):
        self.velocidad=self.velocidad+incremento
        return self.velocidad
    
    def frenar(self,decremento):
        self.velocidad=self.velocidad-decremento
        return self.velocidad
    
    def tocar_claxon(self):
        return "piiiiii"
    
#Instanciar o crear objetos de la clase Coches
coche1=Coches("Blanco","Toyota",220)
coche2=Coches("Amarillo","Nissan",180)

print(coche1.acelerar(50))
print (coche2.frenar(100))

#print(f"Los valores del objeto 1 son:{coche1.marca},{coche1.color},{coche1.velocidad}")
#velocidad=coche1.acelerar(50)
#print(f"El coche 1 acelero de: {coche1.velocidad} a {coche1.acelerar(50)}")

#print(f"Los valores del objeto 2 son:{coche2.marca},{coche2.color},{coche2.velocidad}")
#velocidad=coche2.frenar(100)
#print(f"El coche 2 freno de: {coche2.velocidad} a {coche2.frenar(100)}")