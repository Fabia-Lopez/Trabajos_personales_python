import json
import os


class Historial:

    def __init__(self):
        self.ventas = []
        self.archivo = "datos/ventas.json"
        self.cargar()

    def registrar_venta(self, venta):

        self.ventas.append(venta)
        self.guardar()

        print("Venta registrada.")

    def guardar(self):

        os.makedirs("datos", exist_ok=True)

        with open(self.archivo, "w") as archivo:
            json.dump(self.ventas, archivo, indent=4)

    def cargar(self):

        try:

            with open(self.archivo, "r") as archivo:
                self.ventas = json.load(archivo)

        except FileNotFoundError:
            self.ventas = []

    def mostrar_ventas(self):

        if not self.ventas:
            print("No hay ventas registradas.")
            return

        for i, venta in enumerate(self.ventas, 1):

            print(f"\nVenta {i}")
            print("Total:", venta["total"])

            for producto in venta["productos"]:
                print(
                    producto["nombre"],
                    "-",
                    producto["cantidad"],
                    "x",
                    producto["precio"]
                )
