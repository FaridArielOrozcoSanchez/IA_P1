#Atributos y Métodos en Clases (Python)
'''
En la Programación Orientada a Objetos (POO), los objetos tienen:

Atributos
Son las propiedades o características del objeto.
Se definen dentro de la clase y pueden tener cualquier tipo de dato.
Es recomendable usar nombres descriptivos (como color, tipo, precio) en lugar de letras genéricas (x, y, z).

Métodos
Son funciones que pertenecen a una clase.
Definen comportamientos o acciones que el objeto puede realizar.
Se escriben como funciones dentro de la clase y siempre reciben self como primer parámetro.

Ventajas
Permiten modelar elementos del mundo real.
Facilitan la reutilización y organización del código.
Cada objeto puede tener valores únicos para sus atributos.
'''

#Ejemplos

# Definimos una clase llamada NinjaPrincipal
class NinjaPrincipal:
    # Atributo: puntos de vida del personaje
    hp = 100
    # Atributo: resistencia física del personaje
    resistencia = 50
    # Atributo: experiencia del personaje
    xp = 1
    # Método: se ejecuta cuando el personaje pierde toda la vida
    def game_over(self):
        print("Game over")


# Creamos un objeto llamado ninja a partir de la clase NinjaPrincipal
ninja = NinjaPrincipal()

# Mostramos el valor actual del atributo hp del objeto ninja
print(ninja.hp)  # Salida: 100

# Cambiamos el valor del atributo hp del objeto ninja a 0
ninja.hp = 0

# Verificamos si el hp del ninja es 0
if ninja.hp == 0:
    # Si la condición se cumple, se ejecuta el método game_over()
    ninja.game_over()  # Salida: Game over
