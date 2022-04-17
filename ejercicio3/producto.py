class Producto:
    def __init__(self, precio):
        self.precio = 100

    def facturar(self):
        precio_neto = self.precio + self.precio * self.IVA
        print(precio_neto)