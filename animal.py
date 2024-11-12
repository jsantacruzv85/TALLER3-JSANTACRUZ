from abc import ABC, abstractmethod
from ianimal import IAnimal

class Animal(IAnimal, ABC):
    def __init__(self, nombre, peso, edad):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0

    @property
    def nombre(self):
        return self._nombre

    @property
    def peso(self):
        return self._peso

    @property
    def edad(self):
        return self._edad

    def comer(self, cantidad):
        self._kilos_comidos += cantidad

    def obtener_kilos_comidos(self):
        return self._kilos_comidos

    @abstractmethod
    def hacer_sonido(self):
        pass
