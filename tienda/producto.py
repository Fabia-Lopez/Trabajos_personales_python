class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True

    def aumentar_stock(self, cantidad):
        if cantidad <= 0:
            return False
        self.stock += cantidad
        return True

    def mostrar_info(self):
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"