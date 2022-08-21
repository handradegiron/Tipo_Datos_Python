import pyautogui

# solicita datos al usuario

primer_numero = pyautogui.prompt(text="Primer numero", title="Solicitud", default="")
segundo_numero = pyautogui.prompt(text="ingresar 2° número", title="Solicitud", default="")

#convierte datos a enteros
primer_numero = float(primer_numero)
segundo_numero = float(segundo_numero)

#realiza las operaciones solicitados
suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
division = primer_numero / segundo_numero


#Entrega resultados a usuario mediante consola
print("Resultado de la suma es:" + str(suma))
print("Resultado de la resta es: "+str(resta))
print("Resultado de la multiplicación es: "+str(multiplicacion))
print("Resultado de la division es: "+str(division))