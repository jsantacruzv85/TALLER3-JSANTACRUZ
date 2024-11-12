import unittest
from models.boa_constrictor import Boa_Constrictor

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Boa1", 15, 5, "Brasil", 20.5)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 15 * 20.5)

    def test_agregar_raton(self):
        for _ in range(10):
            self.boa.agregar_raton()
        self.assertEqual(self.boa.ratones_comidos, 10)
        with self.assertRaises(ValueError):
            self.boa.agregar_raton()
