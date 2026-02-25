"""
Módulo: reportes.py
Maneja visualización de historial y generación de reportes.
"""

def mostrar_historial(historial):
    """Muestra resumen del historial de ventas."""

    if not historial:
        print("El historial está vacío.")
        return

    print("\n--- HISTORIAL DE VENTAS ---")

    for i, venta in enumerate(historial, start=1):
        print(f"{i}. Fecha: {venta['fecha']} | Total: ${venta['total']:.2f}")


def ver_venta(historial):
    """Muestra los detalles completos de una venta específica."""

    if not historial:
        print("El historial está vacío.")
        return

    mostrar_historial(historial)

    try:
        indice = int(input("Seleccione número de venta: ")) - 1
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if indice < 0 or indice >= len(historial):
        print("Venta no válida.")
        return

    venta = historial[indice]

    print(f"\n--- DETALLE DE VENTA ---")
    print(f"Fecha: {venta['fecha']}")

    total_calculado = 0

    for nombre, datos in venta["productos"].items():
        subtotal = datos["precio"] * datos["cantidad"]
        total_calculado += subtotal

        print(
            f"{nombre} | "
            f"Precio: ${datos['precio']:.2f} | "
            f"Cantidad: {datos['cantidad']} | "
            f"Subtotal: ${subtotal:.2f}"
        )

    print(f"Total registrado: ${venta['total']:.2f}")
    print(f"Total recalculado: ${total_calculado:.2f}")


def reporte_ventas(historial):
    """Genera estadísticas generales de ventas."""

    if not historial:
        print("No hay ventas registradas.")
        return

    total_vendido = sum(v["total"] for v in historial)
    numero_ventas = len(historial)
    promedio = total_vendido / numero_ventas

    # Producto más vendido
    contador_productos = {}

    for venta in historial:
        for nombre, datos in venta["productos"].items():
            contador_productos[nombre] = (
                contador_productos.get(nombre, 0) + datos["cantidad"]
            )

    producto_top = max(contador_productos, key=contador_productos.get)

    print("\n--- REPORTE GENERAL ---")
    print(f"Total vendido: ${total_vendido:.2f}")
    print(f"Número de ventas: {numero_ventas}")
    print(f"Promedio por venta: ${promedio:.2f}")
    print(f"Producto más vendido: {producto_top}")