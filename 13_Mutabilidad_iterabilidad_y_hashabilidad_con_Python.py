#Mutabilidad
'''Los objetos mutables (cambiantes) son aquellos cuyos valores internos pueden ser modificados después de su creación.
Algunos ejemplos de objetos mutables son: list, dict y set.
'''
#creamos una lista
lista = [10, 10, 30, 40]
# Reasigna el valor 20 a la posición 1 de la lista
lista[1] = 20
#mostramos lista
print(lista)

#Inmutabilidad
'''Los objetos inmutables (no cambiantes) son aquellos cuyos valores internos no pueden ser modificados después de su creación.
Algunos ejemplos de objetos mutables son: int, float, str y tuple.
'''

saludo = "Hola"

print(saludo[0])
print(saludo[1])
print(saludo[2])
print(saludo[3])

#Hashabilidad
'''Para que un objeto sea hashable, debe ser inmutable, tener un valor de hash constante en tiempo de ejecución y que sea comparable con otros objetos de su tipo para determinar si son iguales.

En Python, un hash es un valor entero que se obtiene al aplicar la función hash() a un objeto, y se utiliza para identificar ese objeto en estructuras como diccionarios o conjuntos.
Para que un objeto en Python sea "hashable" (es decir, que se le pueda aplicar un hash), debe cumplir dos requisitos: tener un valor inmutable y definir los métodos __hash__() y __eq__().
'''

saludo = "Hola"

# Imprime el hash del objeto
print(hash(saludo))

#Iterabilidad`
'''
La iterabilidad es la capacidad de un objeto en ser recorrido con posiciones de índice.
 Por ejemplo, una lista, una tupla o una cadena, son objetos iterables, porque tienen índice de posición.
'''

numeros = [10, 20, 30]

# Imprime la posición 0 de la lista
print(numeros[0])

