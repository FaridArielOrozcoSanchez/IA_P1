#Introducción a las funciones con Python

'''
Las funciones son bloques de código reutilizables que realizan tareas específicas. Se definen con def, pueden recibir datos (parámetros) y devolver resultados (return).
Conceptos clave
Definición: def nombre_funcion(parámetros):
Parámetros: Variables internas que reciben datos.
Argumentos: Valores que se pasan al llamar la función.
return: Devuelve un valor al programa.
Scope: Las variables dentro de una función no existen fuera de ella.
Tipos de argumentos:
Posicionales: Se pasan en orden.
De clave: Se especifica el nombre del parámetro.
'''

#Ejemplos

# Función sin parámetros
def saludar():
    nombre = input("Introduzca su nombre, por favor: ")
    print(f"¡Muy buenas, {nombre}!")

saludar()

# Función con un parámetro
def saludar(nombre):
    print(f"¡Muy buenas, {nombre}!")

saludar("Enrique")
saludar("Gabriela")
saludar("Javier")
saludar("María")

# Función con varios parámetros
def saludar(nombre, edad):
    print(f"¡Muy buenas, {nombre}!")
    print(f"Usted tiene {edad} años.")

saludar("Enrique", 32)

# Argumentos de clave (orden flexible)
def saludar(nombre, edad):
    print(f"¡Muy buenas, {nombre}!")
    print(f"Usted tiene {edad} años.")

saludar(nombre="Enrique", edad=32)
saludar(edad=32, nombre="Enrique")  # También válido

# Función que imprime la suma (no devuelve valor)
def suma(numero1, numero2):
    print(numero1 + numero2)

suma(10, 50)

# Función que devuelve la suma con return
def suma(numero1, numero2):
    return numero1 + numero2

resultado = suma(10, 50)
print(resultado)  # Imprime 60

# Función con print() y return juntos
def suma(numero1, numero2):
    print("Se va a calcular la suma...")
    return numero1 + numero2

resultado = suma(10, 50)
print(resultado)  # Imprime mensaje y resultado

