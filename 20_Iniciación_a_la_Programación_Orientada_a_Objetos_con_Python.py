#Programación Orientada a Objetos con Python

'''
La POO permite modelar elementos del mundo real como objetos dentro del código. Cada objeto tiene:
Atributos: características o propiedades (como color, tamaño, nombre).
Métodos: acciones o comportamientos que puede realizar (como saltar, comprar, atacar).

Clases y Objetos
Una clase es el molde que define los atributos y métodos.
Un objeto es una instancia de una clase, con sus propios valores.

Ventajas
Reutilización de código.
Organización clara.
Escalabilidad para proyectos grandes.
'''

#Ejemplos

#Crear una clase vacía
class Personaje:
    pass
# Crear un objeto
protagonista = Personaje()

#Clase con atributos y método
class Personaje:
    def __init__(self, nombre, fuerza):
        self.nombre = nombre
        self.fuerza = fuerza

    def atacar(self):
        print(f"{self.nombre} ataca con fuerza {self.fuerza}!")
# Crear objeto
heroe = Personaje("Farid", 80)
heroe.atacar()

#Clase con múltiples objetos
class Producto:
    def __init__(self, nombre, color, tipo):
        self.nombre = nombre
        self.color = color
        self.tipo = tipo
# Crear objetos
p1 = Producto("Pantalón", "Negro", "Sport")
p2 = Producto("Pantalón", "Blanco", "Sport")

print(p1.color)  # Negro
print(p2.color)  # Blanco

#Ventaja de usar clases vs funciones
# Sin clases: funciones repetidas
def crear_pantalon_negro():
    return {"color": "Negro", "tipo": "Sport"}

def crear_pantalon_blanco():
    return {"color": "Blanco", "tipo": "Sport"}

# Con clase: más limpio
class Pantalon:
    def __init__(self, color, tipo):
        self.color = color
        self.tipo = tipo

p1 = Pantalon("Negro", "Sport")
p2 = Pantalon("Blanco", "Sport")

