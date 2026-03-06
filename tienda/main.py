from modulos.inventario import Inventario
from modulos.ventas import Ventas
from modulos.reportes import Reportes
from sistema.carrito import Carrito


def menu_principal():

    print("\n===== SISTEMA TIENDA =====")
    print("1. Inventario")
    print("2. Realizar venta")
    print("3. Reportes")
    print("4. Salir")


def menu_inventario():

    print("\n--- INVENTARIO ---")
    print("1. Registrar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Volver")


def menu_reportes():

    print("\n--- REPORTES ---")
    print("1. Ver historial ventas")
    print("2. Total vendido")
    print("3. Volver")


def main():

    inventario = Inventario()
    ventas = Ventas(inventario)
    reportes = Reportes(ventas)

    while True:

        menu_principal()

        opcion = input("Seleccione opción: ")

        # ====================
        # INVENTARIO
        # ====================

        if opcion == "1":

            while True:

                menu_inventario()

                op = input("Seleccione opción: ")

                if op == "1":

                    nombre = input("Nombre producto: ")

                    try:
                        precio = float(input("Precio: "))
                        stock = int(input("Stock: "))
                    except ValueError:
                        print("Datos inválidos")
                        continue

                    ok = inventario.registrar_producto(nombre, precio, stock)

                    if ok:
                        print("Producto registrado")
                    else:
                        print("El producto ya existe")

                elif op == "2":

                    nombre = input("Producto a eliminar: ")

                    ok = inventario.eliminar_producto(nombre)

                    if ok:
                        print("Producto eliminado")
                    else:
                        print("Producto no encontrado")

                elif op == "3":

                    inventario.mostrar_productos()

                elif op == "4":

                    break

                else:

                    print("Opción inválida")

        # ====================
        # VENTAS
        # ====================

        elif opcion == "2":

            carrito = Carrito()

            while True:

                inventario.mostrar_productos()

                nombre = input("Producto (0 para terminar): ")

                if nombre == "0":
                    break

                if nombre not in inventario.productos:
                    print("Producto no existe")
                    continue

                try:
                    cantidad = int(input("Cantidad: "))
                except ValueError:
                    print("Cantidad inválida")
                    continue

                producto = inventario.productos[nombre]

                if cantidad > producto.stock:
                    print("Stock insuficiente")
                    continue

                carrito.agregar_producto(producto, cantidad)

            carrito.mostrar_carrito()

            total = carrito.calcular_total()

            print("TOTAL:", total)

            confirmar = input("Confirmar venta (s/n): ")

            if confirmar.lower() == "s":

                venta = ventas.realizar_venta(carrito)

                print("Venta realizada correctamente")
                print("Total:", venta.total)

            else:

                print("Venta cancelada")

        # ====================
        # REPORTES
        # ====================

        elif opcion == "3":

            while True:

                menu_reportes()

                op = input("Seleccione opción: ")

                if op == "1":

                    reportes.mostrar_historial()

                elif op == "2":

                    reportes.reporte_total()

                elif op == "3":

                    break

                else:

                    print("Opción inválida")

        # ====================
        # SALIR
        # ====================

        elif opcion == "4":

            print("Saliendo del sistema...")
            break

        else:

            print("Opción inválida")


if __name__ == "__main__":
    main()