import c  # Importamos UsuariosPremium desde c.py

# Clase que hereda de UsuariosPremium y sobrescribe atributos
class UsuariosPremiumPlus(c.UsuariosPremium):
    participacion_sorteos = 25  # Atributo sobrescrito

    def muestra_datos(self):
        # Extendemos el método heredado
        super().muestra_datos()
        print("El tipo de usuario es:", c.UsuariosPremium.tipo_usuario)
