#Herencia de clases con Python - Superclases y subclases

'''
La herencia en Python permite que una clase (subclase) herede atributos y métodos de otra clase (superclase). Esto evita duplicación de código y facilita la organización.
Superclase:
Es la clase base que contiene atributos y métodos comunes.
Subclase:
Hereda de la superclase.
Puede sobrescribir atributos o métodos si necesita comportamientos distintos.
Ventajas:
Reutilización de código.
Jerarquía clara entre clases.
Mantenimiento más sencillo
'''
#Superclase: Usuarios
class Usuarios:
    # Atributos de clase (compartidos por todas las instancias)
    tipo_usuario = "Free"
    publicidad = True

    # Constructor (__init__) con atributos obligatorios
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


#Subclase: UsuariosPremium que hereda de Usuarios
class UsuariosPremium(Usuarios):
    # Sobrescribimos los atributos de clase
    tipo_usuario = "Premium"
    publicidad = False
    # No es necesario redefinir __init__ ni muestra_datos si no cambian


#Crear un objeto de la clase Usuarios
usuario1 = Usuarios("001", "raulito43", "Raúl", "Fernández Gomila")

#Usar el método heredado para mostrar datos
usuario1.muestra_datos()

#Mostrar el tipo de usuario (atributo de clase)
print("Tipo de usuario:", usuario1.tipo_usuario)  # Salida: Free
print("¿Tiene publicidad?", usuario1.publicidad)  # Salida: True


#Crear un objeto de la subclase UsuariosPremium
usuario2 = UsuariosPremium("002", "paula_dev", "Paula", "Bravo Rojas")

#Usar el método heredado para mostrar datos
usuario2.muestra_datos()

#Mostrar el tipo de usuario (atributo sobrescrito)
print("Tipo de usuario:", usuario2.tipo_usuario)  # Salida: Premium
print("¿Tiene publicidad?", usuario2.publicidad)  # Salida: False
