# ESTRUCTURASDEDATOS

El link al repositorio es el siguiente: https://github.com/Germiprogramer/ESTRUCTURASDEDATOS.git

# EJERCICIO 1

    class Bloque: 
        # Un bloque es un conjunto de instrucciones ejecutadas 
        # unas detrás de otras. 
        def __init__(self): 
            # Por defecto, un bloque no contiene ninguna instrucción. 
            self.instrucciones = [] 

        def agregarInstruction(self, instruccion): 
            self.instrucciones.append(instruccion) 

    class Si: 
        # Representa una instrucción 'if'. 'condicion' es una cadena 
        # de caracteres que contiene la evaluación de la condición, 
        # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
        # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
        # si no se verifica. 

        def __init__(self, condicion, entonces, si_no): 
            self.condicion = condicion 
            self.entonces = entonces 
            self.si_no = si_no 

    class MientrasQue: 
        # Representa una instrucción 'while'. 
        # 'condicion' es una cadena que contiene el valor evaluado 
        # para decidir si el bucle continúa o no, 
        # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
        def __init__(self, condicion, bloque): 
            self.condicion = condicion 
            self.bloque = bloque 

    class Mostrar: 
        # Una instrucción para mostrar un mensaje 
        # en salida estándar. 
        def __init__(self, mensaje): 
            self.mensaje = mensaje 

    mostrar_ok = Mostrar('"OK"') 
    mostrar_ko = Mostrar('"KO"') 
    alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
    bloque_alternativa = Bloque()
    bloque_alternativa.agregarInstruccion(alternativa) 
    bucle = MientrasQue(True, bloque_alternativa) 



# EJERCICIO 2

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

# EJERCICIO 3

    class Producto:
        def __init__(self, precio):
            self.precio = 100

        def facturar(self):
            precio_neto = self.precio + self.precio * self.IVA
            print(precio_neto)

    class Producto_alimenticio(Producto):
        def __init__(self, precio, IVA):
            Producto.__init__(self, precio)
            self.IVA = 0.055

    class Producto_servicio(Producto):
        def __init__(self, precio, IVA):
            Producto.__init__(self, precio)
            self.IVA = 0.2

    producto = Producto_alimenticio("", "")
    producto.facturar()

    producto = Producto_servicio("", "")
    producto.facturar()
