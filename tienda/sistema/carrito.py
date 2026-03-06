class Carrito:

    def __init__(self):
        self.items = {}

    def agregar_producto(self, inventario, nombre, cantidad):

        if nombre not in inventario.productos:
            print("Producto no existe.")
            return

        producto = inventario.productos[nombre]

        if cantidad > producto.stock:
            print("No hay suficiente stock.")
            return

        if nombre in self.items:
            self.items[nombre]["cantidad"] += cantidad
        else:
            self.items[nombre] = {
                "precio": producto.precio,
                "cantidad": cantidad
            }

        print("Producto agregado al carrito.")

    def mostrar_carrito(self):

        if not self.items:
            print("Carrito vacío")
            return

        print("\n--- CARRITO ---")

        for nombre, datos in self.items.items():

            subtotal = datos["precio"] * datos["cantidad"]

            print(
                f"{nombre} | "
                f"Precio: {datos['precio']} | "
                f"Cantidad: {datos['cantidad']} | "
                f"Subtotal: {subtotal}"
            )

    def limpiar(self):
        self.items.clear()