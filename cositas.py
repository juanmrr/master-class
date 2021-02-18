import random


class Cositas:

    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final

    def get_evens(self):
        return (i for i in range(self.inicial, self.final) if i % 2 == 0)

    def get_not_evens(self):
        return [i for i in range(self.inicial, self.final) if i % 2 == 1]

    def mean(self):
        return (self.inicial + self.final) / 2

    def die(self):
        return (random.randint(self.inicial, self.final))


if __name__ == "__main__":
    cositas = Cositas(2, 16)