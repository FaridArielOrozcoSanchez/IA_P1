# Clase base con atributos comunes
class Usuarios:
    tipo_usuario = "Free"       # Atributo de clase
    publicidad = True           # Atributo de clase

    def __init__(self, nid, alias, nombre, apellidos):
        # Atributos de instancia
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestra_datos(self):
        # Método para mostrar información del usuario
        print("El nombre y los apellidos del usuario son:", self.nombre, self.apellidos)
        print("El ID de usuario es:", self.nid + ".")
        print("El alias del usuario es:", self.alias + ".")
