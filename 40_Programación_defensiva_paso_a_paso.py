#Programación defensiva paso a paso: guía definitiva con Python

'''
¿Qué es?
Es una técnica que busca anticiparse a errores y mal uso del programa, validando entradas, manejando excepciones y asegurando condiciones internas.
'''

#Manejo básico de excepciones
def dividir(a, b):
    try:
        resultado = round(a / b, 2)
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except TypeError:
        print("Tipo de dato incorrecto.")
    finally:
        print("Operación finalizada.")

dividir(10, 2)
dividir(10, 0)
dividir(10, "texto")

#Validación de tipo con isinstance()
def validar_entero(valor):
    if isinstance(valor, int):
        print("Es un entero.")
    else:
        print(f"No es entero: {type(valor).__name__}")

validar_entero(42)
validar_entero("42")

#Validación con isdigit() y bandera
bandera = False
while not bandera:
    edad = input("Introduce tu edad: ")
    if edad.isdigit():
        print(f"Edad válida: {edad}")
        bandera = True
    else:
        print("Debes introducir un número entero.")

#Validación de longitud
contrasena = input("Introduce una contraseña (mínimo 8 caracteres): ")
if len(contrasena) >= 8:
    print("Contraseña válida.")
else:
    print("Contraseña demasiado corta.")

#Validación de rango con manejo de excepciones
while True:
    try:
        numero = int(input("Escribe un número del 1 al 10: "))
        if 1 <= numero <= 10:
            print(f"Número válido: {numero}")
            break
        else:
            print("El número debe estar entre 1 y 10.")
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

#Uso de afirmaciones con assert
def procesar(valor):
    assert isinstance(valor, int), "El valor debe ser un entero."
    assert valor > 0, "El valor debe ser positivo."
    print(f"Procesando valor: {valor}")

procesar(5)
# procesar("texto")  # Lanza AssertionError
# procesar(-3)       # Lanza AssertionError

#Ejemplo de múltiples excepciones
def abrir_archivo(ruta):
    try:
        with open(ruta, "r") as archivo:
            print("Archivo abierto correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except OSError:
        print("Error del sistema operativo.")
    finally:
        print("Proceso de apertura finalizado.")

abrir_archivo("archivo_inexistente.txt")

#Depuración con print y control de errores
def sumar(a, b):
    print(f"Sumando {a} + {b}")
    try:
        return a + b
    except TypeError:
        print("Error de tipo en la suma.")
        return None

print("Resultado:", sumar(10, 5))
print("Resultado:", sumar(10, "cinco"))
