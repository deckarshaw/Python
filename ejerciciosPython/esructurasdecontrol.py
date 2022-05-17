

def venderAlcohol(edad):


	if edad >= 18:

		return "puede comprar alcohol"



	else:

		return"No puedes comprar alcohol"


print (venderAlcohol(20))




def saludar(nombre):


	nombreRecibido = nombre.lower()

	if nombreRecibido == "marcos":

		return "Hola, bienvenido a la plataforma"

	else:

		return "No puede acceder a la plataforma"


print(saludar("MarCos"))









