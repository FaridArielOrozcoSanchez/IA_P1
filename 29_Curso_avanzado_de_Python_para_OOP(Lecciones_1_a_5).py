#Curso avanzado de Python para OOP, programación modular y defensiva, Lección 1

'''
Los temas principales que voy a tratar son estos:
1.-Programación orientada a objetos
Introducción a la programación orientada a objetos
Clases
Objetos
El método __init__ y el uso de self en clases
Herencia de clases
Encapsulamiento
Polimorfismo
Abstracción

2.-Programación modular
Introducción a la programación modular
Importación y uso de módulos
Creación de módulos
Espacios de nombres y el ámbito
Paquetes
Trabajando con módulos integrados
PIP y entornos virtuales
Introducción a las funciones
Argumentos
Funciones lambda
Funciones decoradoras
Funciones generadoras e iteradores

3.-Programación defensiva y depuración
Introducción a la programación defensiva
Depuración de errores
Errores y excepciones
Tipos de excepciones
try, except y finally
Errores en tiempo de edición
La validación de datos
El uso de afirmaciones
Lanzar excepciones
Documentación
'''

#Introducción a la programación orientada a objetos con Python, Lección 2

'''
¿Qué es la programación orientada a objetos?
La programación orientada a objetos es una parte importante tanto de Python como de muchos otros lenguajes de programación modernos. 
Dominar este tema se ha vuelto un requisito imprescindible en el mundo del desarrollo.

Conceptos de POO que vas a aprender en este curso
A lo largo de esta primera parte del curso, aprenderás los siguientes conceptos relacionados con la programación orientada a objetos, y alguno más:
Clases
Objetos
Encapsulamiento
Polimorfismo
Herencia
Abstracción
'''

#Introducción a las clases en Python: Aprende desde cero con ejemplos prácticos, Lección 3

'''
¿Qué es una clase?
Una clase es una plantilla que define atributos (datos) y métodos (acciones) para crear objetos. Es la base de la Programación Orientada a Objetos (POO).

Sintaxis básica:
class NombreClase:
    # Atributos
    atributo_1 = "valor"
    
    # Métodos
    def metodo_1(self):
        print("Método ejecutado")

Se usa la palabra clave class.
Los nombres de clase siguen la convención CapWords (Ej. VehiculoTerrestre).
Los métodos deben incluir self como primer parámetro.
'''

#Ejemplos:

#Ejemplo 1: Clase vacía con pass
class Vehiculo:
    pass  # Se usa para evitar errores de indentación mientras se define la estructura

# Se puede crear un objeto aunque la clase esté vacía
auto = Vehiculo()

#Ejemplo 2: Clase con atributos
class Vehiculo:
    color = None              # Atributo sin valor inicial
    longitud_metros = None    # Atributo sin valor inicial
    ruedas = 4                # Atributo con valor por defecto

# Crear objeto y acceder a atributos
auto = Vehiculo()
print(auto.ruedas)  # Salida: 4

#Ejemplo 3: Clase con métodos
class Vehiculo:
    color = None
    longitud_metros = None
    ruedas = 4

    def arrancar(self):
        print("El motor ha arrancado.")

    def detener(self):
        print("El motor está detenido.")

# Crear objeto y ejecutar métodos
auto = Vehiculo()
auto.arrancar()  # Salida: El motor ha arrancado.
auto.detener()   # Salida: El motor está detenido.

#Ejemplo 4: Uso de type() para ver la clase de un objeto
texto = "Python: El creador de los buenos juegos XD."
print(type(texto))  # Salida: <class 'str'>
print(texto.upper())  # Salida: PYTHON: EL PODER DE LOS OBJETOS.

#Objetos en Python: aprende los conceptos esenciales de OOP, Lección 4

'''
¿Qué es un objeto?
Un objeto es una instancia de una clase. 
Tiene:
Estado: representado por sus atributos.
Comportamiento: definido por sus métodos.
Identidad: el nombre o referencia que lo identifica en memoria.

¿Cómo se crea?
class NombreClase:
    pass

objeto = NombreClase()
'''

#Ejemplo:

#Definimos la clase Vehiculo
class Vehiculo:
    # Atributos de clase (estado inicial)
    color = None
    longitud_metros = None
    ruedas = 4
    velocidad_maxima = 0  # Se añade para evitar errores si se usa en todos los objetos

    # Métodos (comportamiento)
    def arrancar(self):
        print("El motor ha arrancado.")

    def detener(self):
        print("El motor está detenido.")

#Instanciamos dos objetos de la clase Vehiculo
objeto_vehiculo_1 = Vehiculo()
objeto_vehiculo_2 = Vehiculo()

#Accedemos a un atributo compartido
print(objeto_vehiculo_1.ruedas)  # Salida: 4

#Reasignamos atributos para personalizar cada objeto
objeto_vehiculo_1.color = "Negro"
objeto_vehiculo_2.color = "Azul"

print(objeto_vehiculo_1.color)  # Salida: Negro
print(objeto_vehiculo_2.color)  # Salida: Azul

#Creamos un atributo único para un solo objeto
objeto_vehiculo_1.velocidad_maxima = 161
print(objeto_vehiculo_1.velocidad_maxima)  # Salida: 161

#Este atributo no existe en objeto_vehiculo_2 si no se ha definido
# print(objeto_vehiculo_2.velocidad_maxima)  # Error: AttributeError

#Si el atributo está definido en la clase, todos los objetos lo tienen
print(objeto_vehiculo_2.velocidad_maxima)  # Salida: 0

#Llamamos a métodos del objeto
objeto_vehiculo_1.arrancar()  # Salida: El motor ha arrancado.
objeto_vehiculo_1.detener()   # Salida: El motor está detenido.

#Imprimimos la identidad del objeto (dirección en memoria)
print(objeto_vehiculo_1)  # Ejemplo: <__main__.Vehiculo object at 0x0000028226985BB0>
print(objeto_vehiculo_2)  # Ejemplo: <__main__.Vehiculo object at 0x0000028226985C10>

#Accedemos a un atributo y lo almacenamos en una variable
ruedas_vehiculo = objeto_vehiculo_1.ruedas
print(ruedas_vehiculo)  # Salida: 4

#El método __init__ de Python para principiantes, Lección 5

'''
¿Qué es?
Es el constructor de una clase.
Se ejecuta automáticamente al crear un objeto.
Permite inicializar atributos de instancia con valores personalizados.

Sintaxis
class Clase:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2
self representa el objeto actual.
Los parámetros se asignan a los atributos del objeto.
'''

#Ejemplo:

#Clase sin __init__: inicialización manual
class UsuarioManual:
    # Atributos de clase con valores por defecto
    nombre = "Sin nombre"
    apellidos = "Sin apellidos"
    edad = 0
    direccion = "Sin dirección"
    telefono = "Sin teléfono"

    def iniciar_sesion(self):
        print("El usuario ha iniciado sesión")

#Crear objeto y asignar atributos manualmente
usuario_m = UsuarioManual()
usuario_m.nombre = "Enrique"
usuario_m.apellidos = "Barros Fernández"
usuario_m.edad = 32
usuario_m.direccion = "C/Programación Fácil n.º 34"
usuario_m.telefono = "123456789"
print("Usuario manual:", usuario_m.nombre, usuario_m.telefono)


#Clase con __init__: inicialización automática
class Usuario:
    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def iniciar_sesion(self):
        print("El usuario ha iniciado sesión")

# Crear objeto con datos iniciales
usuario_1 = Usuario("Enrique", "Barros Fernández", 32, "C/Programación Fácil n.º 34", "123456789")
print("Usuario 1:", usuario_1.nombre, usuario_1.telefono)


#Uso de argumentos por clave (orden flexible)
usuario_2 = Usuario(
    apellidos="Barros Fernández",
    edad=32,
    direccion="C/Programación Fácil n.º 34",
    telefono="123456789",
    nombre="Enrique"
)
print("Usuario 2:", usuario_2.nombre, usuario_2.direccion)


#Atributos de clase junto a atributos de instancia
class UsuarioConClase:
    hora_ultimo_inicio = None  # Atributo de clase

    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

# Crear objeto y modificar atributos
usuario_3 = UsuarioConClase("Enrique", "Barros Fernández", 32, "C/Programación Fácil n.º 34", "123456709")
usuario_3.nombre = "Quique"  # Reasignación de atributo de instancia
usuario_3.hora_ultimo_inicio = "20/12/2025"  # Reasignación de atributo de clase
print("Usuario 3:", usuario_3.nombre, usuario_3.hora_ultimo_inicio)


#Diferencia entre nombres de parámetros y atributos
class UsuarioParam:
    def __init__(self, p1, p2, p3, p4, p5):
        self.a1 = p1
        self.a2 = p2
        self.a3 = p3
        self.a4 = p4
        self.a5 = p5

usuario_4 = UsuarioParam("Farid", "Orozco", 27, "México", "3314150405")
print("Usuario 4:", usuario_4.a1, usuario_4.a5)


#Valores por defecto en atributos de instancia
class UsuarioPorDefecto:
    def __init__(self, nombre, apellidos, edad, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
        self.direccion = "Sin dirección"  # Valor por defecto

usuario_5 = UsuarioPorDefecto("Farid", "Orozco", 27, "5551234567")
print("Usuario 5:", usuario_5.nombre, usuario_5.direccion)
