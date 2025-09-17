#Herencia de clases Python en diferentes archivos

'''
¿Qué es?
La herencia permite que una clase hija (subclase) herede atributos y métodos de una clase padre (superclase). Al distribuir las clases en distintos archivos, puedes mantener tu código limpio y reutilizable.

¿Cómo se organiza?
Archivo b.py: contiene la clase base Usuarios.
Archivo c.py: define la clase UsuariosPremium, que hereda de Usuarios.
Archivo d.py: define la clase UsuariosPremiumPlus, que hereda de UsuariosPremium.
Archivo a.py: importa las clases anteriores y crea objetos para usarlos.
'''
#Pase a abrir los archivos b.py, c.py, d.py y a.py para revisar la leccion