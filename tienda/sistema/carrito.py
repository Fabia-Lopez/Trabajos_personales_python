class Carrito:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):

        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] += cantidad
        else:
            self.productos[producto.nombre] = {
                "producto": producto,
                "cantidad": cantidad
            }

    def mostrar_carrito(self):

        if not self.productos:
            print("Carrito vacío")
            return

        print("\n--- CARRITO ---")

        for item in self.productos.values():

            producto = item["producto"]
            cantidad = item["cantidad"]

            print(producto.nombre, cantidad, producto.precio)

    def calcular_total(self):

        total = 0

        for item in self.productos.values():

            producto = item["producto"]
            cantidad = item["cantidad"]

            total += producto.precio * cantidad

        return total