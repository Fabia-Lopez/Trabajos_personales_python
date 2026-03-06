from sistema.carrito import Carrito
from sistema.venta import Venta


class Ventas:

    def __init__(self, inventario):

        self.inventario = inventario
        self.historial = []

    def realizar_venta(self, carrito):

        total = carrito.calcular_total()

        venta = Venta(carrito.productos.copy(), total)

        self.historial.append(venta)

        for item in carrito.productos.values():

            producto = item["producto"]
            cantidad = item["cantidad"]

            self.inventario.productos[producto.nombre].stock -= cantidad

        return venta