#Guía de importación y uso de módulos con Python

'''
¿Qué es un módulo?
Un módulo es un archivo .py que contiene funciones, clases o variables que puedes reutilizar en otros programas.

Tipos de módulos
Integrados: como math, random, datetime
Externos: como numpy, pandas (requieren instalación con pip)
Propios: creados por ti, como calculadora.py
'''

#Importación de módulo integrado completo
import random

# Usamos una función del módulo
numero = random.randint(1, 1000)
print("Número aleatorio:", numero)

#Importación parcial con from
from random import randint, randrange

# Usamos las funciones directamente sin prefijo
print("Randint:", randint(1, 100))
print("Randrange:", randrange(0, 100, 5))

#Importación con alias
import random as rd

# Usamos el alias para acceder al módulo
print("Alias:", rd.randint(10, 50))

#Importación parcial con alias
from random import randint as rdi

# Usamos el alias directamente
print("Alias parcial:", rdi(100, 200))

#Importación de todo el módulo con *
from random import *

# Usamos cualquier función sin prefijo
print("Importación total:", uniform(1, 10))

#Espacio de nombres antes y después de importar
print("Antes:", dir())  # Muestra nombres definidos en el entorno actual

import math
print("Después:", dir())  # Ahora incluye 'math'

#Ver contenido de un módulo
import random
print("Contenido de random:", dir(random))  # Lista de funciones y atributos del módulo

#Importación dentro de una función (no recomendado)
def generar():
    import random
    print("Desde función:", random.randint(1, 10))

generar()
# print(random.randint(1, 10))  #Error: random no está definido fuera de la función

#Importación de módulo propio (calculadora.py)
# Supón que tienes un archivo calculadora.py con funciones sumar, restar, etc.

import calculadora
print(calculadora.sumar(5, 3))  # Salida: 8

#Importación específica desde módulo propio
from calculadora import sumar
print(sumar(10, 20))  # Salida: 30
