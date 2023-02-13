#Escribe una función que pueda decirte 
#si un año (número entero) es bisiesto o no.

#año no bisiesto 365 dias.
#año bisiesto 366 dias.

def conocerAño(año):
	if año == 366:
		print("El año es bisiesto")
	else:
		print("El año no es bisiesto")

conocerAño(366)