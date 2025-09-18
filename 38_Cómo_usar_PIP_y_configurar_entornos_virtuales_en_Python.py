#Cómo usar PIP y configurar entornos virtuales en Python

'''
¿Qué es PIP?
Es el gestor de paquetes oficial de Python. Permite instalar bibliotecas, frameworks y módulos externos fácilmente.
¿Qué es un entorno virtual?
Es un espacio aislado donde puedes instalar paquetes sin afectar el sistema global. Ideal para mantener proyectos independientes y organizados.

pip --version
# Muestra la versión instalada de PIP

pip install numpy
# Instala NumPy en el entorno global

pip freeze
# Lista todos los paquetes instalados con sus versiones

pip install numpy --upgrade
# Actualiza NumPy a la última versión

pip uninstall numpy
# Elimina NumPy del entorno actual

import numpy as np

a = np.array([1, 2, 3])
print("Array:", a)

python -m venv entorno_de_pruebas
# Crea un entorno virtual llamado entorno_de_pruebas

entorno_de_pruebas\Scripts\activate

source entorno_de_pruebas/bin/activate

pip install pygame
# Instala Pygame solo en el entorno virtual activo

pip freeze
# Ejemplo: pygame==2.6.0

deactivate
# Sale del entorno virtual y vuelve al entorno global

# Solo borra la carpeta del entorno virtual
# Ejemplo: eliminar la carpeta entorno_de_pruebas/

python -m pip install --upgrade pip
# Actualiza PIP a la última versión disponible

# Supón que pygame está instalado
import pygame

pygame.init()
print("Pygame inicializado correctamente.")

pip freeze > requirements.txt
# Guarda los paquetes instalados en un archivo para compartir o replicar el entorno

pip install -r requirements.txt
# Instala todos los paquetes listados en el archivo
'''
#Todo esto solo son los comandos/codigos para poder realizar esta leccion, todos funcionan correctamente.