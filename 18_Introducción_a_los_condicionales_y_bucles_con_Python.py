
#Condicionales y Bucles en Python
'''
1. Condicionales:
   - if: ejecuta si la condición es True.
   - elif: condiciones adicionales.
   - else: ejecuta si ninguna condición anterior se cumple.
   - match-case: alternativa a múltiples if (Python 3.10+).

2. Bucles:
   - for: recorre secuencias (listas, rangos, etc.).
   - while: repite mientras la condición sea True.
   - Simulación de do-while: usando while True + break.

3. Indentación:
   - Python usa sangrías (TAB o espacios) para definir bloques.
   - La indentación incorrecta genera errores (IndentationError).

4. Operadores útiles:
   - Asignación: +=, -=, *=, /=.
   - Ternario: resultado = "Sí" if condición else "No".
   - type() + is: para evaluar tipos de datos.
'''
#Ejemplos prácticos:

# Condicional simple
edad = 20
if edad >= 18:
    print("Es mayor de edad.")

# Condicional if-elif-else
edad = 70
if edad < 18:
    print("Menor de edad.")
elif edad < 65:
    print("Adulto.")
elif edad < 75:
    print("Maduro.")
else:
    print("Anciano.")

# Condicional con type()
valor = [1, 2, 3]
if type(valor) is list:
    print("Es una lista.")

# Operador ternario
edad = 17
print("Mayor" if edad >= 18 else "Menor")

# match-case (Python 3.10+)
codigo = 404
match codigo:
    case 200:
        print("Todo ok.")
    case 404:
        print("Página no encontrada.")
    case _:
        print("Código desconocido.")

# Bucle for
for i in range(5):
    print(f"Iteración {i}")

# Bucle while
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Simulación do-while
while True:
    respuesta = input("¿Continuar? (s/n): ")
    if respuesta != "s":
        break