#El parámetro self de Python para principiantes

'''
¿Qué es self?
Es el primer parámetro obligatorio en todos los métodos de instancia.
Representa al objeto actual que llama al método.
Permite acceder a los atributos y otros métodos del mismo objeto.
Aunque puedes cambiarle el nombre, usar self es una convención universal en Python.

¿Por qué es necesario?
Sin self, los métodos no sabrían a qué instancia se están aplicando.
Python lo pasa automáticamente cuando llamas a un método desde un objeto.
'''
#Definimos una clase con atributos y métodos que usan self
class Usuario:
    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        # Atributos de instancia
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    # Método que usa self para acceder al atributo nombre
    def iniciar_sesion(self):
        print(f"El usuario {self.nombre} ha iniciado sesión.")

    # Otro método que usa self
    def cerrar_sesion(self):
        print(f"El usuario {self.nombre} ha cerrado sesión.")

    # Método que simula cambiar el nombre del perfil
    def cambiar_nombre_perfil(self, nuevo_nombre):
        print(f"Nombre anterior: {self.nombre}")
        self.nombre = nuevo_nombre
        print(f"Nuevo nombre: {self.nombre}")

#Creamos dos objetos distintos de la clase Usuario
usuario_1 = Usuario("Enrique", "Barros Fernández", 32, "C/Programación Fácil n.º 34", "123456789")
usuario_2 = Usuario("Adriana", "Barca López", 28, "Sin dirección", "987654321")

#Llamamos a los métodos usando self implícitamente
usuario_1.iniciar_sesion()  # Salida: El usuario Enrique ha iniciado sesión.
usuario_2.iniciar_sesion()  # Salida: El usuario Adriana ha iniciado sesión.

#Cambiamos el nombre de usuario_1
usuario_1.cambiar_nombre_perfil("Quique")  # Actualiza el atributo nombre

#Cerramos sesión
usuario_1.cerrar_sesion()
usuario_2.cerrar_sesion()

#Guía completa de herencia en clases de Python para principiantes, Lección 7

'''
¿Qué es la herencia?
Permite que una clase (subclase) herede atributos y métodos de otra clase (superclase), evitando repetir código.
¿Qué es super()?
Es una función que permite acceder a métodos de la superclase desde la subclase, especialmente útil para reutilizar el constructor __init__.
'''
#Ejemplo:

#Superclase: Ciudadano
class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion

    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesión es {self.profesion}.")

#Subclase: Medico que hereda de Ciudadano usando super()
class Medico(Ciudadano):
    def __init__(self, nombre):
        # Reutilizamos el constructor de Ciudadano y fijamos la profesión
        super().__init__(nombre, "médico")

#Subclase: MedicoEspecialista con profesión personalizada
class MedicoEspecialista(Ciudadano):
    def __init__(self, nombre, especialidad):
        # Usamos super() para pasar nombre y especialidad como profesión
        super().__init__(nombre, especialidad)

#Subclase: MedicoSinSuper sin usar super()
class MedicoSinSuper(Ciudadano):
    pass  # Hereda todo sin modificar el constructor

#Subclase: Policia que también hereda de Ciudadano
class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "policía")

#Instanciamos objetos de cada clase
persona1 = Ciudadano("Julia", "informática")
persona2 = Medico("Raúl")
persona3 = MedicoEspecialista("Carlos", "cirujano")
persona4 = MedicoSinSuper("Ana", "médico")
persona5 = Policia("Raquel")

#Usamos el método heredado saludar()
print("\n--- Saludos ---")
persona1.saludar()  # Hola, soy Julia. Mi profesión es informática.
persona2.saludar()  # Hola, soy Raúl. Mi profesión es médico.
persona3.saludar()  # Hola, soy Carlos. Mi profesión es cirujano.
persona4.saludar()  # Hola, soy Ana. Mi profesión es médico.
persona5.saludar()  # Hola, soy Raquel. Mi profesión es policía.

#Guía completa de encapsulamiento en clases de Python para principiantes, Lección 8

'''
El encapsulamiento en la mayoría de los lenguajes de programación implica controlar el acceso a los atributos y métodos internos de una clase, utilizando diferentes niveles de visibilidad haciendo uso de modificadores de acceso. 
Mediante estos, controlamos los niveles de acceso, haciendo que ciertos detalles de implementación queden ocultos para el usuario. 
Así le facilitamos el uso y evitamos que haga cosas inesperadas.
'''
#Ejemplo:
#Clase con atributos públicos, protegidos y privados
class Usuario:
    def __init__(self, id, nombre, apellidos):
        self.id = id                  # Público
        self._nombre = nombre         # Protegido (convención)
        self.__apellidos = apellidos  # Privado (name mangling)

    def muestra_apellidos(self):
        # Método público para acceder al atributo privado
        print(f"Los apellidos son: {self.__apellidos}.")

# Instanciamos un objeto
usuario_1 = Usuario(1, "Enrique", "Barros Fernández")

# Acceso a atributos
print(usuario_1.id)           #Público: accesible desde fuera
print(usuario_1._nombre)      #Protegido: accesible pero no recomendado
# print(usuario_1.__apellidos)  #Privado: da error

# Acceso correcto al atributo privado mediante método
usuario_1.muestra_apellidos()

# Acceso forzado al atributo privado (name mangling)
print(usuario_1._Usuario__apellidos)  #Técnica no recomendada

#Herencia y acceso a atributos protegidos vs privados
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad             # Protegido
        self.__raza = "Desconocida"   # Privado

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def mostrar_edad(self):
        print(f"Tengo {self._edad} años.")  #Protegido: accesible desde subclase

    # def mostrar_raza(self):
    #     print(f"Soy de raza {self.__raza}")  #Error: atributo privado no accesible

perro_1 = Perro("Chester", 3, "Husky")
perro_1.mostrar_edad()

#Métodos privados y acceso controlado
class Persona:
    def __init__(self, nombre, edad, altura_cm):
        self.nombre = nombre
        self.edad = edad
        self.altura_cm = altura_cm

    def __calcular_altura_metros(self):  # Método privado
        return self.altura_cm / 100

    def obtener_altura_metros(self):     # Método público
        altura = self.__calcular_altura_metros()
        print(f"La altura de {self.nombre} es de {altura} metros.")

persona = Persona("Ana", 30, 170)
persona.obtener_altura_metros()
# persona.__calcular_altura_metros()  #Error: método privado

#Getters y Setters para atributos privados
class UsuarioConEdad:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.__edad = edad  # Privado

    def obtener_edad(self):  # Getter
        return self.__edad

    def establecer_edad(self, nueva_edad):  # Setter
        self.__edad = nueva_edad

usuario_2 = UsuarioConEdad(2, "Farid", 27)
print(usuario_2.obtener_edad())  # Salida: 27

usuario_2.establecer_edad(30)
print(usuario_2.obtener_edad())  # Salida: 30

#Polimorfismo para clases de Python explicado para principiantes, Lección 9

'''
¿Qué es?
Polimorfismo es la capacidad de un objeto o función de tomar diferentes formas o comportamientos según el contexto. 
En Python, esto se logra principalmente mediante:
Métodos sobrescritos en clases derivadas
Funciones que aceptan múltiples tipos
Uso de *args para manejar diferentes cantidades de argumentos
'''
#Ejemplo:

#Polimorfismo con función nativa len()
titulo = "Python: el poder de los objetos."
print(len(titulo))  # Salida: 32 (número de caracteres)

numeros = (10, 50, 345, 43)
print(len(numeros))  # Salida: 4 (elementos en la tupla)

usuario = {"nombre": "Enrique", "apellidos": "Barros Fernández"}
print(len(usuario))  # Salida: 2 (pares clave-valor)

#Polimorfismo en clases: sobrescritura de métodos
class Animal:
    def hablar(self):
        print("Soy un animal")

class Perro(Animal):
    def hablar(self):
        print("Woof!")

class Gato(Animal):
    def hablar(self):
        print("Meow!")

# Instanciamos objetos
animal = Animal()
perro = Perro()
gato = Gato()

# Cada objeto responde de forma distinta al mismo método
animal.hablar()  # Soy un animal
perro.hablar()   # Woof!
gato.hablar()    # Meow!

#Polimorfismo con funciones que aceptan distintos objetos
def dar_voz(objeto):
    objeto.hablar()

dar_voz(animal)  # Soy un animal
dar_voz(perro)   # Woof!
dar_voz(gato)    # Meow!

#Simulación de sobrecarga con parámetros opcionales
def multiplicacion(a, b, c=None, d=None):
    if c is not None:
        if d is not None:
            print(a * b * c * d)
        else:
            print(a * b * c)
    else:
        print(a * b)

multiplicacion(45, 34)           # 1530
multiplicacion(45, 34, 56)       # 85680
multiplicacion(10, 2, 3, 6)      # 360

#Mejor solución: uso de *args para sobrecarga flexible
def multiplicar(*numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    print(resultado)

multiplicar(2, 3)                # 6
multiplicar(2, 3, 4)             # 24
multiplicar(2, 3, 4, 5, 6)       # 720

#Abstracción para clases de Python explicado para principiantes, Lección 10

'''
¿Qué es?
La abstracción permite ocultar los detalles internos de una clase y mostrar solo lo esencial. Se enfoca en qué hace un objeto, no en cómo lo hace.

¿Cómo se implementa?
Usando el módulo abc (Abstract Base Class)
Decorador @abstractmethod para declarar métodos obligatorios
Las clases abstractas no pueden ser instanciadas directamente
Las subclases deben implementar todos los métodos abstractos
'''
#Ejemplo:

#Importamos las herramientas para crear clases abstractas
from abc import ABC, abstractmethod

#Clase abstracta: no puede ser instanciada directamente
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass  # Método abstracto: sin implementación

#Subclase que implementa el método abstracto
class Perro(Animal):
    def hablar(self):
        print("Woof!")

#Otra subclase que también implementa el método
class Gato(Animal):
    def hablar(self):
        print("Meow!")

#Instanciamos objetos de las subclases
perro = Perro()
gato = Gato()

#Llamamos al método implementado
perro.hablar()  # Salida: Woof!
gato.hablar()   # Salida: Meow!

#Error: subclase sin implementar el método abstracto
class PerroSinHablar(Animal):
    def correr(self):
        print("Ha empezado a correr.")

#perro_error = PerroSinHablar()  # TypeError: Can't instantiate abstract class

#Error: intentar instanciar directamente la clase abstracta
#animal = Animal()  # TypeError: Can't instantiate abstract class Animal

