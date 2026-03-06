class Ventas:

    def confirmar_venta(self, inventario, carrito, historial):

        if not carrito.items:
            print("Carrito vacío.")
            return

        total = 0

        for nombre, datos in carrito.items.items():

            subtotal = datos["precio"] * datos["cantidad"]
            total += subtotal

        print("Total a pagar:", total)

        confirmacion = input("Confirmar venta (s/n): ")

        if confirmacion.lower() != "s":
            print("Venta cancelada.")
            return

        for nombre, datos in carrito.items.items():

            producto = inventario.productos[nombre]
            producto.reducir_stock(datos["cantidad"])

        historial.registrar_venta(carrito)

        carrito.limpiar()

        print("Venta completada.")