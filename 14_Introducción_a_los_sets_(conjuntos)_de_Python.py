'''
Los sets, conocidos en español como conjuntos, son estructuras de datos que almacenan valores únicos, es decir, no permiten duplicados. 
Al contrario de las listas o tuplas, los conjuntos no mantienen un orden específico para sus elementos; estos se colocan aleatoriamente al ejecutar el código.
'''

#¿Por qué los conjuntos solo aceptan objetos inmutables?
'''
Principalmente, los conjuntos no aceptan objetos mutables como elementos, debido a la forma en que Python maneja los elementos en un conjunto.
 Los conjuntos utilizan el hash de los objetos para almacenar elementos y comprobar si existen duplicados. 
'''

#Sintaxis

'''
La sintaxis de un conjunto es la misma que una tupla o una lista, con la diferencia de que estos se crean con unas llaves ({ }):
{elemento1, elemento2, elemento3, ...}
'''
#Ejemplo de uso de un conjunto
set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
print(set_colores)

#Métodos para sets de Python

'''
Añadir valores a un conjunto con el método add()
Para añadir valores a un conjunto, podemos hacerlo con el método llamado add():
'''
set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
# Añade un elemento al set
set_colores.add("marrón")
print(set_colores)

'''
Eliminar valores de un conjunto con el método remove()
Para eliminar valores en un conjunto, podemos utilizar el método remove():
'''
set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
# Se elimina un valor del set
set_colores.remove("azul")
print(set_colores)

'''
Eliminar elementos con el método discard()
Con los conjuntos tenemos otro método para eliminar elementos.
Realiza la misma función, pero si el elemento pasado no existe, simplemente ignora la acción en lugar de devolver un error
'''
set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
# Se elimina un valor del set
set_colores.discard("cian")
print(set_colores)

'''
Elementos duplicados en los conjuntos
Como he indicado al principio, los conjuntos no pueden contener valores repetidos. 
Esto quiere decir que si ponemos un dato varias veces, se van a descartar todas las repeticiones.
'''
set_colores = {"rojo", "verde", "azul", "rojo", "blanco", "rojo", "rojo"}
print(set_colores)

'''
Ver el total de elementos que tiene un conjunto
Para contar el total de elementos que tiene un objeto como un conjunto, puedes utilizar la función predefinida len() de Python:
'''
set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
# Se cuentan los elementos
cantidad_elementos = len(set_colores)
print(f"El objeto tiene {cantidad_elementos} elementos.")
'''Lo mismo puedes hacer con otros objetos iterables de Python, como las listas, tuplas, cadenas, etc.'''
saludo = "Hola"
# Se cuentan los caracteres
cantidad_caracteres = len(saludo)
print(f"El texto tiene {cantidad_caracteres} caracteres.")

'''
Ver los valores mayores y menores de un conjunto
Mediante el uso de las funciones predefinidas min() y max() de Python, puedes obtener los valores mínimo y máximo de un conjunto, respectivamente.
'''
'''min() que mostrará el valor más bajo contenido en el conjunto:'''
set_colores = {100, 6578, 54, 4, 56, 2}
# Se busca el valor más bajo del conjunto
valor_minimo = min(set_colores)
print(f"El valor mínimo del conjunto es: {valor_minimo}")

'''max() mostrará el valor máximo en el conjunto:'''
set_colores = {100, 6578, 54, 4, 56, 2}
# Se busca el valor más alto del conjunto
valor_maximo = max(set_colores)
print(f"El valor máximo del conjunto es: {valor_maximo}")

'''Es posible encontrar los valores mayores y menores de conjuntos con cadenas de caracteres. En este caso, la lógica se aplica en orden alfabético.'''
set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
# Se busca el color más "pequeño" alfabéticamente
color = min(set_colores)
print(color)

#Inmutabilidad con frozensets
'''
Para que entiendas bien lo que son los frozensets, vamos a hacer una comparación.

'''
#Sintaxis de un frozenset
'''frozenset([elemento1, elemento2, elemento3, ...])'''
#ejemplo
numeros = frozenset([1, 2, 3, 4, 5])

print(numeros)


