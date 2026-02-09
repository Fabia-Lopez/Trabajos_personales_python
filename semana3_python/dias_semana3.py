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
"""