"""
Módulo: ventas.py
Maneja carrito, confirmación de venta, historial y persistencia.
"""

from datetime import datetime
import tienda.sistema.inventario as inventario

def agregar_al_carrito(inventario, carrito, nombre, cantidad):

    if nombre not in inventario:
        return False, "Producto no encontrado."

    if cantidad <= 0:
        return False, "Cantidad inválida."

    stock_disponible = inventario[nombre]["stock"]
    cantidad_actual = carrito.get(nombre, {}).get("cantidad", 0)

    if cantidad + cantidad_actual > stock_disponible:
        return False, f"Stock insuficiente. Disponible: {stock_disponible}"

    if nombre in carrito:
        carrito[nombre]["cantidad"] += cantidad
    else:
        carrito[nombre] = {
            "precio": inventario[nombre]["precio"],
            "cantidad": cantidad
        }

    return True, "Producto agregado al carrito."


def mostrar_carrito(carrito):
    """Muestra el contenido del carrito."""

    if not carrito:
        print("El carrito está vacío.")
        return

    print("\n--- CARRITO ---")
    total = 0

    for nombre, datos in carrito.items():
        subtotal = datos["precio"] * datos["cantidad"]
        total += subtotal
        print(f"{nombre} | Cantidad: {datos['cantidad']} | Subtotal: ${subtotal:.2f}")

    print(f"Total actual: ${total:.2f}")


def confirmar_venta(inventario, carrito):

    if not carrito:
        return False, 0, "El carrito está vacío."

    total = sum(d["precio"] * d["cantidad"] for d in carrito.values())
    
    for nombre, datos in carrito.items():
        inventario[nombre]["stock"] -= datos["cantidad"]

    return True, total, "Venta confirmada correctamente."


def registrar_venta(historial, carrito, total):
    """Registra la venta en el historial."""

    if not carrito:
        print("No hay venta para registrar.")
        return historial

    venta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total": total,
        "productos": carrito.copy()
    }

    historial.append(venta)
    print("Venta registrada en historial.")
    return historial


def guardar_historial(historial, filename="historial.txt"):
    """Guarda el historial en archivo."""

    try:
        with open(filename, "w") as file:
            for venta in historial:
                productos_str = ";".join(
                    f"{n}:{d['precio']}:{d['cantidad']}"
                    for n, d in venta["productos"].items()
                )
                file.write(f"{venta['fecha']},{venta['total']},{productos_str}\n")

        print("Historial guardado correctamente.")

    except Exception as e:
        print(f"Error al guardar historial: {e}")


def cargar_historial(filename="historial.txt"):
    """Carga historial desde archivo."""

    historial = []

    try:
        with open(filename, "r") as file:
            for line in file:
                fecha, total, productos_str = line.strip().split(",", 2)

                productos = {}

                for producto in productos_str.split(";"):
                    nombre, precio, cantidad = producto.split(":")
                    productos[nombre] = {
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    }

                historial.append({
                    "fecha": fecha,
                    "total": float(total),
                    "productos": productos
                })

        print("Historial cargado correctamente.")

    except FileNotFoundError:
        print("No existe historial. Se iniciará vacío.")

    except Exception as e:
        print(f"Error al cargar historial: {e}")

    return historial