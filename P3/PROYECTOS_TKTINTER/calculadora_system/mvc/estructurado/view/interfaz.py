"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 Botones para las Operaciones
3.- Mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox
from controller import funciones

ventana=Tk()
ventana.title("Mi primer App con tkinter")
ventana.geometry("600x400")
ventana.resizable(False,False)



n1=IntVar
n2=IntVar
txt_num1=Entry(ventana,textvariable=n1 ,width=5,justify=RIGHT)
txt_num1.pack(side=TOP)
txt_num2=Entry(ventana,textvariable=n2 ,width=5,justify=RIGHT)
txt_num2.pack(side=TOP)

boton_sum=Button(ventana, text="+", command=lambda:funciones.suma(n1.get(),n2.get()))
boton_sum.pack()

boton_res=Button(ventana, text="-", command=lambda:funciones.resta)
boton_res.pack()

boton_mul=Button(ventana, text="x", command=lambda:funciones.multiplicacion)
boton_mul.pack()


boton_div=Button(ventana, text="/", command=lambda:funciones.division)
boton_div.pack()


boton_salir=Button(ventana, text="-", command=lambda:funciones.ventana.quit)
boton_salir.pack()

ventana.mainloop()