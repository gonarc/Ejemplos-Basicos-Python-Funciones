"""
Realizar una calculadora utilizando funciones y return.

"""


def ingreso_datos(numero1, operador, numero2):
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    elif operador == "%":
        resultado = numero1 % numero2
    operacion = str(f"{numero1} {operador} {numero2} = {resultado} ")
    return operacion


print(ingreso_datos(int(input("Ingrese un número: ")), input(
    "Ingrese el operador: "), int(input("Ingrese el segundo número: "))))
print(ingreso_datos(int(input("Ingrese un número: ")), input(
    "Ingrese el operador: "), int(input("Ingrese el segundo número: "))))
