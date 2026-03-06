from datetime import datetime


class Historial:

    def __init__(self):
        self.ventas = []

    def registrar_venta(self, carrito):

        total = 0

        for datos in carrito.items.values():
            total += datos["precio"] * datos["cantidad"]

        venta = {
            "fecha": datetime.now(),
            "productos": carrito.items.copy(),
            "total": total
        }

        self.ventas.append(venta)

        print("Venta registrada.")

    def mostrar_historial(self):

        if not self.ventas:
            print("No hay ventas.")
            return

        for i, venta in enumerate(self.ventas, start=1):

            print(f"\nVenta {i}")
            print("Fecha:", venta["fecha"])
            print("Total:", venta["total"])