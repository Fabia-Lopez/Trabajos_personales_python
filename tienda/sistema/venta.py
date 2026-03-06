from datetime import datetime


class Venta:

    def __init__(self, productos, total):

        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.productos = productos
        self.total = total