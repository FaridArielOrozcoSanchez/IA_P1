#Crea tus propios módulos con Python

'''
¿Qué es un módulo?
Un módulo es un archivo .py que contiene funciones, clases o variables que puedes reutilizar en otros programas.

¿Cómo se crea?
Solo necesitas escribir código Python en un archivo .py. Luego puedes importarlo desde otro archivo que esté en la misma carpeta.
'''
#Ejemplo

'''
Utilizaremos 2 archivos:
suma.py
Este mismo
'''
#Importamos el módulo suma
import suma

#Usamos la función sumar del módulo
resultado = suma.sumar(10, 22)

#Mostramos el resultado
print("Resultado de la suma:", resultado)  # Salida: 32
'''
Variaciones de importacion
#Importar solo la función sumar
from suma import sumar

print("Suma directa:", sumar(5, 7))  # Salida: 12
#Importar con alias
import suma as s

print("Suma con alias:", s.sumar(3, 4))  # Salida: 7
'''