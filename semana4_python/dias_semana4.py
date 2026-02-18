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


#dia 2
Ejercicio 1
Editar producto (por ID)

Crea una función:

editar_producto(lista)


Debe hacer esto:

Pedir ID del producto
Buscarlo
Si existe, permitir editar:

nombre

precio

stock

Validaciones:

nombre no vacío

precio > 0

stock >= 0

Si no existe:

Producto no encontrado

def editar_producto(lista):
    if len(lista) == 0:
        print("No hay productos registrados.")
        return

    try:
        id_producto = int(input("Ingresa el ID del producto que deseas editar: "))
    except ValueError:
        print("ID inválido")
        return

    for producto in lista:
        if producto["id"] == id_producto:

            nuevo_nombre = input("Nuevo nombre: ").strip()
            if nuevo_nombre == "":
                print("Nombre no puede estar vacío")
                return

            try:
                nuevo_precio = float(input("Nuevo precio: "))
                if nuevo_precio <= 0:
                    print("Precio debe ser mayor a 0")
                    return
            except ValueError:
                print("Precio inválido")
                return

            try:
                nuevo_stock = int(input("Nuevo stock: "))
                if nuevo_stock < 0:
                    print("Stock no puede ser negativo")
                    return
            except ValueError:
                print("Stock inválido")
                return

            producto["nombre"] = nuevo_nombre
            producto["precio"] = nuevo_precio
            producto["stock"] = nuevo_stock

            print("Producto actualizado exitosamente")
            return

    print("Producto no encontrado")



#ejercicio 2
Eliminar producto (por ID)

Función:

eliminar_producto(lista)


Debe:

pedir ID
buscar producto
si existe eliminarlo
imprimir:

Producto eliminado correctamente


Si no existe:

Producto no encontrado

def eliminar_producto(lista):
    if len(lista) == 0:
        print("No hay productos registrados.")
        return

    try:
        id_producto = int(input("Ingresa el ID del producto que deseas eliminar: "))
    except ValueError:
        print("ID inválido")
        return

    for i, producto in enumerate(lista):
        if producto["id"] == id_producto:
            eliminado = lista.pop(i)
            print(f"Producto eliminado correctamente: {eliminado['nombre']}")
            return

    print("Producto no encontrado")



#ejercicio 3
Reporte del inventario

Función:

reporte_inventario(lista)


Debe imprimir:

REPORTE DE INVENTARIO
Total productos: 5
Producto más caro: Coca ($20)
Producto más barato: Pan ($15)
Total unidades en stock: 40
Valor total del inventario: $850


Valor total = precio * stock

def reporte_inventario(lista):
    if len(lista) == 0:
        print("No hay productos en el inventario.")
        return

    total_productos = len(lista)
    producto_mas_caro = max(lista, key=lambda x: x["precio"])
    producto_mas_barato = min(lista, key=lambda x: x["precio"])
    total_unidades_stock = sum(producto["stock"] for producto in lista)
    valor_total_inventario = sum(producto["precio"] * producto["stock"] for producto in lista)

    print("\nREPORTE DE INVENTARIO")
    print(f"Total productos: {total_productos}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']:.2f})")
    print(f"Producto más barato: {producto_mas_barato['nombre']} (${producto_mas_barato['precio']:.2f})")
    print(f"Total unidades en stock: {total_unidades_stock}")
    print(f"Valor total del inventario: ${valor_total_inventario:.2f}")


#ejercicio 4
Guardar inventario en archivo TXT

Función:

guardar_productos(lista)


Debe guardar en:

productos.txt

Formato:

1,Coca,20.0,15
2,Pan,15.0,10

def guardar_productos(lista):
    try:
        with open("productos.txt", "w") as archivo:
            for producto in lista:
                linea = f"{producto['id']},{producto['nombre']},{producto['precio']},{producto['stock']}\n"
                archivo.write(linea)

        print("Productos guardados en productos.txt")

    except Exception as e:
        print(f"Error al guardar: {e}")



#ejercicio 5
Cargar inventario desde archivo TXT

Función:

cargar_productos(lista)


Debe:

leer productos.txt
vaciar lista antes de cargar (lista.clear())
convertir a tipos correctos (int, float)

Si no existe:

Archivo no encontrado

def cargar_productos(lista):
    try:
        with open("productos.txt", "r") as archivo:
            lista.clear()

            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue

                id_str, nombre, precio_str, stock_str = linea.split(",")

                producto = {
                    "id": int(id_str),
                    "nombre": nombre,
                    "precio": float(precio_str),
                    "stock": int(stock_str)
                }

                lista.append(producto)

        print("Productos cargados desde productos.txt")

    except FileNotFoundError:
        print("Archivo no encontrado")

    except Exception as e:
        print(f"Error al cargar: {e}")



#ejercicio 6
Menú completo del inventario

El menú debe tener:

1. Registrar producto
2. Mostrar productos
3. Buscar producto por nombre
4. Vender producto
5. Editar producto
6. Eliminar producto
7. Reporte inventario
8. Guardar en archivo
9. Cargar desde archivo
10. Salir

productos = []

while True:
    print("\nMenú de Inventario")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por nombre")
    print("4. Vender producto")
    print("5. Editar producto")
    print("6. Eliminar producto")
    print("7. Reporte inventario")
    print("8. Guardar en archivo")
    print("9. Cargar desde archivo")
    print("10. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        registrar_producto(productos)

    elif opcion == "2":
        mostrar_productos(productos)

    elif opcion == "3":
        buscar_producto(productos)

    elif opcion == "4":
        vender_producto(productos)

    elif opcion == "5":
        editar_producto(productos)

    elif opcion == "6":
        eliminar_producto(productos)

    elif opcion == "7":
        reporte_inventario(productos)

    elif opcion == "8":
        guardar_productos(productos)

    elif opcion == "9":
        cargar_productos(productos)

    elif opcion == "10":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 10.")


#dia 3
Ejercicio 1
Agregar producto al carrito

Crea una función:

agregar_al_carrito(inventario, carrito)


Debe:

pedir ID del producto

pedir cantidad

validar:

cantidad > 0

que exista el producto

que haya stock suficiente

si es válido agregarlo al carrito así:

{"id": 1, "nombre": "Coca", "precio": 20, "cantidad": 3}


OJO: NO debe descontar stock todavía.

def agregar_al_carrito(inventario, carrito):
    try:
        id_producto = int(input("Ingresa el ID del producto: "))
    except ValueError:
        print("ID inválido")
        return

    producto_encontrado = None
    for producto in inventario:
        if producto["id"] == id_producto:
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("Producto no encontrado")
        return

    try:
        cantidad = int(input("Ingresa la cantidad: "))
        if cantidad <= 0:
            print("Cantidad inválida")
            return
    except ValueError:
        print("Cantidad inválida")
        return

    if cantidad > producto_encontrado["stock"]:
        print("Stock insuficiente")
        return

    # 🔥 Si ya existe en el carrito, solo sumamos la cantidad
    for item in carrito:
        if item["id"] == id_producto:
            if item["cantidad"] + cantidad > producto_encontrado["stock"]:
                print("Stock insuficiente para agregar esa cantidad extra")
                return

            item["cantidad"] += cantidad
            print(f"Cantidad actualizada: {item['nombre']} x{item['cantidad']}")
            return

    # Si no existe, se agrega normal
    carrito.append({
        "id": producto_encontrado["id"],
        "nombre": producto_encontrado["nombre"],
        "precio": producto_encontrado["precio"],
        "cantidad": cantidad
    })

    print(f"{cantidad} unidades de {producto_encontrado['nombre']} agregadas al carrito")

#ejercicio 2
Mostrar carrito

Función:

mostrar_carrito(carrito)


Debe imprimir:

CARRITO ACTUAL
1. Coca - $20 x3 = $60
2. Pan - $15 x1 = $15
TOTAL: $75


Si carrito está vacío:

Carrito vacío

def mostrar_carrito(carrito):
    if len(carrito) == 0:
        print("Carrito vacío")
        return

    print("\nCARRITO ACTUAL")
    total = 0

    for i, item in enumerate(carrito, start=1):
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{i}. {item['nombre']} - ${item['precio']:.2f} x{item['cantidad']} = ${subtotal:.2f}")

    print(f"TOTAL: ${total:.2f}")


#ejercicio 3
Confirmar venta (descontar stock)

Función:

confirmar_venta(inventario, carrito)


Debe:

recorrer carrito
descontar stock en inventario
calcular total
imprimir ticket final
vaciar carrito (carrito.clear())

Si carrito está vacío:

No hay productos en el carrito

def confirmar_venta(inventario, carrito):
    if len(carrito) == 0:
        print("No hay productos en el carrito")
        return 0

    # Validar que todo tenga stock antes de descontar
    for item in carrito:
        for producto in inventario:
            if producto["id"] == item["id"]:
                if item["cantidad"] > producto["stock"]:
                    print(f"Stock insuficiente para {producto['nombre']}. Venta cancelada.")
                    return 0

    # Descontar stock
    total = 0
    for item in carrito:
        for producto in inventario:
            if producto["id"] == item["id"]:
                producto["stock"] -= item["cantidad"]
                subtotal = item["precio"] * item["cantidad"]
                total += subtotal

    # Imprimir ticket
    print("\n===== TICKET DE VENTA =====")
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        print(f"{item['nombre']} - ${item['precio']:.2f} x{item['cantidad']} = ${subtotal:.2f}")

    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("===========================")

    carrito.clear()
    return total

#ejercicio 4
Guardar ticket en archivo

Función:

guardar_ticket(carrito, total)


Debe guardar en:

ventas.txt

Formato recomendado:

--- NUEVA VENTA ---
Coca,20,3,60
Pan,15,1,15
TOTAL: 75


def guardar_ticket(ticket_items, total):
    try:
        with open("ventas.txt", "a") as archivo:
            archivo.write("\n--- NUEVA VENTA ---\n")

            for item in ticket_items:
                subtotal = item["precio"] * item["cantidad"]
                archivo.write(f"{item['nombre']},{item['precio']},{item['cantidad']},{subtotal:.2f}\n")

            archivo.write(f"TOTAL: {total:.2f}\n")

        print("Ticket guardado en ventas.txt")

    except Exception as e:
        print(f"Error al guardar el ticket: {e}")



#ejercicio 5
Menú completo (modo tienda real)

Menú:

1. Mostrar inventario
2. Agregar producto al carrito
3. Mostrar carrito
4. Confirmar venta
5. Guardar inventario
6. Cargar inventario
7. Salir


inventario = []
carrito = []

while True:
    print("\nMenú de Tienda")
    print("1. Mostrar inventario")
    print("2. Agregar producto al carrito")
    print("3. Mostrar carrito")
    print("4. Confirmar venta")
    print("5. Guardar inventario")
    print("6. Cargar inventario")
    print("7. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        mostrar_productos(inventario)

    elif opcion == "2":
        agregar_al_carrito(inventario, carrito)

    elif opcion == "3":
        mostrar_carrito(carrito)

    elif opcion == "4":
        confirmar_venta(inventario, carrito)

    elif opcion == "5":
        guardar_productos(inventario)

    elif opcion == "6":
        cargar_productos(inventario)

    elif opcion == "7":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 7.")
    
"""