class Ventas:

    @staticmethod
    def realizar_venta(carrito, historial):

        if not carrito.items:
            print("El carrito está vacío.")
            return

        productos_vendidos = []
        total = 0

        for item in carrito.items:

            subtotal = item["precio"] * item["cantidad"]
            total += subtotal

            productos_vendidos.append({
                "nombre": item["nombre"],
                "precio": item["precio"],
                "cantidad": item["cantidad"]
            })

        venta = {
            "total": total,
            "productos": productos_vendidos
        }

        historial.registrar_venta(venta)

        carrito.vaciar()

        print("Venta realizada correctamente.")
