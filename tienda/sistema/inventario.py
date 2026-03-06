from modelos.producto import Producto


class Inventario:

    def __init__(self):
        self.productos = {}

    def registrar_producto(self, nombre, precio, stock):

        if nombre in self.productos:
            print("El producto ya existe.")
            return

        self.productos[nombre] = Producto(nombre, precio, stock)
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

        for producto in self.productos.values():
            print(producto)

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

    def cargar_inventario(self):

        try:
            with open("datos/inventario.txt", "r") as archivo:

                for linea in archivo:

                    nombre, precio, stock = linea.strip().split(",")

                    self.productos[nombre] = Producto(
                        nombre,
                        float(precio),
                        int(stock)
                    )

            print("Inventario cargado.")

        except FileNotFoundError:
            print("No existe archivo de inventario.")