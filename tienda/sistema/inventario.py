import json
import os
from modelos.producto import Producto


class Inventario:

    def __init__(self):
        self.productos = []
        self.archivo = "datos/inventario.json"
        self.cargar()

    def agregar_producto(self, nombre, precio, stock):

        producto = Producto(nombre, precio, stock)
        self.productos.append(producto)

        self.guardar()

    def guardar(self):

        os.makedirs("datos", exist_ok=True)

        data = [p.to_dict() for p in self.productos]

        with open(self.archivo, "w") as archivo:
            json.dump(data, archivo, indent=4)

    def cargar(self):

        try:

            with open(self.archivo, "r") as archivo:
                data = json.load(archivo)

            self.productos = [Producto.from_dict(p) for p in data]

        except FileNotFoundError:
            self.productos = []
