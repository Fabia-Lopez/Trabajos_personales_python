"""
Módulo principal de la tienda.
Coordina inventario, ventas y reportes.
"""

import inventario
import ventas
import reportes


# ----------- FUNCIÓN HELPER PARA MENÚS -----------

def mostrar_menu(titulo, opciones):
    print(f"\n=== {titulo} ===")
    for clave, descripcion in opciones.items():
        print(f"{clave}. {descripcion}")
    return input("Seleccione una opción: ").strip()


# ----------- FUNCIÓN PRINCIPAL -----------

def main():

    inventario_data = inventario.cargar_inventario()
    historial_ventas = ventas.cargar_historial()
    carrito = {}

    while True:

        opcion = mostrar_menu(
            "MENÚ PRINCIPAL",
            {
                "1": "Gestión de Inventario",
                "2": "Realizar Venta",
                "3": "Reportes",
                "4": "Salir"
            }
        )

        # ================= INVENTARIO =================
        if opcion == "1":

            while True:

                sub = mostrar_menu(
                    "GESTIÓN DE INVENTARIO",
                    {
                        "1": "Registrar Producto",
                        "2": "Editar Producto",
                        "3": "Eliminar Producto",
                        "4": "Mostrar Productos",
                        "5": "Volver"
                    }
                )

                if sub == "1":
                    inventario_data = inventario.registrar_producto(inventario_data)
                    inventario.guardar_inventario(inventario_data)

                elif sub == "2":
                    inventario_data = inventario.editar_producto(inventario_data)
                    inventario.guardar_inventario(inventario_data)

                elif sub == "3":
                    inventario_data = inventario.eliminar_producto(inventario_data)
                    inventario.guardar_inventario(inventario_data)

                elif sub == "4":
                    inventario.mostrar_productos(inventario_data)

                elif sub == "5":
                    break

                else:
                    print("Opción inválida.")

        # ================= VENTAS =================
        elif opcion == "2":

            while True:

                sub = mostrar_menu(
                    "VENTAS",
                    {
                        "1": "Agregar producto al carrito",
                        "2": "Mostrar carrito",
                        "3": "Confirmar venta",
                        "4": "Cancelar y volver"
                    }
                )

                if sub == "1":
                    carrito = ventas.agregar_al_carrito(inventario_data, carrito)

                elif sub == "2":
                    ventas.mostrar_carrito(carrito)

                elif sub == "3":
                    total = ventas.confirmar_venta(inventario_data, carrito)

                    if total > 0:
                        historial_ventas = ventas.registrar_venta(
                            historial_ventas, carrito, total
                        )
                        ventas.guardar_historial(historial_ventas)
                        inventario.guardar_inventario(inventario_data)
                        carrito.clear()

                    break

                elif sub == "4":
                    carrito.clear()
                    break

                else:
                    print("Opción inválida.")

        # ================= REPORTES =================
        elif opcion == "3":

            while True:

                sub = mostrar_menu(
                    "REPORTES",
                    {
                        "1": "Mostrar Historial",
                        "2": "Ver Detalle de Venta",
                        "3": "Reporte General",
                        "4": "Volver"
                    }
                )

                if sub == "1":
                    reportes.mostrar_historial(historial_ventas)

                elif sub == "2":
                    reportes.ver_venta(historial_ventas)

                elif sub == "3":
                    reportes.reporte_ventas(historial_ventas)

                elif sub == "4":
                    break

                else:
                    print("Opción inválida.")

        # ================= SALIR =================
        elif opcion == "4":
            inventario.guardar_inventario(inventario_data)
            ventas.guardar_historial(historial_ventas)
            print("Sistema cerrado correctamente.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()