#Atributos obligatorios en clases de Python

'''
__init__ es el método constructor que se ejecuta automáticamente al crear un objeto.
self representa al objeto actual y permite acceder a sus atributos y métodos.
Al usar __init__, puedes exigir que ciertos valores se proporcionen al instanciar la clase.
Esto evita objetos incompletos y hace tu código más robusto.
Puedes añadir atributos personalizados a objetos individuales si lo necesitas.
'''

#Ejemplo 1: Clase sin constructor __init__
# Se definen atributos directamente en la clase, con valores por defecto
class NinjaPrincipal:
    HP = 100            # Puntos de vida
    resistencia = 50    # Energía
    XP = 1              # Experiencia

    # Método que se ejecuta cuando el personaje pierde toda la vida
    def game_over(self):
        print("Game over")

# Se crean dos objetos a partir de la misma clase
ninja = NinjaPrincipal()
ninja_enemigo = NinjaPrincipal()

# Se modifica el atributo HP del objeto enemigo
ninja_enemigo.HP = 25

# Se imprime el nuevo valor de HP del enemigo
print(ninja_enemigo.HP)  # Salida: 25


#Ejemplo 2: Clase con constructor __init__ y uso de self
#Se definen atributos obligatorios que deben pasarse al crear el objeto
class Ninjas:
    def __init__(self, hp, resistencia, xp, vidas):
        self.hp = hp                # Puntos de vida
        self.resistencia = resistencia  # Energía
        self.xp = xp                # Experiencia
        self.vidas = vidas          # Número de vidas

    # Método que se ejecuta si el personaje pierde toda la vida
    def game_over(self):
        print("Game over")

# Se crea un objeto con valores personalizados
ninja_principal = Ninjas(100, 50, 1, 3)

# Se accede a los atributos del objeto
print(ninja_principal.hp)     # Salida: 100
print(ninja_principal.vidas)  # Salida: 3


#Ejemplo 3: Añadir atributo personalizado a un solo objeto
#Se puede agregar un atributo extra solo a un objeto específico
ninja_principal.salto = True

# Se imprime el nuevo atributo
print(ninja_principal.salto)  # Salida: True

# Se crea otro objeto sin el atributo 'salto'
otro_ninja = Ninjas(80, 40, 2, 2)

# Este objeto no tiene el atributo 'salto' por defecto
# Si intentamos acceder a 'salto' en otro_ninja, dará error si no lo hemos definido
# print(otro_ninja.salto)  # AttributeError si se descomenta
