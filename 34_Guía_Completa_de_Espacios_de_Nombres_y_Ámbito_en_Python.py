#Guía Completa de Espacios de Nombres y Ámbito en Python

'''
¿Qué es el ámbito (scope)?
Es el contexto donde una variable es accesible. Python sigue la regla LEGB:
Local: dentro de funciones
Enclosed: funciones anidadas
Global: fuera de funciones
Built-in: funciones y nombres integrados
'''
#Ejemplo :

#Alcance local: variable dentro de una función
def imprimir_nombre():
    nombre = "Programación Fácil"
    print("Local:", nombre)

imprimir_nombre()
# print(nombre)  #Error: NameError

#Diccionario local con locals()
def funcion():
    a = 10
    b = "Hola"
    c = 10.56
    print("Diccionario local:", locals())

funcion()

#Alcance global: variable fuera de funciones
nombre = "PCMaster"

def imprimir_nombre():
    nombre = "Programación Fácil"  # Variable local
    print("Local:", nombre)

imprimir_nombre()
print("Global:", nombre)

#Diccionario global con globals()
nombre = "Programación Fácil"
print("Diccionario global:", globals()["nombre"])

#Acceder al espacio de nombres de un módulo
import random
print("Espacio de nombres de random:", random.__dict__)

#Usar vars() para ver atributos de clases y objetos
class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

usuario1 = Usuario("Enrique", "Barros", 32)
usuario2 = Usuario("Elvira", "Gómez", 27)
usuario1.correo = "correo@gmail.com"
usuario2.telefono = "123456789"

print("Clase Usuario:", vars(Usuario))
print("Usuario 1:", vars(usuario1))
print("Usuario 2:", vars(usuario2))

#Alcance encerrado con funciones anidadas
def funcion_externa():
    a = 10
    def funcion_interna():
        b = 20
        print("Encerrado:", a, b)
    funcion_interna()

funcion_externa()

#Uso de nonlocal para modificar variable del ámbito superior
def funcion_externa():
    a = 10
    def funcion_interna():
        nonlocal a
        a = 100
        print("Interna:", a)
    funcion_interna()
    print("Externa:", a)

funcion_externa()
'''
#Error si nonlocal no encuentra variable en el ámbito superior
def funcion_externa():
    def funcion_interna():
        nonlocal b  #Error: no binding for nonlocal 'b'
        b = 100'''

#Alcance predefinido con __builtins__
print("Built-in:", __builtins__.__dict__["print"])

#Alcance de bloque no existe en Python
if True:
    nombre = "Variable declarada"

print("Fuera del bloque:", nombre)  # ✅ Accesible

#Uso de global para modificar variable global desde función
nombre = "PCMaster"

def imprimir_nombre():
    global nombre
    nombre = "Programación Fácil"
    print("Dentro:", nombre)

imprimir_nombre()
print("Fuera:", nombre)

#Crear variable global desde función
def funcion():
    global a
    a = 10

funcion()
print("Variable global creada:", a)

#Uso recomendado: devolver valor en lugar de usar global
var = 1

def foo():
    print("Antes:", var)
    return 10

var = foo()
print("Después:", var)

#Usar dir() para ver nombres en el espacio actual
from math import acos
print("Espacio actual:", dir())

import random
aleatorio = random.randint(10, 60)
print("Actualizado:", dir())

def prueba():
    variable_prueba = None
    print("Dentro de función:", dir())

prueba()
