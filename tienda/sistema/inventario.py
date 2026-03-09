from modelos.producto import Producto
import json


class Inventario:

    def __init__(self):
        self.productos = {}
        self.cargar()

    def registrar_producto(self, nombre, precio, stock):

        if nombre in self.productos:
            print("El producto ya existe.")
            return

        producto= Producto(nombre, precio, stock)
        self.productos.append(producto)
        self.guardar()
        print("Producto registrado correctamente.")

    def eliminar_producto(self, nombre):

        if nombre not in self.productos:
            print("Producto no encontrado.")
            return

        del self.productos[nombre]
        print("Producto eliminado.")

    def mostrar_productos(self):

        if not self.productos:
            print("Inventario vacío")
            return

        print("\n--- INVENTARIO ---")

        for i, producto in enumerate(self.productos.values(), 1):
            print(f"{i}. {producto}")

    def buscar_producto(self, nombre):

        for producto in self.productos.values():

            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def guardar_inventario(self):

        try:
            with open("datos/inventario.txt", "w") as archivo:

                for producto in self.productos.values():

                    archivo.write(
                        f"{producto.nombre},{producto.precio},{producto.stock}\n"
                    )

            print("Inventario guardado.")

        except Exception as e:
            print("Error al guardar:", e)

    def guardar(self):

        data = [p.to_dict() for p in self.productos.values()]
        with open("datos/inventario.json", "w") as archivo:
            json.dump(data, archivo, indent=4)

    def cargar(self):

        try:
            with open("datos/inventario.json", "r") as archivo:
                data = json.load(archivo)
            self.productos =[Producto.from_dict(p) for p in data]
        except FileNotFoundError:
            self.productos = []
        except Exception as e:
            print("Error al cargar:", e)
            self.productos = []