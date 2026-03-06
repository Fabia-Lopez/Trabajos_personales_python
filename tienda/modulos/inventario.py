
""" Módulo de gestión de inventario """
from sistema.producto import Producto


class Inventario:

    def __init__(self):
        self.productos = {}

    def registrar_producto(self, nombre, precio, stock):

        if nombre in self.productos:
            return False

        self.productos[nombre] = Producto(nombre, precio, stock)

        return True

    def eliminar_producto(self, nombre):

        if nombre not in self.productos:
            return False

        del self.productos[nombre]

        return True

    def mostrar_productos(self):

        if not self.productos:
            print("Inventario vacío")
            return

        print("\n--- INVENTARIO ---")

        for producto in self.productos.values():

            print(
                producto.nombre,
                producto.precio,
                producto.stock
            )