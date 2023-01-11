#Escribe un programa en la consola de python que pida 
#al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, 
#e imprima por pantalla la frase Tu índice de masa 
#corporal es donde es el índice de masa corporal 
#calculado redondeado con dos decimales. 

print("*********Bienvenido***********")


peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su altura en mts: "))

masaCorporal = peso / pow(estatura, 2)

print("Su peso es: ", peso, "Kg")
print("Su estatura es: ", estatura, "mts")
print("El indice de masa corporal es: ", masaCorporal)

if masaCorporal < 18.5:
	print("Peso inferior al normal")
if masaCorporal > 30.0:
	print("posee un nivel de obesidad, debe mejorar su estilo de vida y dieta")
