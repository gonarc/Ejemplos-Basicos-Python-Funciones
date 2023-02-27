"""
Funcion para mostrar en pantalla el nombre que el usuario ingrese como parametro.
Funcion para mostrar en pantalla la edad que el usuario ingrese como parametro y definir si es mayor o menor de edad.


"""


def mostrarNombre(nombre, edad):
    edad = int(edad)
    # Funcion para mostrar el nombre en pantalla con parametro "(nombre)"
    print(f"El nombre pasado por parametro es: {nombre}.")
    print(f"La edad de {nombre} es: {edad} años.")
    if edad < 18:
        print(f"{nombre} es menor de edad")
    else:
        print(f"{nombre} es mayor de edad")
    print("")  # Salto de linea

    # Invocacion de funcion con input para que el usuario ingrese el nombre como parametro.


mostrarNombre(
    input("Por favor escriba el nombre que desea pasar como parametro: "),
    input("Por favor escriba la edad que desea pasar como parametro: "))
mostrarNombre(
    input("Por favor escriba el nombre que desea pasar como parametro: "),
    input("Por favor escriba la edad que desea pasar como parametro: "))
