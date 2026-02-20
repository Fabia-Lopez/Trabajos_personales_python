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
    

#dia 4
Ejercicio 1
Guardar venta en historial

Crea una función:

registrar_venta(historial, ticket, total)


Debe:

generar folio automático (folio = len(historial)+1)

guardar fecha y hora actual

guardar lista de productos con subtotales

guardar total

meter todo al historial

Debe imprimir:

Venta registrada con folio: 3

from datetime import datetime

def registrar_venta(historial, ticket_items, total):
    folio = len(historial) + 1
    fecha_hora = datetime.now()

    venta = {
        "folio": folio,
        "fecha_hora": fecha_hora,
        "items": ticket_items.copy(),  # Guardamos una copia del ticket
        "total": total
    }

    historial.append(venta)
    print(f"Venta registrada con folio: {folio}")


#ejercicio 2
Mostrar historial de ventas

Función:

mostrar_historial(historial)


Debe imprimir algo así:

HISTORIAL DE VENTAS
Folio: 1 | Fecha: 2026-02-12 10:20 | Total: $75
Folio: 2 | Fecha: 2026-02-12 11:05 | Total: $40


Si no hay ventas:

No hay ventas registradas

def mostrar_historial(historial):
    if len(historial) == 0:
        print("No hay ventas registradas")
        return

    print("\nHISTORIAL DE VENTAS")
    for venta in historial:
        fecha_str = venta["fecha_hora"].strftime("%Y-%m-%d %H:%M")
        print(f"Folio: {venta['folio']} | Fecha: {fecha_str} | Total: ${venta['total']:.2f}")


#ejercicio 3
Ver detalle de una venta por folio

Función:

ver_venta(historial)


Debe pedir folio.

Si existe, imprimir:

VENTA #2
Fecha: 2026-02-12 11:05
Coca - 20 x2 = 40
TOTAL: 40


Si no existe:

Venta no encontrada

def ver_venta(historial):
    if len(historial) == 0:
        print("No hay ventas registradas")
        return

    try:
        folio_busqueda = int(input("Ingresa el folio de la venta que deseas ver: "))
    except ValueError:
        print("Folio inválido")
        return

    for venta in historial:
        if venta["folio"] == folio_busqueda:
            fecha_str = venta["fecha_hora"].strftime("%Y-%m-%d %H:%M")
            print(f"\nVENTA #{venta['folio']}")
            print(f"Fecha: {fecha_str}")
            for item in venta["items"]:
                subtotal = item["precio"] * item["cantidad"]
                print(f"{item['nombre']} - ${item['precio']:.2f} x{item['cantidad']} = ${subtotal:.2f}")
            print(f"TOTAL: ${venta['total']:.2f}")
            return

    print("Venta no encontrada")

#ejercicio 4
Reporte total vendido

Función:

reporte_ventas(historial)


Debe imprimir:

total de ventas

dinero total ganado

venta más cara

venta más barata

Ejemplo:

REPORTE DE VENTAS
Total de ventas: 5
Dinero total ganado: $850
Venta más cara: Folio 3 ($250)
Venta más barata: Folio 1 ($40)



def reporte_ventas(historial):
    if len(historial) == 0:
        print("No hay ventas registradas")
        return

    total_ventas = len(historial)
    dinero_total_ganado = sum(venta["total"] for venta in historial)
    venta_mas_cara = max(historial, key=lambda x: x["total"])
    venta_mas_barata = min(historial, key=lambda x: x["total"])

    print("\nREPORTE DE VENTAS")
    print(f"Total de ventas: {total_ventas}")
    print(f"Dinero total ganado: ${dinero_total_ganado:.2f}")
    print(f"Venta más cara: Folio {venta_mas_cara['folio']} (${venta_mas_cara['total']:.2f})")
    print(f"Venta más barata: Folio {venta_mas_barata['folio']} (${venta_mas_barata['total']:.2f})")


#ejercicio 5
MENÚ NUEVO COMPLETO

Tu menú ahora debe ser:

Mostrar inventario

Agregar producto al carrito

Mostrar carrito

Confirmar venta (y guardar en historial)

Mostrar historial de ventas

Ver venta por folio

Reporte de ventas

Guardar inventario

Cargar inventario

Salir

historial = []

while True:
    print("\nMenú de Tienda")
    print("1. Mostrar inventario")
    print("2. Agregar producto al carrito")
    print("3. Mostrar carrito")
    print("4. Confirmar venta")
    print("5. Mostrar historial de ventas")
    print("6. Ver venta por folio")
    print("7. Reporte de ventas")
    print("8. Guardar inventario")
    print("9. Cargar inventario")
    print("10. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        mostrar_productos(inventario)

    elif opcion == "2":
        agregar_al_carrito(inventario, carrito)

    elif opcion == "3":
        mostrar_carrito(carrito)

    elif opcion == "4":
        total_venta = confirmar_venta(inventario, carrito)

        if total_venta > 0:
            ticket = carrito.copy()

            registrar_venta(historial, ticket, total_venta)
            guardar_ticket(ticket, total_venta)

            carrito.clear()
            print("Venta completada correctamente.")

    elif opcion == "5":
        mostrar_historial(historial)

    elif opcion == "6":
        ver_venta(historial)

    elif opcion == "7":
        reporte_ventas(historial)

    elif opcion == "8":
        guardar_productos(inventario)

    elif opcion == "9":
        cargar_productos(inventario)

    elif opcion == "10":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 10.")


#Dia 5
Ejercicio 1
Guardar historial completo

Función:

guardar_historial(historial)

Debe:

recorrer todas las ventas

escribir cada una con el formato anterior

usar modo "w" (sobrescribir)

manejar errores

FORMATO QUE USAREMOS EN ventas.txt

Ejemplo:

---VENTA---
FOLIO:1
FECHA:2026-02-20 18:30
ITEM:Coca,20,2,40
ITEM:Pan,15,1,15
TOTAL:55

Luego otra venta:

---VENTA---
FOLIO:2
FECHA:2026-02-20 19:05
ITEM:Leche,25,2,50
TOTAL:50


def guardar_historial(historial):
    try:
        with open("ventas.txt", "w") as archivo:
            for venta in historial:
                archivo.write("---VENTA---\n")
                archivo.write(f"FOLIO:{venta['folio']}\n")
                fecha_str = venta["fecha_hora"].strftime("%Y-%m-%d %H:%M")
                archivo.write(f"FECHA:{fecha_str}\n")

                for item in venta["items"]:
                    subtotal = item["precio"] * item["cantidad"]
                    archivo.write(f"ITEM:{item['nombre']},{item['precio']},{item['cantidad']},{subtotal:.2f}\n")

                archivo.write(f"TOTAL:{venta['total']:.2f}\n")

        print("Historial completo guardado en ventas.txt")

    except Exception as e:
        print(f"Error al guardar el historial: {e}")

        
#ejercicio 2
Cargar historial desde archivo

Función:

cargar_historial(historial)

Debe:

limpiar historial

leer archivo

reconstruir cada venta

convertir fecha a datetime

convertir números correctamente

agregar ventas a historial

Si no existe archivo:

Archivo no encontrado
Concepto nuevo clave

Convertir texto a datetime:

from datetime import datetime

fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

Eso convierte texto en fecha real.

def cargar_historial(historial):
    try:
        with open("ventas.txt", "r") as archivo:
            historial.clear()
            venta_actual = None

            for linea in archivo:
                linea = linea.strip()

                if linea == "---VENTA---":
                    if venta_actual is not None:
                        historial.append(venta_actual)
                    venta_actual = {"items": []}

                elif linea.startswith("FOLIO:"):
                    venta_actual["folio"] = int(linea.split(":")[1])

                elif linea.startswith("FECHA:"):
                    fecha_str = linea.split(":")[1]
                    venta_actual["fecha_hora"] = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

                elif linea.startswith("ITEM:"):
                    _, item_str = linea.split(":", 1)
                    nombre, precio_str, cantidad_str, subtotal_str = item_str.split(",")
                    item = {
                        "nombre": nombre,
                        "precio": float(precio_str),
                        "cantidad": int(cantidad_str)
                    }
                    venta_actual["items"].append(item)

                elif linea.startswith("TOTAL:"):
                    venta_actual["total"] = float(linea.split(":")[1])

            if venta_actual is not None:
                historial.append(venta_actual)

        print("Historial cargado desde ventas.txt")

    except FileNotFoundError:
        print("Archivo no encontrado")

    except Exception as e:
        print(f"Error al cargar el historial: {e}")

#ejercicio 3
Agregar al menú

Tu menú ahora tendrá:

Mostrar inventario

Agregar al carrito

Mostrar carrito

Confirmar venta

Mostrar historial

Ver venta

Reporte ventas

Guardar inventario

Cargar inventario

Guardar historial ventas

Cargar historial ventas

Salir

inventario = []
carrito = []
historial = []

while True:
    print("\nMenú de Tienda")
    print("1. Mostrar inventario")
    print("2. Agregar producto al carrito")
    print("3. Mostrar carrito")
    print("4. Confirmar venta")
    print("5. Mostrar historial de ventas")
    print("6. Ver venta por folio")
    print("7. Reporte de ventas")
    print("8. Guardar inventario")
    print("9. Cargar inventario")
    print("10. Guardar historial ventas")
    print("11. Cargar historial ventas")
    print("12. Salir")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        mostrar_productos(inventario)

    elif opcion == "2":
        agregar_al_carrito(inventario, carrito)

    elif opcion == "3":
        mostrar_carrito(carrito)

    elif opcion == "4":
        total_venta = confirmar_venta(inventario, carrito)

        if total_venta > 0:
            ticket = carrito.copy()

            registrar_venta(historial, ticket, total_venta)
            guardar_ticket(ticket, total_venta)

            carrito.clear()
            print("Venta completada correctamente.")

    elif opcion == "5":
        mostrar_historial(historial)

    elif opcion == "6":
        ver_venta(historial)

    elif opcion == "7":
        reporte_ventas(historial)

    elif opcion == "8":
        guardar_productos(inventario)

    elif opcion == "9":
        cargar_productos(inventario)

    elif opcion == "10":
        guardar_historial(historial)

    elif opcion == "11":
        cargar_historial(historial)

    elif opcion == "12":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 12.")
"""