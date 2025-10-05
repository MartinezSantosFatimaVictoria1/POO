import os
os.system("cls")

class Alumnos:
    def _init_(self, nombre, edad, matricula):
        self.__nombre = nombre        
        self.__edad = edad            
        self.__matricula = matricula  

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, valor):
        self.__curso = valor

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        self.__nota = valor

    
    def inscribirse(self, curso):
        self.__curso = curso
        

    def estudiar(self):
        return self.__estudiar

class Curso:
    def _init_(self, nombre_curso, codigo, creditos):
        self.__nombre_curso = nombre_curso
        self.__codigo = codigo
        self.__creditos = creditos
       
    @property
    def nombre(self):
        return self.__nombre

    @property
    def codigo(self):
        return self.__codigo

    @property
    def creditos(self):
        return self.__creditos

    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, valor):
        self.__profesor = valor

    def asignar(self, profesor):
        self.__profesor = profesor
        
class Profesor:
    def _init_(self, nombre_profe, experiencia, num_profesor):
        self.__nombre_profe = nombre_profe
        self.__experiencia = experiencia
        self.__num_profesor = num_profesor

    @property
    def nombre(self):
        return self.__nombre_profe

    @property
    def experiencia(self):
        return self.__experiencia

    @property
    def num_profesor(self):
        return self.__num_profesor

    def impartir(self, curso):
        curso.profesor = self
        

    def evaluar(self, alumno, nota):
        alumno.nota = nota
        
alumno1=Alumnos("Victoria", 19, 3141240135)
alumno2=Alumnos("Adrian", 18, 3141250624)

curso1 = Curso("frances", "fkl89", 5)
curso2 = Curso("POO", "poo2025", 9)

profesor1 = Profesor("Alejandro", 10, 25)
profesor2 = Profesor("xd", 15, 14)







