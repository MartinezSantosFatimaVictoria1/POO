#Encapsular. Es un pilar de la POO que permite indicar cual es la manera de como poder utilizar los atributos y métodos de una clase
#a la hora de usar en objetos o en herencia

import os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo público"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

def __init__(self,color,tamanio):
    self.__color=color
    self.__tamanio=tamanio

@property #Método get
def color(self):
    return self.__color

@color.setter #Método set
def color(self,color):
    self.__color=color

@property
def tamanio(self,tamanio):
    return self.__tamanio

@tamanio.setter
def tamanio(self,tamanio):
    self.__tamanio=tamanio

@property
def atributo_publico(self):
    return self.atributo_publico

@atributo_publico.setter
def atributo_publico(self,atributo_publico):
    self.atributo_publico=atributo_publico

@property
def atributo_protegido(self):
    return self._atributo_protegido

@atributo_protegido.setter
def atributo_protegido(self,atributo_protegido):
    self._atributo_protegido=atributo_protegido

@property
def atributo_privado(self):
    return self.__atributo_privado

@atributo_privado.setter
def atributo_privado(self,atributo_privado):
    self.__atributo_privado=atributo_privado

def getAtributoPrivado(self):
    return self.__atributo_privado


#Utilizar la clase

objeto=Clase("Rojo","Grande")
#print(objeto.atributo_publico) #No es una buena práctica acceder a los valores directamente
#print(objeto._atributo_protegido)

print(objeto.__atributo_privado)
print(objeto.atributo_publico)
print(objeto._atributo_protegido)
