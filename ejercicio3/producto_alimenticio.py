from producto import *

class Producto_alimenticio(Producto):
    def __init__(self, precio, IVA):
        Producto.__init__(self, precio)
        self.IVA = 0.055