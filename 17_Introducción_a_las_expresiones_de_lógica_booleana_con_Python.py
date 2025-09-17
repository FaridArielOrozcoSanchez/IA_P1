#Introducción a las expresiones de lógica booleana con Python
'''
Este capítulo explica los fundamentos de la lógica booleana en programación, incluyendo:
1. Operadores de comparación:
   - == : Igual que
   - != : Diferente que
   - <  : Menor que
   - >  : Mayor que
   - <= : Menor o igual que
   - >= : Mayor o igual que
2. Operadores lógicos:
   - and : Devuelve True si ambas expresiones son verdaderas
   - or  : Devuelve True si al menos una expresión es verdadera
   - not : Invierte el valor booleano de una expresión
'''
#Ejemplos

#Comparadores   
# Igual que (==)
a = 10
b = 10
print(a == b)  # True

# Diferente que (!=)
a = 10
b = 15
print(a != b)  # True

# Mayor que (>)
a = 20
b = 15
print(a > b)   # True

# Menor que (<)
a = 5
b = 10
print(a < b)   # True

# Mayor o igual que (>=)
a = 10
b = 10
print(a >= b)  # True

# Menor o igual que (<=)
a = 8
b = 10
print(a <= b)  # True

#Operadores
# Operador AND
a = 5
b = 10
c = 15
resultado = a < b and b < c
print(resultado)  # True

# Operador OR
a = 5
b = 10
c = 15
resultado = a > b or b < c
print(resultado)  # True

# Operador NOT
a = 5
b = 10
resultado = not a > b
print(resultado)  # True

#Expreciones complejas
a = 10
b = 20
c = 30
# Combinación de operadores
resultado = not (a < b and (b == c or c != a))
print(resultado)  # False
