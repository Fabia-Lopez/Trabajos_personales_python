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
        self.stock += cantidad

    def __str__(self):
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"