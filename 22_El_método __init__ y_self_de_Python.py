#__init__ y self en Python

'''
En la Programación Orientada a Objetos (POO), el método __init__ es el constructor de una clase. Se ejecuta automáticamente al crear un nuevo objeto y sirve para inicializar sus atributos.
__init__(self, ...): define los valores iniciales del objeto.
self: representa al objeto mismo. Permite acceder y modificar sus atributos desde dentro de la clase.
Usar __init__ evita tener que asignar atributos manualmente cada vez que se crea un objeto.
Puedes añadir atributos personalizados a objetos específicos después de crearlos.
'''

#Ejemplo 1: Clase sin constructor __init__
#Se definen atributos directamente en la clase
class NinjaPrincipal:
    HP = 100            # Puntos de vida por defecto
    resistencia = 50    # Energía por defecto
    XP = 1              # Nivel de experiencia por defecto

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
#Se define una clase más flexible que permite inicializar atributos al crear el objeto
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


#Ejemplo 3: Añadir atributos personalizados a un solo objeto
#Se puede agregar un atributo extra solo a un objeto específico
ninja_principal.salto = True

# Se imprime el nuevo atributo
print(ninja_principal.salto)  # Salida: True

# Se crea otro objeto sin el atributo 'salto'
otro_ninja = Ninjas(80, 40, 2, 2)

# Si intentamos acceder a 'salto' en otro_ninja, dará error si no lo hemos definido
# print(otro_ninja.salto)  # Esto causaría AttributeError si se descomenta
