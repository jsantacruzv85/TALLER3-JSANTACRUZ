from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [Boa_Constrictor("Boa1", 15, 5, "Brasil", 20.5), Boa_Constrictor("Boa2", 14, 4, "Perú", 18.0)]
        self.hurones = [Huron("Huron1", 2, 3, "Argentina", 10.0), Huron("Huron2", 1.5, 2, "Chile", 12.0)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.agregar_raton()
            return "Éxito"
        except ValueError:
            return "La boa está llena"
