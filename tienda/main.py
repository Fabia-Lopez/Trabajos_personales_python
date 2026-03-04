"""
Módulo principal de la tienda.
Versión completamente orientada a objetos.
"""

from inventario import Inventario
from carrito import Carrito
from historial import HistorialVentas



# ----------- FUNCIÓN HELPER PARA MENÚS -----------

def mostrar_menu(titulo, opciones):
    print(f"\n=== {titulo} ===")
    for clave, descripcion in opciones.items():
        print(f"{clave}. {descripcion}")
    return input("Seleccione una opción: ").strip()


# ----------- FUNCIÓN PRINCIPAL -----------

def main():

    inventario = Inventario()
    inventario.cargar_inventario()

    carrito = Carrito()
    historial = HistorialVentas()
    historial.cargar()

    while True:

        opcion = mostrar_menu(
            "MENÚ PRINCIPAL",
            {
                "1": "Gestión de Inventario",
                "2": "Ventas",
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
                    try:
                        nombre = input("Nombre: ")
                        precio = float(input("Precio: "))
                        stock = int(input("Stock: "))
                    except ValueError:
                        print("Datos inválidos.")
                        continue

                    exito, mensaje = inventario.registrar_producto(
                        nombre, precio, stock
                    )
                    print(mensaje)

                elif sub == "2":
                    try:
                        nombre = input("Nombre del producto a editar: ")
                        precio = float(input("Nuevo precio: "))
                        stock = int(input("Nuevo stock: "))
                    except ValueError:
                        print("Datos inválidos.")
                        continue

                    exito, mensaje = inventario.editar_producto(
                        nombre, precio, stock
                    )
                    print(mensaje)

                elif sub == "3":
                    nombre = input("Nombre del producto a eliminar: ")
                    exito, mensaje = inventario.eliminar_producto(nombre)
                    print(mensaje)

                elif sub == "4":
                    inventario.mostrar_productos()

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
                        "1": "Agregar al carrito",
                        "2": "Mostrar carrito",
                        "3": "Confirmar venta",
                        "4": "Cancelar y volver"
                    }
                )

                if sub == "1":
                    try:
                        nombre = input("Nombre del producto: ")
                        cantidad = int(input("Cantidad: "))
                    except ValueError:
                        print("Cantidad inválida.")
                        continue

                    producto = inventario.obtener_producto(nombre)

                    if not producto:
                        print("Producto no encontrado.")
                        continue

                    exito, mensaje = carrito.agregar(producto, cantidad)
                    print(mensaje)

                elif sub == "2":
                    carrito.mostrar()

                elif sub == "3":
                    exito, total, mensaje = carrito.confirmar()
                    print(mensaje)

                    if exito:
                        historial.registrar_venta(carrito.productos, total) 
                        historial.guardar()
                        inventario.guardar_inventario()
                        carrito.limpiar()

                    break

                elif sub == "4":
                    carrito.limpiar()
                    break

                else:
                    print("Opción inválida.")

        # ================= REPORTES =================
        elif opcion == "3":

            while True:

                sub = mostrar_menu(
                    "REPORTES",
                    {
                        "1": "Mostrar historial",
                        "2": "Ver detalle de venta",
                        "3": "Volver"
                    }
                )

                if sub == "1":
                    historial.mostrar_historial()

                elif sub == "2":
                    try:
                        indice = int(input("Número de la venta a ver: "))
                        historial.ver_venta(indice)
                    except ValueError:
                        print("Índice inválido.")

                elif sub == "3":
                    break
                else:
                    print("Opción inválida.")


        # ================= SALIR =================
        elif opcion == "4":
            inventario.guardar_inventario()   
            historial.guardar()        
            print("Sistema cerrado correctamente.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()