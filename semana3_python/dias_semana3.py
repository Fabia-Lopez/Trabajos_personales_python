#dia 1
#ejemplos
"""
try:
    edad = int(input("Edad: "))
except:
    print("Eso no es un número")


#ejercicio 1

Pedir número válido

Haz un programa que pida un número al usuario.

Si el usuario escribe algo que no es número → mostrar "Error, ingresa un número"

Si sí es número → imprimir "Número guardado correctamente"

Debe usar:

try
except

while True:
    try:
        numero = int(input("Ingresa un numero: "))
        print(f"Numero guardado correctamente: {numero}")
        break
    except:
        print("Error, ingresa un numero valido")


#ejercicio 2

División segura

Pide dos números al usuario:

número 1

número 2

Luego imprime la división.

PERO:

Si el usuario mete letras → error

Si mete 0 como divisor → error (no se puede dividir entre 0)

Debe mostrar mensajes como:

"No se puede dividir entre 0"

"Error: ingresa números válidos"


while True:
    try:
        numero1=int(input("ingresa un numero 1: "))
        numero2=int(input("ingresa el numero 2: "))
        print(f"la division de {numero1} y {numero2} es: {numero1/numero2}")
        break
    except ValueError:
        print("Error: ingresa numeros validos")
    except ZeroDivisionError:
        print("no se puede dividir entre 0")


#ejercicio 3
Menú con validación (modo cajero pro)

Haz un menú tipo cajero:

1. Consultar saldo
2. Depositar
3. Retirar
4. Salir


Reglas:
saldo inicial = 1000
debe repetirse con while
para depositar y retirar debes pedir monto

Pero OJO:

si el usuario mete letras en vez de número → no debe romperse

si mete un retiro mayor al saldo → "Saldo insuficiente"

si mete monto negativo → "Monto inválido"

Aquí vas a usar try/except en depósito y retiro.


saldo = 1000

while True:
    print("\n1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        print(f"Tu saldo es: {saldo}")

    

    elif opcion == "2":
        try:
            deposito = int(input("Monto a depositar: "))

            if deposito <= 0:
                print("Monto inválido")
            else:
                saldo += deposito
                print(f"Depósito exitoso. Nuevo saldo: {saldo}")

        except ValueError:
            print("Error: ingresa un número válido")

    elif opcion == "3":
        try:
            retiro = int(input("Monto a retirar: "))

            if retiro <= 0:
                print("Monto inválido")
            elif retiro > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= retiro
                print(f"Retiro exitoso. Nuevo saldo: {saldo}")

        except ValueError:
            print("Error: ingresa un número válido")

    elif opcion == "4":
        print("Gracias por usar el cajero")
        break

    else:
        print("Opción no válida")

#dia 2
#ejercicio 1
Registro de edades (validación pro)

Pide al usuario cuántas personas va a registrar.

Luego pide la edad de cada persona.

Reglas:

Si mete letras → error

Si mete edad negativa o 0 → "Edad inválida"

Guarda todas las edades en una lista

Al final imprime:

lista de edades

promedio de edades

Ejemplo:

Edades registradas: [18, 20, 15]
Promedio: 17.6

personas = int(input("¿Cuántas personas vas a registrar? "))
edades = []

for i in range(personas):
    while True:
        try:
            edad = int(input(f"Edad de la persona {i+1}: "))
            if edad <= 0:
                print("Edad inválida")
            else:
                edades.append(edad)
                break
        except ValueError:
            print("Error: ingresa un número válido")

print(f"Edades registradas: {edades}")
if len(edades) > 0:
    promedio = sum(edades) / len(edades)
    print(f"Promedio: {promedio:.1f}")
else:
    print("No se registraron edades.")


#ejercicio 2
pide al usuario cuántos alumnos va a registrar.

Por cada alumno pide:

nombre

calificación

Guarda cada alumno en un diccionario:

{"nombre": "Juan", "calificacion": 90}


Guárdalos en una lista.

Reglas:

calificación debe estar entre 0 y 100

si mete letras → error

si mete fuera de rango → "Calificación inválida"

Al final imprime:

ALUMNOS REGISTRADOS
1. Juan - 90
2. Ana - 100

alumnos = []
cantidad = int(input("¿Cuántos alumnos vas a registrar? "))

for i in range(cantidad):
    nombre = input(f"Nombre del alumno {i+1}: ")
    
    while True:
        try:
            calificacion = int(input(f"Calificación de {nombre}: "))
            if 0 <= calificacion <= 100:
                alumnos.append({"nombre": nombre, "calificacion": calificacion})
                break
            else:
                print("Calificación inválida")
        except ValueError:
            print("Error: ingresa un número válido")

print("\nALUMNOS REGISTRADOS")
for i, alumno in enumerate(alumnos, start=1):
    print(f"{i}. {alumno['nombre']} - {alumno['calificacion']}")


#ejercicio 3
Buscar alumno (modo pro)

Usando la lista del ejercicio 2:

Pide un nombre de alumno para buscar.

Si existe:
Imprime su calificación.

Si no existe:
Imprime:

Alumno no encontrado


Requisitos:

usar bandera encontrado = False

la búsqueda debe ser sin importar mayúsculas/minúsculas

Ejemplo:
Entrada: "juan"
Salida: "La calificación de Juan es 90"

nombre_buscar = input("Ingresa el nombre del alumno a buscar: ").strip().lower()
encontrado = False
for alumno in alumnos:
    if alumno["nombre"].lower() == nombre_buscar:
        print(f"La calificación de {alumno['nombre']} es {alumno['calificacion']}")
        encontrado = True
        break
if not encontrado:
    print("Alumno no encontrado")

"""