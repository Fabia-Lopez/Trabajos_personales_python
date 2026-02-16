"""
#dia 1
ejercicio 1
Registrar productos con stock

Pide cuántos productos vas a registrar.

Cada producto debe guardar:

id automático

nombre

precio

stock

Formato:

{"id": 1, "nombre": "Coca", "precio": 20, "stock": 15}


Al final imprime:

PRODUCTOS REGISTRADOS
1. Coca - $20 - Stock: 15
2. Pan - $15 - Stock: 10

cantidad_productos = int(input("¿Cuántos productos vas a registrar? "))
productos = []

for i in range(cantidad_productos):
    nombre = input(f"Ingresa el nombre del producto {i + 1}: ")
    precio = float(input(f"Ingresa el precio del producto {i + 1}: "))
    stock = int(input(f"Ingresa el stock del producto {i + 1}: "))
    
    producto = {"id": i + 1, "nombre": nombre, "precio": precio, "stock": stock}
    productos.append(producto)

print("\nPRODUCTOS REGISTRADOS")
for producto in productos:
    print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


ejercicio 2 
Buscar producto por nombre

Usando la lista del ejercicio 1:

Pide un nombre de producto.

Si existe:

Producto encontrado:
ID: 2
Nombre: Pan
Precio: 15
Stock: 10


Si no existe:

Producto no encontrado


Requisito:

búsqueda sin importar mayúsculas/minúsculas

bandera encontrado = False


nombre_busqueda = input("Ingresa el nombre del producto que deseas buscar: ")
encontrado = False

for producto in productos:
    if producto['nombre'].lower() == nombre_busqueda.lower():
        print("\nProducto encontrado:")
        print(f"ID: {producto['id']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Stock: {producto['stock']}")
        encontrado = True
        break
if not encontrado:
    print("\nProducto no encontrado")


ejercicio 3
Venta de producto (sistema real)

Haz una función:

vender_producto(lista)


Debe hacer esto:

Pedir nombre del producto

Buscarlo

Si no existe → "Producto no encontrado"

Si existe:

pedir cantidad a vender

si cantidad <= 0 → "Cantidad inválida"

si cantidad > stock → "Stock insuficiente"

si es válida:

restar stock

imprimir:

Venta realizada
Stock restante: X


Ejemplo:
Producto: Coca
Stock: 10
Usuario compra 3
Nuevo stock: 7

def vender_producto(lista):
    nombre_producto = input("Ingresa el nombre del producto que deseas vender: ")
    encontrado = False

    for producto in lista:
        if producto['nombre'].lower() == nombre_producto.lower():
            encontrado = True
            cantidad_vender = int(input("Ingresa la cantidad a vender: "))
            
            if cantidad_vender <= 0:
                print("Cantidad inválida")
            elif cantidad_vender > producto['stock']:
                print("Stock insuficiente")
            else:
                producto['stock'] -= cantidad_vender
                print("Venta realizada")
                print(f"Stock restante: {producto['stock']}")
            break

    if not encontrado:
        print("Producto no encontrado")
vender_producto(productos)
print("\nPRODUCTOS ACTUALIZADOS")
for producto in productos:
    print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")   

"""