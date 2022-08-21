from datetime import datetime, timedelta, date, time

#Consultar strftime.org
#Obtener la fecha actual usando datetime
hoy = datetime.today()
print(f"La fecha de hoy es: {hoy}")

#Obtener solo la hora actual uando strftime(formato)
hora = datetime.today().strftime('%H-%M-%S')
print(hora)


#Obtener el año
print(hoy.year)

# #Obtener el mes
print(hoy.month)

# #Obtener el día
print(hoy.day)

# #Obtener la hora
print(hoy.hour)

# #Obtener el minuto
print(hoy.minute)

# #Obtener el segundo
print(hoy.second)

# #Obtener el microsegundo
print(hoy.microsecond)


#Sumar dos días a la fecha actual
hoy = datetime.now()
nueva_fecha = hoy + timedelta(days=2)
print(nueva_fecha)

#Restar dos días a la fecha actual
hoy = datetime.now()
nueva_fecha = hoy - timedelta(days=2)
print(nueva_fecha)


#Calcular tiempo de ejecución de un algoritmo
inicio = time.process_time()
for i in range (1000):
	print("Calculando en tiempo")

fin = time.process_time()
print(fin - inicio)

#Convertir cadena en fecha
resultado = datetime.strptime('15/4/2020', '%d/%m/%Y')
print(type(resultado))
print(resultado)


#Extrae solo la fecha actual sin hora
fecha = date.today()
print(fecha)