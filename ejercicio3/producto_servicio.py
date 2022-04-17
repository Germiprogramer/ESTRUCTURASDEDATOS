from producto import *

class Producto_servicio(Producto):
    def __init__(self, precio, IVA):
        Producto.__init__(self, precio)
        self.IVA = 0.2