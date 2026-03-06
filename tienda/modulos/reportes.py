class Reportes:

    def __init__(self, ventas):

        self.ventas = ventas

    def mostrar_historial(self):

        if not self.ventas.historial:
            print("No hay ventas")
            return

        print("\n--- HISTORIAL ---")

        for venta in self.ventas.historial:

            print(venta.fecha, venta.total)

    def reporte_total(self):

        total = sum(v.total for v in self.ventas.historial)

        print("Total vendido:", total)