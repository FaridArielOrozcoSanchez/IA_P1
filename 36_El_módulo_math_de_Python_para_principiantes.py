#El módulo math de Python para principiantes

'''
¿Qué es?
Es un módulo integrado que proporciona funciones matemáticas avanzadas como raíces, potencias, trigonometría, logaritmos, constantes como π, etc.

¿Cómo se usa?
Primero debes importarlo:
'''
import math

'''Luego puedes acceder a sus funciones con la sintaxis math.función().'''

#Solicitamos un número al usuario
numero = int(input("Introduce un número: "))

#Calculamos la raíz cuadrada (devuelve float)
raiz_float = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz_float}")  # Ej: 3.0

#Si queremos un entero, aplicamos conversión
raiz_entero = int(math.sqrt(numero))
print(f"La raíz cuadrada entera de {numero} es {raiz_entero}")  # Ej: 3

#Calculamos el valor absoluto
valor_absoluto = math.fabs(-numero)
print(f"El valor absoluto de -{numero} es {valor_absoluto}")

#Redondeamos hacia abajo y hacia arriba
print("Redondeo hacia abajo:", math.floor(raiz_float))
print("Redondeo hacia arriba:", math.ceil(raiz_float))

#Usamos constantes matemáticas
print("Valor de pi:", math.pi)
print("Valor de e:", math.e)

#Potencias y logaritmos
print("Potencia:", math.pow(2, 3))       # 2^3 = 8.0
print("Logaritmo natural:", math.log(math.e))  # log(e) = 1.0

#Trigonometría básica
angulo = math.radians(90)  # Convertimos grados a radianes
print("Seno de 90°:", math.sin(angulo))  # ≈ 1.0
print("Coseno de 90°:", math.cos(angulo))  # ≈ 0.0
