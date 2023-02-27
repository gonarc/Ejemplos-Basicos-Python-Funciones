"""
Definir una funcion con dos parametros opcionales, en caso de que no se ingrese algun valor en ellos,
omitirlo y mostrar solamente el que se ingreso.

"""


def empleado(nombre, telefono = 0):
    print("")
    print(f"Nombre del empleado es: {nombre}")
    if telefono == 0: #En caso de no ingresarle el parametro por defecto su valor va a ser 0. 
        pass
    else:
        print(f"Su telefono es: {telefono}")
    print("")

#Invocacion de la funcion
empleado("Gonzalo", 15689484)  # Con parametro opcional.
empleado("Gonzalo",)  # Sin parametro opcional.
