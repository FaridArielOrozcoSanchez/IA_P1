#Todo Sobre Funciones en Python: def, lambda, decoradores y generadores

'''
¿Qué es una función?
Un bloque de código reutilizable que se ejecuta cuando se llama. Puede recibir parámetros y devolver valores.
'''

#Función básica
def saludar():
    print("Hola, Farid!")

saludar()


#Función con parámetros y retorno
def sumar(a, b):
    return a + b

print("Suma:", sumar(10, 5))


#Parámetros por defecto
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()
saludar("Farid")


#Argumentos posicionales y de clave
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años.")

presentar("Farid", 27)
presentar(edad=27, nombre="Farid")


#*args: argumentos arbitrarios posicionales
def listar_valores(*args):
    print("Valores:", args)

listar_valores(1, 2, 3, "Farid")


#**kwargs: argumentos arbitrarios de clave
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Farid", edad=27)


#Función lambda
multiplicar = lambda x, y: x * y
print("Multiplicación:", multiplicar(3, 4))


#Uso de lambda con map()
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)


#Decorador básico
def decorador(func):
    def interna():
        print("Inicio")
        func()
        print("Fin")
    return interna

@decorador
def mensaje():
    print("Función decorada")

mensaje()


#Decorador con *args y **kwargs
def decorador(func):
    def interna(*args, **kwargs):
        print("Inicio")
        func(*args, **kwargs)
        print("Fin")
    return interna

@decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Farid")


#Función generadora con yield
def generadora():
    for i in range(3):
        yield i

gen = generadora()
print(next(gen))
print(next(gen))
print(next(gen))


#Generadora con lógica condicional
def pares_impares():
    for i in range(5):
        yield f"{i} - par" if i % 2 == 0 else f"{i} - impar"

for valor in pares_impares():
    print(valor)


#Convertir generador en lista
def generadora():
    for i in range(5):
        yield i * 2

lista = list(generadora())
print("Lista generada:", lista)
