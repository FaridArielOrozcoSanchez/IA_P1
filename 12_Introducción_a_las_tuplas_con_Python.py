'''Una tupla es una colección inmutable y ordenada de elementos.

Al igual que las listas, las tuplas tienen índice de posiciones, de ahí lo de “ordenada”. Entonces, estamos ante otro elemento iterable de Python.'''

#Sintaxis de una tupla:
#(elemento1, elemento2, elemento3)

#Ejemplo

tupla_colores = ("rojo", "verde", "azul") #Asi es como se ve una tupla, casi como una lista
print(tupla_colores)#Asi podeos visualizarla en la terminal, asi podemos visualizar los elementos que tiene la tupla

#Para ver solo un elemento podemos decidir a base de sus elemento enumerados en orden de la siguiente forma, van de 0 hasta el elemento que sea ultimo
print(tupla_colores[1])

#Métodos para tuplas

'''Las tuplas, al ser inmutables, no pueden utilizar algunos de los métodos que hemos usado en las listas. Cada elemento (objeto) de Python, tiene sus propios métodos.

Por ejemplo, no podemos eliminar un elemento de una tupla con el método pop():'''

#El método index() con tuplas

'''El método index() se utiliza indicando un elemento.
 Este nos devuelve su posición de índice, siempre que el elemento se encuentre en la tupla. Exactamente, el funcionamiento es el mismo que con las listas.'''
tupla_colores = ("rojo", "verde", "azul")
# Se busca la posición de índice de un elemento
print(tupla_colores.index("rojo"))

#El método count()
'''El método count() se puede usar también con las tuplas. 
Este lo emplearemos para contar el número total de veces que se encuentra un valor en ellas.'''
tupla_colores = ("rojo", "verde", "azul", "rojo", "amarillo")
# Se cuentan las veces que está el elemento
print(tupla_colores.count("rojo"))

#¿Cuándo utilizar tuplas en lugar de listas?
'''Tendrás que utilizar tuplas cuando necesites un conjunto de elementos inmutables. 
Es decir, datos que no deben cambiar durante la ejecución del programa.

Las tuplas son adecuadas para datos constantes, como coordenadas, fechas, configuraciones y otras situaciones en las que la información no debería cambiar inesperadamente.
Las listas, por otro lado, son más adecuadas cuando se necesita un conjunto de elementos que se puedan modificar en cualquier momento.'''

#Desempaquetado de tuplas y listas
'''La técnica de desempaquetado de tuplas se puede utilizar en listas también.
 Esta técnica consiste en obtener los valores de las posiciones de una tupla o lista, y distribuirlos en varias variables.
 A continuación tienes un ejemplo:'''

# Tupla para desempaquetar
numeros = (10, 20, 30, 40)

# Desempaquetado en variables
numero_1, numero_2, numero_3, numero_4, = numeros

# Comprobamos el resultado
print(numero_1)
print(numero_2)
print(numero_3)
print(numero_4)

#Recoger el exceso de valores en una lista
'''Cuando necesitas desempaquetar solo algunos valores de una colección más grande, puedes utilizar * delante de una variable para indicar que esa variable debe capturar todos los valores adicionales, organizándolos en una lista.'''
# Tupla con varios valores
numeros = (10, 20, 30, 40)

# Desempaquetado con una variable para capturar el exceso de valores
numero_1, numero_2, *resto = numeros

# Resultado
print(numero_1)
print(numero_2)
print(resto)
 #o

 # Tupla con varios valores
numeros = (10, 20, 30, 40)

# Lista vacía para almacenar valores restantes
resto = []

# Desempaquetado con una variable para capturar el exceso de valores
numero_1, numero_2, *resto = numeros

# Resultado
print(numero_1)
print(numero_2)
print(resto)