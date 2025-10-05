#Instanciar los objetos para posteriormente implementarlos

from coches import Coches,Camiones,Camionetas

coche=Coches("VW","Blanco","2020",220,200,5)
print(coche.marca, coche.acelerar())

camioneta=Camionetas("Nissan","Amarillo","2025",180,200,4,"trasera",False)
print(camioneta.marca, camioneta.acelerar())

camioneta=Camionetas("Nissan","Amarillo","2025",180,200,4,"trasera",False)
print(camioneta.marca, camioneta.acelerar())
#num_coches=int(input("Cuantos coches quieres crear: "))


#for i in range(0,num_coches):
#	print(f"Datos del coche {i+1}")
#	marca=input("Introduce la marca del coche: ").upper()
#	color=input("Introduce el color del coche: ").upper()
#	modelo=input("Introduce el modelo del coche: ").upper()
#	velocidad=int(input("Introduce la velocidad del coche: "))
#	potencia=int(input("Introduce el potencia del coche: "))
#	plazas=int(input("Introduce el numero de plazas del coche: "))


#	coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)
#	print(f"El coche 1 es un {coche1.getMarca()} y el color es {coche1.getColor()} Modelo:{coche1.getModelo()} Velocidad:{coche1.getVelocidad()} Caballaje{coche1.getCaballaje()} Plazas{coche1.getPlazas()}" )
	
#	print(coche1.acelerar())



#coche1=Coches("VW","Blanco","2022",220,150,5)
#coche2=Coches("Nissan","Azul","2020",180,150,6)
#coche3=Coches("Honda","","",0,0,0)
