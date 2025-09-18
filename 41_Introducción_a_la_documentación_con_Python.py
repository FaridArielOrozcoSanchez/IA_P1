#Introducción a la documentación con Python

'''
La importancia de la documentación
En programación, el orden y la claridad, son dos de las partes fundamentales. Sin ellas, todo lo que hagas, será muy difícil de entender y mantener.
Imagina una biblioteca de Python, que no tenga documentación en absoluto, ni tutoriales. Solo el código.
Esto hará que tengas que utilizar otra biblioteca, en su lugar, o bien, que estés horas o días investigando como utilizar cada cosa.
Si tienes una documentación a mano, puedes consultar de forma rápida, todo lo que puedes hacer y como lo puedes hacer, errores y malas prácticas que se pueden evitar, etc.
'''

#Comentario de una línea
# Multiplica dos números
def multiplicar(a, b):
    return a * b

# Esta función devuelve un resultado aleatorio
# Paso 1: Solicitar al usuario un número
# Paso 2: Convertir el número a entero
# Paso 3: Comprobar si es par o impar

#Etiquetas útiles en comentarios
# BUG: Este bucle falla con valores negativos
for i in range(10):
    pass

# FIXME: Esta función es ineficiente, probar con generadores
def procesar_valores(valores):
    pass

# TODO: Implementar la función 'calcular_impuestos()'
# NOTE: Mejora el rendimiento general. Manipular con cautela.

#Tipado con anotaciones (desde Python 3.5+)
def longitud(cadena: str) -> int:
    return len(cadena)

print(type(longitud("Hola")))  # <class 'int'>

#Tipado con múltiples parámetros
def calcular_total(par1: object, par2: int, par3: float) -> float:
    return par2 + par3

#Función que imprime pero no devuelve (None)
def suma_decimales(a: float, b: float) -> None:
    print(a + b)

suma_decimales(10.5, 20.4)
print(suma_decimales(10.5, 20.4))  # Muestra 30.9 y luego None

#Función que devuelve un valor
def suma_decimales(a: float, b: float) -> float:
    return a + b

suma = suma_decimales(10.5, 20.4)
print(type(suma))  # <class 'float'>

#Docstring en función
def par_impar(numero):
    """
    Solicita un número al usuario con input().
    Lo transforma a tipo int.
    Indica si el número es par o impar.
    """
    numero = int(numero)
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

par_impar(7)
print(par_impar.__doc__)
help(par_impar)

#Docstrings en módulo, clase, método y función
"""Docstring del módulo"""

class Clase:
    """Docstring de la clase"""

    def metodo(self):
        """Docstring del método"""
        pass

def funcion():
    """Docstring de la función"""
    pass

#Acceder a documentación interna
print(int.__doc__)         # Muestra ayuda de int
print(par_impar.__doc__)   # Muestra docstring de la función
help(int)                  # Muestra ayuda completa en consola
help(par_impar)            # Muestra ayuda de la función definida