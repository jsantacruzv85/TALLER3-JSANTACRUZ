from animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    @property
    def pais_origen(self):
        return self._pais_origen

    @property
    def impuestos(self):
        return self._impuestos

    def calcular_flete(self):
        return self._impuestos * self._peso
