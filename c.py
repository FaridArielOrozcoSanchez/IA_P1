import b  # Importamos la clase Usuarios desde b.py

# Clase que hereda de Usuarios y añade nuevos atributos
class UsuariosPremium(b.Usuarios):
    tipo_usuario = "Premium"
    publicidad = False
    participacion_sorteos = 10

    def __init__(self, nid, alias, nombre, apellidos, participacion_sorteos, puntos_premios):
        # Nuevos atributos específicos de UsuariosPremium
        self.participacion_sorteos = participacion_sorteos
        self.puntos_premios = puntos_premios
        self.contenido_premium = True

        # Llamamos al constructor de la clase padre
        super().__init__(nid, alias, nombre, apellidos)

    def muestra_datos(self):
        # Extendemos el método heredado
        super().muestra_datos()
        print("Tienes", self.puntos_premios, "puntos para canjear en premios.")
        print("Tienes", self.participacion_sorteos, "puntos para participar en sorteos.")
