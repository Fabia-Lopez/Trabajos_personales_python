"""
Módulo: inventario.py
Maneja todas las operaciones relacionadas con productos:
registrar, editar, eliminar, mostrar, guardar y cargar inventario.
"""
from producto import Producto

def registrar_producto(inventario, nombre, precio, stock):

    if nombre in inventario:
        return False, "El producto ya existe."

    inventario[nombre] = Producto(nombre, precio, stock)

    return True, "Producto registrado correctamente."


def editar_producto(inventario, nombre, precio, cantidad, stock):

    if nombre not in inventario:
        return False, "Producto no encontrado."

    if precio < 0 or cantidad < 0 or stock < 0:
        return False, "Los valores no pueden ser negativos."

    inventario[nombre]["precio"] = precio
    inventario[nombre]["cantidad"] = cantidad
    inventario[nombre]["stock"] = stock

    return True, "Producto actualizado correctamente."


def eliminar_producto(inventario, nombre):

    if nombre not in inventario:
        return False, "Producto no encontrado."

    del inventario[nombre]
    return True, "Producto eliminado correctamente."


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