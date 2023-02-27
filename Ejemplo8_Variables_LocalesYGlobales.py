"""
Variables:
Locales
en funciones (Se pueden llamar solo desde el interior)

Globales
en funciones (Se pueden llamar desde el exterior)

"""
# Variable global
variable_global = "Hola soy una variable global"


def funcion_local(variable):
    global variable_local  # Traspaso de variable LOCAL A GLOBAL.
    variable_local = variable  # variable Local hecho Global


funcion_local("Hola Soy una variable Local pasado a global")
print(variable_local)

""" 
def funcion_local(variable):
    #global variable_local
    variable_local_2= variable #variable Local

funcion_local("Hola Soy una variable Local pasado a global")    
print(variable_local_2) # No reconoce la variable       
"""
