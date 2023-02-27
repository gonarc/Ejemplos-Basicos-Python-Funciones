"""
Funciones LAMBDA, utilización para funciones sencillas y de una linea.

"""
#Ejercicio: cúantos años pasaron desde el año X hasta el año actual (2023).
cuantos_years_pasaron= lambda year:f"Pasaron {abs(year - 2023)} años desde el 2023" #Funcion de una sola linea 
print(cuantos_years_pasaron(1994)) #Muestra en pantalla