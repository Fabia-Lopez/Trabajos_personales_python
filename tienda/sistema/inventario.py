"""
Módulo: inventario.py
Clase Inventario orientada a objetos.
"""

from tienda.modelos.producto import Producto


class Inventario:

    def __init__(self):
        self.productos = {}

    def registrar_producto(self, nombre, precio, stock):

        if nombre in self.productos:
            return False, "El producto ya existe."

        self.productos[nombre] = Producto(nombre, precio, stock)
        return True, "Producto registrado correctamente."

    def editar_producto(self, nombre, precio, stock):

        if nombre not in self.productos:
            return False, "Producto no encontrado."

        producto = self.productos[nombre]
        producto.precio = precio
        producto.stock = stock

        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, nombre):

        if nombre not in self.productos:
            return False, "Producto no encontrado."

        del self.productos[nombre]
        return True, "Producto eliminado correctamente."

    def obtener_producto(self, nombre):
        return self.productos.get(nombre)

    def mostrar_productos(self):

        if not self.productos:
            print("Inventario vacío.")
            return

        print("\n--- INVENTARIO ---")
        for producto in self.productos.values():
            print(producto.mostrar_info())

    def guardar_inventario(self, filename="inventario.txt"):

        try:
            with open(filename, "w") as file:
                for producto in self.productos.values():
                    file.write(
                        f"{producto.nombre},{producto.precio},{producto.stock}\n"
                    )
            print("Inventario guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def cargar_inventario(self, filename="inventario.txt"):

        try:
            with open(filename, "r") as file:
                for line in file:
                    nombre, precio, stock = line.strip().split(",")

                    self.productos[nombre] = Producto(
                        nombre,
                        float(precio),
                        int(stock)
                    )

            print("Inventario cargado exitosamente.")

        except FileNotFoundError:
            print("Archivo no encontrado. Se iniciará inventario vacío.")

        except Exception as e:
            print(f"Error al cargar inventario: {e}")