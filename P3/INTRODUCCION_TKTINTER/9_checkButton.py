from tkinter import * 

ventana = Tk()
ventana.title("checkButton")
ventana.geometry("500x500")

def mostrarEstado():
    if opcion.get()==1:
        resultado.config(text="Notificaciones...")
    else:
        resultado.config(text="Notificaciones desactivadas...")  


Boton = Button(ventana , text="Confirmar", command=mostrarEstado)
Boton.pack() 

opcion=IntVar()
checkButton=Checkbutton(ventana,text="¿Deseas recibir notificaciones?",
variable=opcion, onvalue=1,offvalue=0)
checkButton.pack()

resultado = Label(ventana, text="")
resultado.pack()

ventana.mainloop()

