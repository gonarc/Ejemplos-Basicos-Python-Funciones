"""
Guia de funciones predefinidas:

"""
print("Hola")#Muestra en pantalla
variable = "Hola mundo"

print(type(variable)) #str 
# Type() muestra el tipo de variable que se le pase: str,int,float,boolean,etc...

#Detectar tipado con isinstance(variable , tipo de dato a comprobar) si coincide da TRUE.
comprobar = isinstance(variable,str)
if comprobar:
    print("La variable es String") #La variable es String
else:
    print("La variable es otro tipo de dato.")

#Limpar todos los espacios a los lados de una cadena de caracteres con strip()
frase= "          Hola soy una frase con espacios a los lados.          "
print(frase)
print(frase.strip()) #Hola soy una frase con espacios a los lados.

#Eliminar variables
variable_para_eliminar = "Hola mundo"
print(variable_para_eliminar)#Hola mundo
del variable_para_eliminar #VARIABLE ELIMINADA.

#Comprobar si una variable esta vacia o tiene contenido con len().
verificar_contenido= "   Hola   "
print(f"Esta variable posee {len(verificar_contenido)} caracteres.")#Esta variable posee 10 caracteres. 
if len(verificar_contenido) <= 0:
    print("Esta variable no tiene contenido")
else:
    print(f"Esta variable tiene contenido, su contenido es: {verificar_contenido}") #Esta variable tiene contenido, su contenido es: "   Hola   " 

#Encontrar caracteres especificos con find("Palabra o caracter a buscar"), va a devolver la posicion en donde comienza el caracter o la palabra especificada.
frase_para_buscar="mi nombre es gonzalo, soy programador python"
print(frase_para_buscar.find("python")) #38

#reemplazar caracteres por otro o otros caracteres con   replace("palabra a reemplazar","reemplazo de palabra").
print(frase_para_buscar.replace("python","Java")) #mi nombre es gonzalo, soy programador Java

#Todo mayusculas con upper() y todo minusculas con lower()
print(frase_para_buscar.upper()) #MI NOMBRE ES GONZALO, SOY PROGRAMADOR PYTHON
print(frase_para_buscar.lower()) #mi nombre es gonzalo, soy programador python

