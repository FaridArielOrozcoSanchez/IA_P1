#Concatenacion, sirve para unir dos cadenas de formato especial
fragmento1 = "La programación es como la vida:"
fragmento2 = "llena de errores, pero también de posibilidades."
# concatenamos los dos strings
frase_completa = fragmento1 + fragmento2
# Imprimimos los dos strings en uno solo
print(frase_completa)

#Tipos de comillas en cadenas de caracteres: '' y ""
#Alternar comillas
#Para poder escribir comillas dentro de una cadena
print('"El tiempo es oro", me dijo.')
print("'El tiempo es oro', me dijo.")

#Escape de caracteres
#El escape de caracteres es una forma de incluir caracteres especiales en las cadenas de Python.
#Esta técnica se implementa mediante el símbolo de la barra invertida, contrabarra o backslash en inglés (\).
print('\'El tiempo es oro\', me dijo.')

#Sintaxis de f-strings de Python
# Solicitud de nombre
nombre = input("Por favor, introduzca su nombre:\n")
# Incrustación del valor de la variable en la cadena
print(f"Hola, {nombre}. Tenga un maravilloso día.")

#Cómo llamar a un método en Python
#objeto.nombre_metodo()
#La primera parte (objeto) es el objeto con el que queremos aplicar la llamada del método. Por ejemplo, un str.

#El método capitalize()
#El método capitalize() permite convertir el primer carácter de una cadena de caracteres en letra mayúscula, y el resto de caracteres los deja en minúsculas.
frase = "la imaginación es el principio de la creación."

# Primera letra mayúscula
frase_convertida = frase.capitalize()
print(frase_convertida)

#Entrada de datos con conversión de letra mayúscula
# Obtiene el nombre del usuario
nombre = input("Introduzca su nombre:\n")
# Convierte la primera letra en mayúscula
nombre_convertido = nombre.capitalize()
print(f"Hola {nombre_convertido}.")

#El método upper()
#El método upper() convierte el contenido de una cadena de caracteres, completamente en mayúsculas:
frase = "la imaginación es el principio de la creación."
# Todas las letras en mayúsculas
frase_convertida = frase.upper()
print(frase_convertida)

#El método lower()
#El método lower() convierte el contenido de una cadena de caracteres, completamente en minúsculas:
frase = "lA imAgiNAción ES el pRincipiO de LA CREAción."
# Todas las letras en minúsculas
frase_convertida = frase.lower()
print(frase_convertida)