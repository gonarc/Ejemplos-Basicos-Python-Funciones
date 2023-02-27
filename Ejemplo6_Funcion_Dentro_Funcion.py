"""
FUNCIONES DENTRO DE FUNCIONES:

"""


def ingreso_nombre(nombre):
    texto = f"Su nombre es {nombre}"
    return texto


def ingreso_apellido(apellido):
    texto = f"Su apellido es {apellido}"
    return texto

#INCORPORACIONES DE FUNCIONES
def muestra_datos(nombre, apellido):
    texto = ingreso_nombre(nombre) + "\n" + ingreso_apellido(apellido)
    return texto


print(muestra_datos("Gonzalo", "Arce"))
