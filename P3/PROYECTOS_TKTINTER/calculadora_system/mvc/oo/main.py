"""
crear una calculadora:
1.-dos botones de campo de texto
2.- 4 botones para las operaciones
3.-Mostrar el resultado en una alerta
4.-Programacion Estructurada
5.-Implementar el MVC
"""

from view import interfaz
from tkinter import * 

class App:
    def __init__(self,ventana):
        view=interfaz.Vistas(ventana)


#def main():
#    interfaz.interfaz()

if __name__ =='__main__':
      ventana=Tk()
      app=App(ventana)
      ventana.mainloop()