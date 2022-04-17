class Texto:
    def __init__(self, linea1, linea2):
        self.linea1 = linea1
        self.linea2 = linea2

    def get_linea1(self):
        return self.linea1

    def set_linea1(self, a):
        self.linea1 = a

    def get_linea2(self):
        return self.linea2

    def set_linea2(self, a):
        self.linea2 = a


texto = Texto("hola", "adios")

def mayusculas(texto):

    linea1mayus = texto.get_linea1()
    linea2mayus = texto.get_linea2()

    texto.set_linea1(linea1mayus.upper())
    texto.set_linea2(linea2mayus.upper())
    return texto

mayusculas(texto)

def establecer_archivo(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def escribir_archivo(archivo, texto):
    archivo.write(texto)

arch = establecer_archivo("hola.txt", "a")
escribir_archivo(arch, texto.get_linea1())
escribir_archivo(arch, texto.get_linea2())




