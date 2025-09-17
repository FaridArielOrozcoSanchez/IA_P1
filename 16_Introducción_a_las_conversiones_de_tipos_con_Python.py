'''
La conversión de tipos de datos, llamada casting en inglés, es el proceso de cambio de un tipo de dato a otro compatible. Esta acción la necesitaremos en múltiples ocasiones.
Por ejemplo, si queremos transformar la entrada de un input(), la cual se guarda como str, pero necesitamos un int o un float, para operar con él.
'''

#Funciones predefinidas para conversiones
'''
Muchas de las funciones predefinidas de Python sirven para realizar conversiones. A continuación tienes un listado de ellas:

int(): Convierte un valor a un número entero.
float(): Convierte un valor a un número de coma flotante.
str(): Convierte un valor a una cadena de caracteres.
bool(): Convierte un valor a un booleano.
complex(): Convierte un valor a un número complejo.
ord(): Convierte un carácter a su código Unicode.
chr(): Convierte un código Unicode a un carácter.
hex(): Convierte un número a su representación hexadecimal.
oct(): Convierte un número a su representación octal.
bin(): Convierte un número a su representación binaria.
'''

#Conversión implícita
'''
La conversión implícita es la que ocurre cuando el intérprete de Python transforma el tipo de dato automáticamente. 
Por ejemplo, si sumamos un número entero (int) con un número con decimales (float), Python realizará la conversión implícita del entero, al tipo float, antes de realizar la suma.
De esta forma es posible operar con ambos tipos de datos sin tener errores.
'''
numero_1 = 10
numero_2 = 20.5
print(numero_1 + numero_2)

#¿Cómo saber el tipo de dato en Python?
'''
En Python podemos comprobar cualquier tipo de dato con la función predefinida type().
Observa el siguiente ejemplo:
'''
numero_1 = 10
numero_2 = 20.5
print(type(numero_1 + numero_2))

#Conversión explícita
'''
La conversión explícita es aquella que hacemos manualmente, escribiéndola en el código. Veamos un ejemplo de esto con la función predefinida int():
'''
numero = 100.43
numero_entero = int(numero) # Se convierte en int
print(numero)
print(numero_entero)

#Analizar los tipos de datos
'''
En este ejemplo estoy realizando la operación de suma de los dos valores entrados desde la consola (10 y 24).
Después imprimo tanto los tipos de datos de los valores introducidos, como el tipo de dato que produce el resultado final, gracias a la función predefinida type().
De este modo, en todo momento podemos apreciar en la consola los tipos de datos que se están manejando.
'''
numero_1 = input("Introduzca el primer número: ")
numero_2 = input("Introduzca el segundo número: ")
suma = numero_1 + numero_2
print(f"El resultado es: {suma}")
print(f"Tipo de numero_1: {type(numero_1)}")
print(f"Tipo de numero_2: {type(numero_2)}")
print(f"Tipo de suma: {type(suma)}")

#Conversión int()
'''
Para realizar una conversión a tipo int, lo haremos con la función predefinida int().
En el siguiente código, estoy transformando numero_1 y numero_2, que llevarán originalmente valores str, a tipo int:
'''
numero_1 = input("Introduzca el primer número: ")
numero_2 = input("Introduzca el segundo número: ")
numero_1 = int(numero_1)
numero_2 = int(numero_2)
suma = numero_1 + numero_2
print(f"Tipo de numero_1: {type(numero_1)}")
print(f"Tipo de numero_2: {type(numero_2)}")
print(f"Tipo de suma: {type(suma)}")
print(f"El resultado de la suma es: {suma}.")

#Conversión float()
numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))
suma = numero_1 + numero_2
print(f"Número 1: {numero_1}")
print(f"Número 2: {numero_2}")
print(f"El resultado de la suma es: {suma}.")

#Conversión bool()
'''
Las conversiones explícitas a tipo de dato bool las haremos con la función predefinida bool().
La lógica booleana establece que numéricamente hablando, el valor 0 corresponde al valor booleano False, y 1 al valor True.
'''
interruptor = 1
# Convierte el valor entero a bool
booleano = bool(interruptor)
print(booleano)
interruptor = 0
# Convierte el valor entero a bool
booleano = bool(interruptor)
print(booleano)

#Conversión str()
'''
Las conversiones explícitas a tipo de dato str, las haremos con la función str().
'''
numero = 1000
# Convierte el valor int a str
cadena = str(numero)
print(type(cadena))

decimal = 1000
# Se convierte el decimal en hexadecimal
hexadecimal = hex(decimal)
print(hexadecimal)