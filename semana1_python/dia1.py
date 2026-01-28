"""
print("hola mundo")
nombre = "fabian lopez"
carrera= "ingenieria en sistemas "
semestre = "4to semestre"

print("soy", nombre, "estoy en", carrera, "y curso el", semestre) 

#ejercicio 2
a =10 
b=20
print (a+b)
print (a-b)
print (a*b)
print (a/b)

#ejercicio 3
edad= 19
print ("mi edad es", edad, "en 10 años tendre ", edad+10) 
print ("mi edad es", edad, "en 20 años tendre ", edad+20)
print ("mi edad es", edad, "en 30 años tendre ", edad+30)

#ejercicio final del dia
#Pide el nombre con input()
#Pide la edad
# Imprime cuántos años tendrá en 5 y 10 años
#Usa f-strings

nombre = input("¿Cual es tu nombre? ")
edad = int(input("¿Cual es tu edad? ")) 

print(f"Hola {nombre}, en 5 años tendras {edad + 5} años y en 10 años tendras {edad+10} años.")

#fin del dia 1
"""

#Dia 2
#Ejemplos
"""
calificacion = 85

if calificacion >= 70:
    print("Aprobaste la materia")
else:
    print("Reprobaste la materia")

calificaciones = 92

if calificaciones >= 90:
    print("Excelente")
elif calificaciones >= 80:
    print("Muy bien")
elif calificaciones >= 70:
    print("Bien")
else:
    print("Reprobado")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes votar")
else:
    print("No puedes votar")

dinero = 5000

if dinero >= 10000:
    print("Puedes invertir")
else:
    print("Aún necesitas ahorrar más")

#Ejercicio 1
#hecho por mi

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print(f"{nombre}, no puedes votar.")
elif edad < 65:
    print (f"{nombre}, puedes votar.")
else:
    print(f"{nombre}, eres un adulto mayor")

#estilo pro hecho por chat
mensaje = ""

if edad < 18:
    mensaje = "no puedes votar"
elif edad < 65:
    mensaje = "puedes votar"
else:
    mensaje = "eres un adulto mayor"

print(f"{nombre}, {mensaje}.")

#ejercicio 2
#hecho por mi
nombres = input("Ingresa tu nombre: ")
calificacion = int(input("Ingresa tu calificacion: "))

if calificacion<70:
    print(f"{nombres} tu calificacion es {calificacion}, Reprobado")
elif calificacion< 90:
    print(f"{nombres} tu calificacion es {calificacion}, Aprobado")
else:
    print(f"{nombres} tu calificacion es {calificacion}, Excelente")

#ejercicio 3
#hecho por mi

nombress= input("Ingresa tu nombre: ")
edads = int(input("ingresa tu edad: ")) 
dinero = int(input("ingresa tu dinero disponible: "))

if edads < 18:
    print (f"{nombress}: Acceso denegado por edad")
elif edads>= 18 and dinero <100:
    print (f"{nombress}:Acceso denegado por fondos")
else:
    print(f"{nombress}: Acceso autorizado. Bienvenido al sistema")

#hecho por chat
if edads < 18:
    print(f"{nombress}: Acceso denegado por edad")
elif dinero < 100:
    print(f"{nombress}: Acceso denegado por fondos")
else:
    print(f"{nombress}: Acceso autorizado. Bienvenido al sistema")
"""
#dia 3
#ejemplos
"""
for i in range(5):
    print(i)

range(inicio, fin, paso)
range(0, 5)      # 0 1 2 3 4
range(1, 6)      # 1 2 3 4 5
range(0, 10, 2)  # 0 2 4 6 8

for i in range(1, 6):
    print(f"Repetición número {i}")

nombre = "Fabian"

for letra in nombre:
    print(letra)

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} es par")

"""
#ejercicio 1
"""
Usa un for
Imprime los números del 1 al 10
Muestra si el número es par o impar

for i in range (1,11):
    if i% 2== 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
"""

#ejercicio 2
"""
Pide un número al usuario
Usa un for
Imprime la tabla de multiplicar de ese número del 1 al 10

numero = int(input("ingresa un numero: "))

for i in range (1,11):
    print(f"{numero} x {i} = {numero * i}")
"""

#ejercicio 3
"""
Pida:

nombre

cuántas calificaciones va a ingresar

Use un for para:

pedir cada calificación

acumular la suma

Al final:

calcule el promedio

muestre si aprobó (≥70) o reprobó

nombre = input("dime tu nombre: ")

calificacion = int(input("cuantas calificaciones quieres ingresar: "))

suma= 0

for i in range (1, calificacion + 1):
    print (f"calificacion {i}")
    calificaciones= int(input("ingresa calificacion: "))
    suma+= calificaciones

promedio = suma/calificacion
print(f"el promedio de {nombre} es igual a {promedio}")

if promedio >= 70:
    print(f"{nombre} aprobaste")
else:
    print(f"{nombre} reprobaste")
"""
