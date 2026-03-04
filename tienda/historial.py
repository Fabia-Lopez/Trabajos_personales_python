"""
Clase HistorialVentas
Maneja todas las ventas realizadas.
"""

from datetime import datetime


class HistorialVentas:

    def __init__(self):
        self.ventas = []

    def registrar_venta(self, productos, total):

        venta = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "productos": productos.copy(),
            "total": total
        }

        self.ventas.append(venta)

    def mostrar_historial(self):

        if not self.ventas:
            print("No hay ventas registradas.")
            return

        print("\n--- HISTORIAL DE VENTAS ---")
        for i, venta in enumerate(self.ventas, 1):
            print(f"{i}. Fecha: {venta['fecha']} | Total: ${venta['total']:.2f}")

    def ver_venta(self, indice):

        if indice < 1 or indice > len(self.ventas):
            print("Venta no válida.")
            return

        venta = self.ventas[indice - 1]

        print(f"\nFecha: {venta['fecha']}")
        print("Productos:")

        for item in venta["productos"].values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal = producto.precio * cantidad

            print(f"{producto.nombre} | Cantidad: {cantidad} | Subtotal: ${subtotal:.2f}")

        print(f"Total: ${venta['total']:.2f}")

    def guardar(self, filename="ventas.txt"):

        try:
            with open(filename, "w") as file:
                for venta in self.ventas:
                    file.write(
                        f"{venta['fecha']}|{venta['total']}\n"
                    )
            print("Historial guardado.")
        except Exception as e:
            print(f"Error al guardar historial: {e}")

    def cargar(self, filename="ventas.txt"):

        try:
            with open(filename, "r") as file:
                for line in file:
                    fecha, total = line.strip().split("|")

                    self.ventas.append({
                        "fecha": fecha,
                        "productos": {},
                        "total": float(total)
                    })

            print("Historial cargado.")

        except FileNotFoundError:
            print("Archivo de ventas no encontrado.")

        except Exception as e:
            print(f"Error al cargar historial: {e}")