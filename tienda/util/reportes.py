class Reportes:

    def reporte_ventas(self, historial):

        if not historial.ventas:
            print("No hay ventas registradas.")
            return

        total = 0

        for venta in historial.ventas:
            total += venta["total"]

        print("\n--- REPORTE ---")
        print("Ventas totales:", len(historial.ventas))
        print("Total vendido:", total)