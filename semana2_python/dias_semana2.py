#dia 1
#ejemplos
#estructuras de una funcion
"""
def nombre_funcion(parametros):
    # código
    return resultado

def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)
"""
#ejercicio 1
"""
Crea una función llamada saludo() que:
No reciba parámetros
Imprima: "Bienvenido al sistema"

Luego:

Llama la función 3 veces

def saludo()->None:
    print("Bienvenido al sistema")

saludo()
saludo()
saludo()

#ejercicio 2
Crea una función calcular_promedio(a, b, c) que:
Reciba 3 calificaciones
Regrese el promedio
Imprima si aprobó (≥70) o reprobó
Usa return


def calcular_promedio(a,b,c)->int:
    promedio = (a+b+c)/3
    return promedio

a=int(input("ingresa el primer numero: "))
b=int(input("ingresa el primer numero: "))
c=int(input("ingresa el primer numero: "))

promedio = calcular_promedio(a,b,c)
if promedio>= 70:
    print (f"el promedio fue de {promedio}: aprobado")
else:
    print(f"reprobaste con {promedio}")

#ejercicio 3

consultar_saldo()
depositar(saldo)
retirar(saldo)
menu()

El while debe estar en el menu()
Las funciones deben modificar o devolver el saldo


def consultar_saldo(saldo):
    print(f"tu saldo es: {saldo}")
    return saldo

def depositar(saldo):
    deposito= int(input("cuanto quieres depositar: "))
    return saldo + deposito

def retirar(saldo):
    retiro = int(input("cuanto quieres retirar: "))
    if retiro> saldo:
        print("saldo insuficiente")
        return saldo
    else:
        print(f"retiraste: {retiro} de tu saldo {saldo}")
        return saldo - retiro

def menu():
    saldo = 1000
    opcion = ""

    while opcion != "salir":
        print("\n1. consultar saldo")
        print("2. depositar")
        print("3. retirar")
        print("4. salir")

        opcion = input("Elige una opción: ").lower()

        if opcion == "consultar saldo":
            saldo = consultar_saldo(saldo)
        elif opcion == "depositar":
            saldo = depositar(saldo)
        elif opcion == "retirar":
            saldo = retirar(saldo)
        elif opcion == "salir":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()

#dia 2
#ejemplos
def sumar_lista(numeros):
    suma = 0
    for n in numeros:
        suma += n
    return suma

#ejercicio 1
Crea una función llamada calcular_promedio(lista) que:
Reciba una lista de números
Regrese el promedio
def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

#ejercicio 2
Crea una función llamada mayor_y_menor(lista) que:
Reciba una lista
Regrese el número mayor y el número menor

def mayor_menor(lista):
    mayor= lista[0]
    menor = lista[0]

    for num in lista:
        if num > mayor:
            mayor = num
            
        if num< menor:
            menor = num
            
    return mayor, menor

#ejercicio 3
Pida cuántas calificaciones va a ingresar
Guarde todas en una lista
Cree funciones para:

promedio

mayor

menor

contar cuántas son aprobatorias (>=70)

contar cuántas son reprobatorias (<70)

Al final debe imprimir un reporte así:
📊 REPORTE FINAL
Promedio: 78.5
Mayor: 100
Menor: 45
Aprobados: 4
Reprobados: 2

calificaciones = int(input("cuantas calificaciones deseas ingresar: "))
lista=[]

for n in range(calificaciones):
    calificacion=int(input("ingresa una calificacion: "))
    lista.append(calificacion)


def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def mayor(lista):
    mayor= lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

def menor(lista):
    menor = lista[0]
    for num in lista:
        if num< menor:
            menor = num
    return menor

def contar_aprobadas(lista):
    aprobadas=[]
    for n in lista:
        if n >=70:
            aprobadas.append(n)
    return len(aprobadas)

def contar_reprobadas(lista):
    reprobadas=[]
    for n in lista:
        if n < 70:
            reprobadas.append(n)
    return len(reprobadas)

print("informa final")
print(f"el promedio: {calcular_promedio(lista)}")
print(f"el mayor: {mayor(lista)}")
print(f"el menor: {menor(lista)}")
print(f"aprobadas: {contar_aprobadas(lista)}")
print(f"Reprobadas: {contar_reprobadas(lista)}")
"""