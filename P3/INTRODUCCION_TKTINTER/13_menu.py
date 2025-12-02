from tkinter import *


def mostrarEstado():
    resultado.config(text="")


ventana=Tk()
ventana.title("Menú")
ventana.geometry("500x500")

menuBar=Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu=Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='Archivo',menu=archivoMenu)
archivoMenu.add_command(label='Nuevo Archivo',command=mostrarEstado)
archivoMenu.add_command(label='Guardar Archivo',command=mostrarEstado)
archivoMenu.add_separator()
archivoMenu.add_command(label='Salir',command=ventana.quit)

edicionMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label='Edicion',menu=edicionMenu)
edicionMenu.add_command(label='Copiar',command=mostrarEstado)
edicionMenu.add_command(label='Recortar',command=mostrarEstado)
edicionMenu.add_separator()
edicionMenu.add_command(label='Salir',command=ventana.quit)


resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()