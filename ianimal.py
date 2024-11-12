from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def comer(self, cantidad):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass
