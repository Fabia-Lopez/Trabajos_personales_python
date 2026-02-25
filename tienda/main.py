"""
Módulo principal de la tienda.
Coordina inventario, ventas y reportes.
"""

import inventario
import ventas
import reportes


def main():

    inventario_data = inventario.cargar_inventario()
    historial_ventas = ventas.cargar_historial()
    carrito = {}

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Inventario")
        print("2. Realizar Venta")
        print("3. Reportes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        # ---------------- INVENTARIO ----------------
        if opcion == "1":

            while True:
                print("\n--- GESTIÓN DE INVENTARIO ---")
                print("1. Registrar Producto")
                print("2. Editar Producto")
                print("3. Eliminar Producto")
                print("4. Mostrar Productos")
                print("5. Volver")

                sub = input("Seleccione una opción: ").strip()

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

        # ---------------- VENTAS ----------------
        elif opcion == "2":

            while True:
                print("\n--- VENTAS ---")
                print("1. Agregar producto al carrito")
                print("2. Mostrar carrito")
                print("3. Confirmar venta")
                print("4. Cancelar y volver")

                sub = input("Seleccione una opción: ").strip()

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

        # ---------------- REPORTES ----------------
        elif opcion == "3":

            while True:
                print("\n--- REPORTES ---")
                print("1. Mostrar Historial")
                print("2. Ver Detalle de Venta")
                print("3. Reporte General")
                print("4. Volver")

                sub = input("Seleccione una opción: ").strip()

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

        # ---------------- SALIR ----------------
        elif opcion == "4":
            inventario.guardar_inventario(inventario_data)
            ventas.guardar_historial(historial_ventas)
            print("Sistema cerrado correctamente.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()