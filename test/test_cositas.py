from unittest import TestCase
from unittest import mock
from masterclass.cositas import Cositas


class Test_Cositas(TestCase):

    inicio = 2
    final = 16
    cositas = Cositas(inicio, final)

    def test_cositas_get_evens(self):
        expected_return = [2, 4, 6, 8, 10, 12, 14]
        
        lista = list(self.cositas.get_evens())
        assert lista == expected_return

    def test_cositas_get_not_evens(self):
        expected_return = [3, 5, 7, 9, 11, 13, 15]

        lista = self.cositas.get_not_evens()
        assert lista == expected_return

    def test_cositas_mean(self):
        expected_return = 9

        mean = self.cositas.mean()
        assert mean == expected_return

    def test_cositas_die(self):
        die = self.cositas.die()
        assert die in range(self.inicio, self.final)

