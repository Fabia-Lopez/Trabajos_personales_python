"""
Módulo: inventario.py
Maneja todas las operaciones relacionadas con productos:
registrar, editar, eliminar, mostrar, guardar y cargar inventario.
"""

def registrar_producto(inventario):
    """Registra un nuevo producto en el inventario."""
    
    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre in inventario:
        print("Ese producto ya existe.")
        return inventario

    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
    except ValueError:
        print("Error: Precio, cantidad y stock deben ser números válidos.")
        return inventario

    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad,
        "stock": stock
    }

    print(f"Producto '{nombre}' registrado exitosamente.")
    return inventario


def editar_producto(inventario):
    """Edita un producto existente en el inventario."""
    
    nombre = input("Ingrese el nombre del producto a editar: ").strip()

    if nombre not in inventario:
        print("Producto no encontrado.")
        return inventario

    try:
        precio = float(input("Ingrese el nuevo precio: "))
        cantidad = int(input("Ingrese la nueva cantidad: "))
        stock = int(input("Ingrese el nuevo stock: "))
    except ValueError:
        print("Error: Datos inválidos.")
        return inventario

    inventario[nombre]["precio"] = precio
    inventario[nombre]["cantidad"] = cantidad
    inventario[nombre]["stock"] = stock

    print(f"Producto '{nombre}' actualizado correctamente.")
    return inventario


def eliminar_producto(inventario):
    """Elimina un producto del inventario."""
    
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print("Producto no encontrado.")

    return inventario


def mostrar_productos(inventario):
    """Muestra todos los productos del inventario."""
    
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- INVENTARIO ---")
    for nombre, datos in inventario.items():
        print(
            f"Nombre: {nombre} | "
            f"Precio: ${datos['precio']:.2f} | "
            f"Cantidad: {datos['cantidad']} | "
            f"Stock: {datos['stock']}"
        )


def guardar_inventario(inventario, filename="inventario.txt"):
    """Guarda el inventario en un archivo de texto."""

    try:
        with open(filename, "w") as file:
            for nombre, datos in inventario.items():
                file.write(
                    f"{nombre},{datos['precio']},{datos['cantidad']},{datos['stock']}\n"
                )
        print("Inventario guardado exitosamente.")
    except Exception as e:
        print(f"Error al guardar inventario: {e}")


def cargar_inventario(filename="inventario.txt"):
    """Carga el inventario desde un archivo de texto."""

    inventario = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                nombre, precio, cantidad, stock = line.strip().split(",")

                inventario[nombre] = {
                    "precio": float(precio),
                    "cantidad": int(cantidad),
                    "stock": int(stock)
                }

        print("Inventario cargado exitosamente.")

    except FileNotFoundError:
        print("Archivo no encontrado. Se iniciará inventario vacío.")

    except Exception as e:
        print(f"Error al cargar inventario: {e}")

    return inventario