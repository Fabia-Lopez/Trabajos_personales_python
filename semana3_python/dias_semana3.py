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


#dia 3
EJERCICIO 1: Registrar alumnos con función

Crea una función llamada:

registrar_alumno(lista)


Que pida:

nombre

calificación (0 a 100)

Validaciones:

si mete letras en calificación → error

si está fuera de rango → "Calificación inválida"

Guarda así:

{"nombre": "Juan", "calificacion": 90}

def registrar_alumno(lista):
    while True:
        nombre = input("Nombre del alumno: ").strip()
        if nombre == "":
            print("Nombre inválido")
        else:
            break

    while True:
        try:
            calificacion = int(input(f"Calificación de {nombre} (0-100): "))
            if 0 <= calificacion <= 100:
                lista.append({"nombre": nombre, "calificacion": calificacion})
                print(f"Alumno {nombre} registrado con calificación {calificacion}.")
                break
            else:
                print("Calificación inválida")
        except ValueError:
            print("Error: ingresa un número válido")


#ejercicio 2
Crea una función:

mostrar_alumnos(lista)


Debe imprimir:

ALUMNOS REGISTRADOS
1. Juan - 90
2. Ana - 100


Si la lista está vacía:

No hay alumnos registrados

def mostrar_alumnos(lista):
    if len(lista) == 0:
        print("No hay alumnos registrados")
    else:
        print("\nALUMNOS REGISTRADOS")
        for i, alumno in enumerate(lista, start=1):
            print(f"{i}. {alumno['nombre']} - {alumno['calificacion']}")


#ejercicio 3
Buscar alumno

Función:

buscar_alumno(lista)


Pide un nombre y busca sin importar mayúsculas/minúsculas.

Si existe:

La calificación de Juan es 90


Si no:

Alumno no encontrado

def buscar_alumno(lista):
    nombre_buscar = input("Ingresa el nombre del alumno a buscar: ").strip().lower()
    encontrado = False
    for alumno in lista:
        if alumno["nombre"].lower() == nombre_buscar:
            print(f"La calificación de {alumno['nombre']} es {alumno['calificacion']}")
            encontrado = True
            break
    if not encontrado:
        print("Alumno no encontrado")


#ejercicio 4
Promedio general

Función:

promedio_general(lista)


Regresa el promedio de todas las calificaciones.

Si no hay alumnos → regresar 0

def promedio_general(lista):
    if len(lista) == 0:
        return 0
    total = sum(alumno["calificacion"] for alumno in lista)
    return total / len(lista)

#ejercicio 5
Contar aprobados y reprobados

Función:

contar_aprobados(lista)


Aprobado si >=70

y otra:

contar_reprobados(lista)

def contar_aprobados(lista):
    return sum(1 for alumno in lista if alumno["calificacion"] >= 70)

def contar_reprobados(lista):
    return sum(1 for alumno in lista if alumno["calificacion"] < 70)

#ejercicio 6
Menú completo

Haz un programa con menú así:

1. Registrar alumno
2. Mostrar alumnos
3. Buscar alumno
4. Promedio general
5. Contar aprobados y reprobados
6. Salir
El menú debe repetirse con while True hasta que el usuario elija salir.

alumnos = []
while True:
    print("\n1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Promedio general")
    print("5. Contar aprobados y reprobados")
    print("6. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_alumno(alumnos)
    elif opcion == "2":
        mostrar_alumnos(alumnos)
    elif opcion == "3":
        buscar_alumno(alumnos)
    elif opcion == "4":
        if len(alumnos) == 0:
            print("No hay alumnos registrados")
        else:
            promedio = promedio_general(alumnos)
            print(f"Promedio general: {promedio:.2f}")
    elif opcion == "5":
        aprobados = contar_aprobados(alumnos)
        reprobados = contar_reprobados(alumnos)
        print(f"Aprobados: {aprobados}, Reprobados: {reprobados}")
    elif opcion == "6":
        print("Gracias por usar el programa")
        break
    else:
        print("Opción no válida")


#dia 4
#ejercicio 1
Editar calificación de un alumno

Tienes una lista de alumnos así:

alumnos = [
{"nombre": "Juan", "calificacion": 90},
{"nombre": "Ana", "calificacion": 100}
]


Haz una función:

editar_calificacion(lista)

Debe hacer esto:

Pedir el nombre del alumno a editar

Buscarlo sin importar mayúsculas/minúsculas

Si lo encuentra:

pedir la nueva calificación

validar que sea entre 0 y 100

actualizarla

Si no existe:

imprimir "Alumno no encontrado"

alumnos = [
    {"nombre": "Juan", "calificacion": 90},
    {"nombre": "Ana", "calificacion": 100}
]

def editar_calificacion(lista):
    nombre_buscar = input("Ingresa el nombre del alumno a editar: ").strip().lower()
    encontrado = False
    for alumno in lista:
        if alumno["nombre"].lower() == nombre_buscar:
            while True:
                try:
                    nueva_calificacion = int(input(f"Ingresa la nueva calificación para {alumno['nombre']} (0-100): "))
                    if 0 <= nueva_calificacion <= 100:
                        alumno["calificacion"] = nueva_calificacion
                        print(f"Calificación de {alumno['nombre']} actualizada a {nueva_calificacion}.")
                        break
                    else:
                        print("Calificación inválida")
                except ValueError:
                    print("Error: ingresa un número válido")
            encontrado = True
            break
    if not encontrado:
        print("Alumno no encontrado")

#ejercicio 2
Eliminar alumno

Haz una función:

eliminar_alumno(lista)

Debe:

pedir nombre del alumno

buscarlo

si lo encuentra eliminarlo de la lista

imprimir "Alumno eliminado"

si no existe imprimir "Alumno no encontrado"

alumnos = [
    {"nombre": "Juan", "calificacion": 90},
    {"nombre": "Ana", "calificacion": 100}
]

def eliminar_alumno(lista):
    nombre_buscar = input("Ingresa el nombre del alumno a eliminar: ").strip().lower()
    encontrado = False
    for i, alumno in enumerate(lista):
        if alumno["nombre"].lower() == nombre_buscar:
            del lista[i]
            print(f"Alumno {alumno['nombre']} eliminado.")
            encontrado = True
            break
    if not encontrado:
        print("Alumno no encontrado")

#ejercicio 3
Reporte completo de alumnos

Haz una función:

reporte_alumnos(lista)

Si la lista está vacía imprimir:

No hay alumnos registrados


Si hay alumnos debe imprimir:

REPORTE FINAL
Total alumnos: 5
Promedio general: 78.4
Mayor calificación: 100
Menor calificación: 45
Aprobados: 3
Reprobados: 2


Reglas:

Aprobado si >= 70

Reprobado si < 70

Usa for y contadores o sum()

Promedio con 1 decimal

EXTRA (Opcional si quieres)

Agrega estas opciones a tu menú:

7. Editar calificación
8. Eliminar alumno
9. Reporte final

def reporte_alumnos(lista):
    if len(lista) == 0:
        print("No hay alumnos registrados")
    else:
        total_alumnos = len(lista)
        promedio = promedio_general(lista)
        mayor_calificacion = max(alumno["calificacion"] for alumno in lista)
        menor_calificacion = min(alumno["calificacion"] for alumno in lista)
        aprobados = contar_aprobados(lista)
        reprobados = contar_reprobados(lista)

        print("\nREPORTE FINAL")
        print(f"Total alumnos: {total_alumnos}")
        print(f"Promedio general: {promedio:.1f}")
        print(f"Mayor calificación: {mayor_calificacion}")
        print(f"Menor calificación: {menor_calificacion}")
        print(f"Aprobados: {aprobados}")
        print(f"Reprobados: {reprobados}")

def promedio_general(lista):
    if len(lista) == 0:
        return 0
    total = sum(alumno["calificacion"] for alumno in lista)
    return total / len(lista)

def contar_aprobados(lista):
    return sum(1 for alumno in lista if alumno["calificacion"] >= 70)

def contar_reprobados(lista):
    return sum(1 for alumno in lista if alumno["calificacion"] < 70)
"""