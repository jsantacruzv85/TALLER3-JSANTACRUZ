import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Huron1", 2, 3, "Argentina", 10.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 2 * 10.0)
