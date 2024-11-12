from animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self._ratones_comidos = 0

    @property
    def ratones_comidos(self):
        return self._ratones_comidos

    def agregar_raton(self):
        if self._ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self._ratones_comidos += 1

    def hacer_sonido(self):
        return "¡Tsss!"
