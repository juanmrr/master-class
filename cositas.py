import random

class Cositas:

    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final
        self.numeros=[]
        for i in range(inicial, final):
            self.numeros.append(i)

    def get_evens(self):
        pares=[]
        for i in self.numeros:
            if i%2 == 0:
                pares.append(i)
        return pares

    def get_not_evens(self):
        impares=[]
        for i in self.numeros:
            if i%2==1:
                impares.append(i)

        return impares

    def mean(self):
        return (self.inicial+self.final)/2

    def die(self):
        return (random.randint(self.inicial, self.final))