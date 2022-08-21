#MAYUSCULAS Y MINUSCULAS

#Para ello se utiliza el método title()
nombre = "josé martinez"
nombre = nombre.title()
print(nombre)


#Convierte toda la cadena a mayúscula 
#Para ello se utiliza el método upper()
nombre = "josé martinez"
nombre = nombre.upper()
print(nombre)

#Convierte toda la cadena a minúscula 
#Para ello se utiliza el método lower()
nombre = "JOSE MARTINEZ"
nombre = nombre.lower()
print(nombre)



#CADENA DE VARIAS LINEAS
mensaje = """Muy cordialmente, la presente es para 
comunicarle de la suspención del servicio"""

print(mensaje)



#DAR FORMATO A UNA CADENA
#Con una variable
color = "verde"


print("El color es {}".format(color))
print(f"El color es {color}")


#Más de dos variables
objeto = "polo"
color = "verde"
print("Usted tiene un {} {}".format(objeto, color))
print(f"Usted tiene un {objeto} {color}")


#LONGITUD DE UNA CADENA
#Para ello se utiliza la función len()
cadena = "Flecha: ->"
longitud = len(cadena)
print(longitud)


#CONOCER PERTENENCIA
#Para saber si una cadena está contenida en otra se utiliza in

nombre ="María Ramirez Rojas"
fragmento = "María Ramirez"
fragmento2 = "Rojas"
resultado = fragmento in nombre
resultado2 = fragmento2 in nombre
print(resultado)
print(resultado2)



#CONOCER REPETICIONES DE CADENA
#Contra el número de ocurrencias de un caracter en una cadena
#Para ello se utiliza count()
cadena = "María es enfermera. María es casada. María va al gym"
resultado = cadena.count("María")
print(resultado)


#REMPLAZAR CADENAS
#El método para remplazar caracteres es "replace"
cadena = "María es enfermera. María es casada. María va al gym"
resultado = cadena.replace("María", "Ana")
print(resultado)



#ACCEDER A UNA CADENA EN CONCRETO
#Se accede a un caracter en concreto mediane operador []
cadena = "María es enfermera."
print(cadena[0])


#ELIMINAR ESPACIOS EN BLANCO
#Para ello se utiliza en método strip()
cadena = " María "
resultado = cadena.strip()
print(len(resultado))

#OPERACIONES CON CADENAS

#Suma
nombre = "Paolo "
apellido = "Guerrero"
resultado = nombre + apellido
print(resultado)

#Multiplicación
nombre = "Paolo"
resultado = nombre*3
print(resultado)