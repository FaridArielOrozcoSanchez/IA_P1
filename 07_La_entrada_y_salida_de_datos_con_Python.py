#La función predefinida print()
#print(*objects, sep=' ', end='\n', file=None, flush=False)
#El parámetro *objects
"""El primer parámetro, *objects, es una característica de Python llamada *args, la cual, nos permite pasarle un ilimitado número de objetos (argumentos) a la función que la utiliza.
En Python, las cosas están formadas por objetos. Por ejemplo, una cadena (str) es un objeto, un int, es otro objeto.
"""
print("El resultado","de sumar",10,"más",50.65,"es:",10+50.65)

#El parámetro sep: Esto quiere decir, que tras cada objeto que le pasamos a la función, se aplica un espacio en el resultado final de la consola. 
sep=' '

#Saltos de línea y el parámetro end: \n
print("Línea 1\n" + "Línea 2\n" + "Línea 3")

#La función input()
#La entrada de datos se refiere a la información que el usuario introduce en un programa.
# Entrada de datos
nombre = input("Por favor, introduce tu nombre: ")

# Salida de datos
print("El nombre almacenado es: " + nombre + ".")

#Tipos de datos en las entradas
# Solicita dos números para sumar
numero_1 = input("Introduce el primer número a sumar: ")
numero_2 = input("Introduce el segundo número a sumar: ")

# Realiza y guarda la suma
suma = numero_1 + numero_2

# Muestra el resultado
print(suma)
