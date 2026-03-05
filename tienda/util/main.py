"""
Módulo principal de la tienda.

Coordina todo el sistema:
- Inventario
- Ventas
- Reportes
"""

from sistema import inventario
import ventas
import reportes



def main():

    inventario_data = inventario.cargar_inventario()
    carrito = {}
    historial_ventas = []

    while True:

        print("\n===== SISTEMA TIENDA =====")
        print("1. Gestionar Inventario")
        print("2. Realizar Venta")
        print("3. Ver Reportes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        # INVENTARIO
        if opcion == "1":

            while True:

                print("\n--- INVENTARIO ---")
                print("1. Registrar producto")
                print("2. Editar producto")
                print("3. Eliminar producto")
                print("4. Mostrar productos")
                print("5. Volver")

                sub = input("Seleccione una opción: ")

                if sub == "1":

                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))
                    stock = int(input("Stock: "))

                    ok, mensaje = inventario.registrar_producto(
                        inventario_data, nombre, precio, stock
                    )
                    print(mensaje)

                    if ok:
                        inventario.guardar_inventario(inventario_data)

                elif sub == "2":

                    nombre = input("Producto a editar: ")
                    precio = float(input("Nuevo precio: "))
                    cantidad = int(input("Cantidad: "))
                    stock = int(input("Stock: "))

                    ok, mensaje = inventario.editar_producto(
                        inventario_data, nombre, precio, cantidad, stock
                    )
                    print(mensaje)

                    if ok:
                        inventario.guardar_inventario(inventario_data)

                elif sub == "3":

                    nombre = input("Producto a eliminar: ")

                    ok, mensaje = inventario.eliminar_producto(
                        inventario_data, nombre
                    )
                    print(mensaje)

                    if ok:
                        inventario.guardar_inventario(inventario_data)

                elif sub == "4":

                    inventario.mostrar_productos(inventario_data)

                elif sub == "5":

                    break

                else:
                    print("Opción inválida")

        # VENTAS
        elif opcion == "2":

            carrito = ventas.agregar_al_carrito(inventario_data, carrito)

            ventas.mostrar_carrito(carrito)

            if ventas.confirmar_venta(inventario_data, carrito):

                historial_ventas = ventas.registrar_venta(
                    historial_ventas, carrito
                )

                carrito.clear()

                inventario.guardar_inventario(inventario_data)

        # REPORTES
        elif opcion == "3":

            while True:

                print("\n--- REPORTES ---")
                print("1. Historial de ventas")
                print("2. Ver venta específica")
                print("3. Reporte de ventas")
                print("4. Volver")

                sub = input("Seleccione una opción: ")

                if sub == "1":

                    reportes.mostrar_historial(historial_ventas)

                elif sub == "2":

                    reportes.ver_venta(historial_ventas)

                elif sub == "3":

                    reportes.reporte_ventas(historial_ventas)

                elif sub == "4":

                    break

                else:
                    print("Opción inválida")

        # SALIR
        elif opcion == "4":

            inventario.guardar_inventario(inventario_data)
            ventas.guardar_historial(historial_ventas)

            print("Sistema cerrado correctamente.")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":
    main()