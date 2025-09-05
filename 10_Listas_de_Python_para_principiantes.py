'''
Las listas son estructuras de datos que se utilizan para almacenar colecciones ordenadas de elementos. 
Estos elementos pueden ser de cualquier tipo, como números, cadenas de caracteres, booleanos o incluso otras listas.
'''
#Creando una lista de Python
#Gracias a las listas, podremos agrupar datos que estén relacionados. Mira este ejemplo con cuatro variables:
# Camiseta
color = "rojo"
talla = "L"
precio = 100
cantidad = 10
#Para este propósito, vamos a guardar la lista dentro de una variable, así podremos manejarla, al estar asociada a un identificador:
camiseta = ["rojo", "L", 100, 1]

#Para imprimir una lista como la anterior, solo tienes que llamar a la variable que la contiene:
print(camiseta)

#índice de posiciones en las listas
'''
El índice de posición es una numeración que tienen las listas en cada una de sus posiciones. 
Gracias a este índice, podemos manipular cada elemento de la lista de manera individual.
El índice de posición de una lista empieza a contar desde el número 0.
'''
colores = ["azul", "verde", "rojo"]
#Sintaxis de asignación en listas
'''Para asignar un valor a cierta posición de una lista, lo haremos de forma parecida a la asignación de valores a las variables.
Solo que tendremos que añadir un valor extra, el conocido como índice de posición.'''
colores = ["azul", "verde", "rojo"]
# Reasigna el valor a la posición 0 de la lista
colores[0] = "amarillo"
# Imprime el resultado
print(colores)

#Métodos para añadir elementos en listas
'''
El método append() sirve para añadir un elemento al final de una lista
El método insert() de Python también permite insertar un elemento en una lista.
La diferencia con el método anterior, es que con este método podemos especificar una posición concreta en la que queremos insertar el elemento.
Índice inexistente: Con este método, si indicas una posición de índice inexistente, Python solucionará el fallo. A pesar de ello, intenta no equivocarte con esto, ya que puede dificultar la interpretación del código por parte de las personas.
El método extend() de Python, sirve para “extender” una lista a partir de un elemento iterable (no todos los tipos de datos son iterables).
'''
colores = ["azul", "verde", "rojo"]
# Añade el elemento "amarillo" al final de la lista
colores.append("amarillo")
print(colores)

colores1 = ["azul", "verde", "rojo"]
# Se añade el elemento "amarillo" en la posición 0 del índice
colores1.insert(0, "amarillo")
print(colores1)

colores2 = ["azul", "verde", "rojo"]
# Inserta el elemento "amarillo" en la posición 7
colores2.insert(7, "amarillo")
print(colores2)

colores3 = ["azul", "verde", "rojo"]
colores4 = ["amarillo", "naranja", "marrón"]
# Extiende la lista
colores3.extend(colores4)
print(colores3)
#Otra forma
colores1 = ["azul", "verde", "rojo"]
colores2 = ["amarillo", "naranja", "marrón"]
# Concatena las listas
colores1 = colores1 + colores2
print(colores1)


#Métodos para eliminar elementos en listas Python
'''
El método pop() sirve para eliminar un elemento de una lista. Este método puede ser utilizado de dos formas. Con un argumento, o sin él.
El método remove() elimina un elemento literal concreto.
'''

colores = ["azul", "verde", "rojo"]
# Se elimina el último elemento de la lista
colores.pop()
print(colores)

colores = ["azul", "verde", "rojo"]
# Elimina el elemento de la posición 0
colores.pop(0)
print(colores)

colores = ["azul", "verde", "rojo"]
# Elimina el elemento "rojo"
colores.remove("rojo")
print(colores)

#Métodos para buscar elementos en listas de Python
'''
El método index() se encarga de buscar un elemento en una lista. Solo va a buscar hasta encontrarlo una vez; si está repetido, ignora el resto de resultados.
El método count() también busca elementos en las listas, pero es sustancialmente diferente. Este método busca todas las coincidencias y nos dice cuántas hay en una lista.
'''

numeros = [87, 10, 5, 7, 378, 10, 10, 65, 10]
# Guardamos lo que devuelve index() en una variable
busca_numero = numeros.index(378)
print(busca_numero)

numeros = [87, 10, 5, 7, 378, 10, 10, 65, 10]
# Especificamos un valor de búsqueda
valor_busqueda = 10
# Buscamos el total de coincidencias
coincidencias = numeros.count(valor_busqueda)
print(f"En total, el valor de búsqueda {valor_busqueda}, tiene {coincidencias} coincidencias.")