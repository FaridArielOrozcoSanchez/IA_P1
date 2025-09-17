#Herencia de clases con Python - cómo utilizar super()

'''
¿Qué es la herencia?
La herencia permite que una clase (subclase) tome atributos y métodos de otra clase (superclase). Esto evita repetir código y facilita la organización.

¿Qué hace super()?
Llama al constructor (__init__) de la superclase desde una subclase.
Permite extender el comportamiento sin sobrescribir completamente el método original.
Es útil cuando quieres añadir atributos nuevos sin perder los heredados.
'''

#Superclase: Usuarios
class Usuarios:
    # Atributos de clase (compartidos por todas las instancias)
    tipo_usuario = "Free"
    publicidad = True

    # Constructor con atributos obligatorios
    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid                # ID del usuario
        self.alias = alias            # Alias del usuario
        self.nombre = nombre          # Nombre del usuario
        self.apellidos = apellidos    # Apellidos del usuario

    # Método para mostrar los datos del usuario
    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son:", self.nombre, self.apellidos)
        print("El ID de usuario es:", self.nid + ".")
        print("El alias del usuario es:", self.alias + ".")

#Subclase: UsuariosPremium hereda de Usuarios
class UsuariosPremium(Usuarios):
    # Atributos de clase sobrescritos
    tipo_usuario = "Premium"
    publicidad = False
    participacion_sorteos = 10  # Atributo adicional

    # Constructor que extiende el de la superclase usando super()
    def __init__(self, nid, alias, nombre, apellidos, participacion_sorteos, puntos_premios):
        # Atributos nuevos de la subclase
        self.participacion_sorteos = participacion_sorteos
        self.puntos_premios = puntos_premios
        self.contenido_premium = True

        # Llamamos al constructor de la superclase para inicializar sus atributos
        super().__init__(nid, alias, nombre, apellidos)

#Subclase: UsuariosPremiumPlus hereda de UsuariosPremium
class UsuariosPremiumPlus(UsuariosPremium):
    # Sobrescribimos el atributo de sorteos
    participacion_sorteos = 25
    # Hereda todo lo demás sin necesidad de redefinir __init__

# Crear objeto de la clase base Usuarios
usuario1 = Usuarios("001", "raulito43", "Raúl", "Fernández Gomila")
usuario1.muestra_datos()
print("Tipo de usuario:", usuario1.tipo_usuario)      # Free
print("¿Tiene publicidad?", usuario1.publicidad)      # True

#Crear objeto de la subclase UsuariosPremium
usuario2 = UsuariosPremium("002", "paula_dev", "Paula", "Bravo Rojas", 10, 150)
usuario2.muestra_datos()
print("Tipo de usuario:", usuario2.tipo_usuario)       # Premium
print("¿Tiene publicidad?", usuario2.publicidad)       # False
print("Sorteos:", usuario2.participacion_sorteos)      # 10
print("Puntos:", usuario2.puntos_premios)              # 150
print("¿Tiene contenido premium?", usuario2.contenido_premium)  # True

#Crear objeto de la subclase UsuariosPremiumPlus
usuario3 = UsuariosPremiumPlus("003", "super_paula", "Paula", "Bravo Rojas", 25, 300)
usuario3.muestra_datos()
print("Tipo de usuario:", usuario3.tipo_usuario)       # Premium
print("Sorteos:", usuario3.participacion_sorteos)      # 25
print("Puntos:", usuario3.puntos_premios)              # 300