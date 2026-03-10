from sistema.inventario import Inventario
from sistema.carrito import Carrito
from sistema.historial import Historial

from util.ventas import Ventas
from util.reportes import Reportes


def main():

    inventario = Inventario()
    carrito = Carrito()
    historial = Historial()

    ventas = Ventas()
    reportes = Reportes()

    inventario.cargar()

    while True:

        print("\n===== SISTEMA TIENDA =====")
        print("1. Inventario")
        print("2. Agregar al carrito")
        print("3. Mostrar carrito")
        print("4. Confirmar venta")
        print("5. Historial ventas")
        print("6. Reporte ventas")
        print("7. Salir")

        opcion = input("Selecciona opción: ")

        if opcion == "1":

            print("\n--- INVENTARIO ---")
            print("1. Registrar producto")
            print("2. Eliminar producto")
            print("3. Mostrar productos")

            op = input("Opción: ")

            if op == "1":

                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))

                inventario.agregar_producto(nombre, precio, stock)

            elif op == "2":

                nombre = input("Producto a eliminar: ")
                inventario.eliminar_producto(nombre)

            elif op == "3":

                inventario.mostrar_productos()

        elif opcion == "2":

            nombre = input("Producto: ")
            cantidad = int(input("Cantidad: "))

            carrito.agregar_producto(inventario, nombre, cantidad)

        elif opcion == "3":

            carrito.mostrar_carrito()

        elif opcion == "4":

            ventas.realizar_venta(carrito, historial)

        elif opcion == "5":

            historial.mostrar_ventas()

        elif opcion == "6":

            reportes.reporte_ventas(historial)

        elif opcion == "7":

            inventario.guardar()
            historial.guardar()
            print("Sistema cerrado.")
            break


if __name__ == "__main__":
    main()