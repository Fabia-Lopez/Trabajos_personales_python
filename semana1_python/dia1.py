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
#dia 4
#ejemplos
"""
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "Fabian"]
mezcla = [10, "hola", 3.5]

print(nombres[0])  # Ana
print(nombres[2])  # Fabian

calificaciones = [80, 90, 75]

for calificacion in calificaciones:
    print(calificacion)

calificaciones = []
calificaciones.append(90)
calificaciones.append(85)

print(len(calificaciones))

suma = 0

for c in calificaciones:
    suma += c

promedio = suma / len(calificaciones)

#ejercicio 1

Crea una lista vacía
Pide 5 números al usuario
Guárdalos en la lista
Imprime la lista completa

lista = []

for i in range(5):
    numero = int(input("Ingresa un número: "))
    lista.append(numero)

print(lista)


#ejercicio 2
Crea una lista de calificaciones
Recorre la lista con for
Imprime solo las calificaciones mayores o iguales a 70


calificaciones=[22,0,73,5,100]

for calificacion in calificaciones:
    if calificacion >= 70:
        print(f"esta calificacion es mayor o igual a 70: {calificacion}")



#ejercicio 3
Pida:

nombre

cuántas calificaciones va a ingresar

Use una lista para:

guardar todas las calificaciones

Al final:

calcule el promedio

diga si aprobó o reprobó


nombre= input("dime tu nombre: ")
calificaciones = int(input("cuantas calificaciones quieres ingresar: "))

calificacion = []
suma=0
promedio =0

for i in range (1, calificaciones+1):
    grade = int(input("ingresa calificacion: "))
    calificacion.append(grade)
    suma+=grade
print(calificacion)
promedio= suma/ len(calificacion)

if promedio > 59:
    print(f"{nombre} aprobaste con un promedio de {promedio}")
else:
    print(f"{nombre} reprobaste con un promedio de {promedio}")


#hecho por chat

nombre = input("Dime tu nombre: ")
cantidad = int(input("¿Cuántas calificaciones vas a ingresar? "))

calificaciones = []

for i in range(cantidad):
    nota = int(input(f"Ingresa la calificación {i + 1}: "))
    calificaciones.append(nota)

suma = 0
for nota in calificaciones:
    suma += nota

promedio = suma / len(calificaciones)

print(f"Calificaciones ingresadas: {calificaciones}")
print(f"Promedio: {promedio}")

if promedio >= 70:
    print(f"{nombre}, aprobaste")
else:
    print(f"{nombre}, reprobaste")

"""
