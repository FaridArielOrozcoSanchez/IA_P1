import calculadora
import utilidades

resultado = calculadora.multiplicar(6, 7)
utilidades.mostrar_mensaje(f"Resultado de la multiplicación: {resultado}")

if utilidades.es_par(resultado):
    utilidades.mostrar_mensaje("El resultado es par.")
else:
    utilidades.mostrar_mensaje("El resultado es impar.")
