from abc import ABC, abstractmethod

class HealthHospital(ABC):

    @abstractmethod
    def indiceMasaCorporal(self, peso: float, altura: float) -> float:
        pass

    @abstractmethod
    def pesoCorporalIdeal(self, sexo: str, altura: float) -> float:
        pass
