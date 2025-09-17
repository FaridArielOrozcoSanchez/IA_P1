#Utilización de *args en las clases de Python

'''
Atributos de clase:
Se definen fuera del método __init__.
Son compartidos por todas las instancias de la clase.
Se pueden acceder directamente desde la clase o desde un objeto.
Atributos de instancia:
Se definen dentro del método __init__.
Son únicos para cada objeto creado.
Método vs Función:
Una función es independiente.
Un método es una función que pertenece a una clase y siempre recibe self como primer parámetro.
Uso de *args en clases:
Permite pasar un número indefinido de argumentos al constructor.
Se almacenan como una tupla en el atributo que tú definas (por ejemplo, self.args).
'''

#Definimos una clase con atributos de clase y atributos de instancia
class Usuarios:
    # Atributos de clase: compartidos por todos los objetos
    tipo_usuario = "Free"
    publicidad = True

    # Constructor con atributos obligatorios y *args para adicionales
    def __init__(self, nid, alias, nombre, apellidos, *args):
        # Atributos de instancia: únicos por objeto
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos
        self.args = args  # Almacena argumentos adicionales como tupla

#Crear un objeto con argumentos obligatorios y adicionales
usuario1 = Usuarios(
    "001", "PdePython", "Paula", "Bravo Rojas",
    "Persona estudiosa", "Amante del lenguaje de programación Python", "27"
)

#imprimir atributos de clase
print(usuario1.tipo_usuario)  # Salida: Free

#Modificar atributo de clase desde el objeto
usuario1.tipo_usuario = "Premium"
print(usuario1.tipo_usuario)  # Salida: Premium

#Acceder al atributo de clase directamente desde la clase
print(Usuarios.publicidad)  # Salida: True

#Imprimir los argumentos adicionales almacenados en *args
print(usuario1.args)
# Salida: ('Persona estudiosa', 'Amante del lenguaje de programación Python', '27')
