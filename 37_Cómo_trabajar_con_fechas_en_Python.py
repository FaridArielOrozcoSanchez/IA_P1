#Cómo trabajar con fechas en Python: Tutorial completo con ejemplos

'''
¿Qué es datetime?
Es un módulo integrado en Python que permite trabajar con fechas (date), horas (time) y combinaciones de ambas (datetime). No requiere instalación.
'''

#Importamos el módulo
import datetime

#Creamos un objeto de tipo time (hora)
hora = datetime.time(14, 30, 20, 7577)
print("Hora completa:", hora)  # Salida: 14:30:20.007577

#Accedemos a sus atributos
print("Hora:", hora.hour)
print("Minutos:", hora.minute)
print("Segundos:", hora.second)
print("Microsegundos:", hora.microsecond)

#Creamos un objeto de tipo date (fecha)
fecha = datetime.date(2027, 12, 20)
print("Fecha completa:", fecha)  # Salida: 2027-12-20

#Accedemos a sus atributos
print("Año:", fecha.year)
print("Mes:", fecha.month)
print("Día:", fecha.day)

#Obtenemos la fecha actual
fecha_hoy = datetime.date.today()
print("Fecha actual:", fecha_hoy)  # Ejemplo: 2025-09-18

#Obtenemos fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)  # Ejemplo: 2025-09-18 00:11:56.123456

#Accedemos a partes específicas
print("Solo hora:", fecha_hora_actual.hour)
print("Solo día:", fecha_hora_actual.day)

#Formateamos la fecha con strftime()
fecha_formateada = fecha_hora_actual.strftime("%A, %d de %B de %Y a las %H:%M")
print("Fecha formateada:", fecha_formateada)  # Ejemplo: Thursday, 18 de September de 2025 a las 00:11

#Traducimos la fecha al español con locale
import locale
locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")  # En Windows puede requerir configuración regional

fecha_espanol = fecha_hora_actual.strftime("%A, %d de %B de %Y a las %H:%M").capitalize()
print("Fecha en español:", fecha_espanol)  # Ejemplo: Jueves, 18 de septiembre de 2025 a las 00:11
