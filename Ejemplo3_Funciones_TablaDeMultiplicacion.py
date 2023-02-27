"""
Hacer una funcion que me de la tabla del numero que el usuario pase por parametro.

"""
contador = 1
resultado = 0


def tabla_multiplicacion(tabla):
    print("")
    print(f"--- TABLA DEL {tabla}. ---")
    print("")
    for contador in range(1,11):
        resultado = tabla*contador
        print(f"{tabla} X {contador} = {resultado}.")


tabla_multiplicacion(
    int(input("Ingrese el número de la tabla de multiplicación que desea ver: ")))
