#¿Qué es el Encapsulamiento? - Atributos privados

'''
¿Qué es el encapsulamiento?
Es una técnica que permite ocultar atributos o métodos de una clase para que no puedan ser accedidos directamente desde fuera. 
Esto protege la integridad de los datos y obliga a usar métodos definidos para interactuar con ellos.

¿Cómo se implementa?
Se antepone doble guion bajo (__) al nombre del atributo para hacerlo privado.
Los atributos privados solo pueden usarse dentro de la clase.
Para acceder o modificar estos atributos desde fuera, se deben crear métodos públicos dentro de la clase.
'''

#Definimos una clase llamada Usuarios
class Usuarios:
    # Constructor con atributos públicos y uno privado
    def __init__(self, nid, alias, nombre, apellidos, password):
        self.nid = nid                  # ID del usuario (público)
        self.alias = alias              # Alias del usuario (público)
        self.nombre = nombre            # Nombre del usuario (público)
        self.apellidos = apellidos      # Apellidos del usuario (público)
        self.__password = password      # Contraseña (privado con doble guion bajo)

    # Método para mostrar los datos del usuario
    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son:", self.nombre, self.apellidos)
        print("El ID de usuario es:", self.nid + ".")
        print("El alias del usuario es:", self.alias + ".")
        print("La contraseña es:", self.__password)  # Acceso permitido dentro de la clase

#Creamos un objeto de la clase Usuarios
usuario1 = Usuarios("002", "PdePython", "Paula", "Vega García", "h$6pOcN9YDub")

#Llamamos al método para mostrar los datos
usuario1.muestra_datos()

#Intentar acceder directamente al atributo privado desde fuera de la clase
# print(usuario1.__password)  # Esto generaría un error: AttributeError

#Acceso indirecto (no recomendado, pero posible)
#print(usuario1._Usuarios__password)  # Esto funciona, pero rompe el encapsulamiento
