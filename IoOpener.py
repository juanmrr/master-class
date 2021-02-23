class IoOpener:

    def __init__(self, fichero):
        self.fichero = fichero

    def read(self):
        cadena = ''
        with open(self.fichero, 'r') as reader:
            for line in reader:
                cadena += line
        return cadena

    def write(self, cadena_a_escribir):
        with open(self.fichero, 'a') as writer:
            for cadena in cadena_a_escribir:
                writer.write(cadena)


if __name__ == "__main__":
    fichero_lectura = IoOpener('prueba.txt')
    print(fichero_lectura.read())

    fichero_escritura = IoOpener('prueba.txt')
    fichero_escritura.write('hola\n')