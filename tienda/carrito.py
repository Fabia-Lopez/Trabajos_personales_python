"""
Clase Carrito
Maneja los productos seleccionados para una venta.
"""

class Carrito:

    def __init__(self):
        self.productos = {}  # {nombre: {"producto": Producto, "cantidad": int}}

    def agregar(self, producto, cantidad):

        if cantidad <= 0:
            return False, "Cantidad inválida."

        if cantidad > producto.stock:
            return False, f"Stock insuficiente. Disponible: {producto.stock}"

        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] += cantidad
        else:
            self.productos[producto.nombre] = {
                "producto": producto,
                "cantidad": cantidad
            }

        return True, "Producto agregado al carrito."

    def mostrar(self):

        if not self.productos:
            print("Carrito vacío.")
            return

        print("\n--- CARRITO ---")
        total = 0

        for item in self.productos.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal = producto.precio * cantidad
            total += subtotal

            print(f"{producto.nombre} | Cantidad: {cantidad} | Subtotal: ${subtotal:.2f}")

        print(f"Total: ${total:.2f}")

    def calcular_total(self):
        return sum(
            item["producto"].precio * item["cantidad"]
            for item in self.productos.values()
        )

    def confirmar(self):

        if not self.productos:
            return False, 0, "El carrito está vacío."

        total = self.calcular_total()

        for item in self.productos.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            producto.reducir_stock(cantidad)

        return True, total, "Venta confirmada correctamente."

    def limpiar(self):
        self.productos.clear()