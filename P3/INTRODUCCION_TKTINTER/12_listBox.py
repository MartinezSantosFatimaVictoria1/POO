from tkinter import *

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")

def mostrarEstado():
    resultado.config(text="Valor seleccionado por el usuario:")

valor=IntVar()
escala= Scale (ventana, from_=0, to=100, orient='horizontal',variable=valor)
escala.pack()

boton= Button(ventana, text="Confirmar", command=mostrarEstado)
boton.pack

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()