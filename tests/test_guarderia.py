import unittest
from models.guarderia import Guarderia
from models.boa_constrictor import Boa_Constrictor

class TestGuarderia(unittest.TestCase):
    def setUp(self):
        self.guarderia = Guarderia()

    def test_alimentar_boa_exito(self):
        boa = self.guarderia.boas[0]
        resultado = self.guarderia.alimentar_boa(boa)
        self.assertEqual(resultado, "Éxito")

    def test_alimentar_boa_llena(self):
        boa = self.guarderia.boas[0]
        for _ in range(10):
            boa.agregar_raton()
        resultado = self.guarderia.alimentar_boa(boa)
        self.assertEqual(resultado, "La boa está llena")

    def test_alimentar_boa_inexistente(self):
        resultado = self.guarderia.alimentar_boa(None)
        self.assertEqual(resultado, "Esta Boa no existe!")
