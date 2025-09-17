'''
Los diccionarios son estructuras de datos más complejas que las listas, tuplas o conjuntos, 
ya que están compuestos por pares de clave-valor que permiten almacenar información de forma más ordenada.
'''
#Sintaxis de un diccionario
'''
{clave1: valor1, clave2: valor2, clave3: valor3, ...}
El diccionario se declara haciendo uso de unas llaves ({ }) que envuelven todo el conjunto de datos.
Lo que encontramos dentro, es una serie de pares clave-valor separados por comas.
Las claves deben ser únicas y de tipo inmutable (como cadenas de texto o números), mientras que los valores pueden ser de cualquier tipo y mutables.
'''
#Crear un diccionario
'''
camiseta = ["rojo", "L", 100, 10]
Aquí es donde entran en juego los diccionarios. Gracias a las claves, podemos aportar una descripción a los valores. Mira cómo se podría hacer:
'''
#Ejemplo:
camiseta = {
"color" : "rojo",
"talla" : "L",
"precio" : 100,
"unidades" : 10
}
#Llamar a valores de diccionario
# Obtiene el valor asociado a la clave "color"
dato_obtenido = camiseta["color"]
# Vemos el resultado
print(dato_obtenido)

#Asignar nuevos valores a un diccionario
# Comprobamos el stock
print(f"Hay {camiseta['unidades']} unidades en el almacén.")
# Se modifica el valor de "unidades"
camiseta['unidades'] = 25
# Comprobamos el stock de nuevo
print(f"Hay {camiseta['unidades']} unidades en el almacén.")

#Crear claves y valores nuevos
# Se crea un nuevo par clave-valor en el diccionario
camiseta["material"] = "100% Algodón"
print(camiseta)

#Eliminar claves y valores en diccionarios
# Se elimina una clave y su valor asociado
del camiseta["color"]
print(camiseta)

#Eliminar un diccionario entero
'''
# Se elimina todo el diccionario
del camiseta
'''