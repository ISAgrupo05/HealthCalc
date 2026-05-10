from abc import ABC, abstractmethod

class HealthHospital(ABC):

    @abstractmethod
    def calcularIMC(self, peso: float, altura: float) -> float:
        pass

    @abstractmethod
    def clasificarIMC(self, imc: float) -> str:
        pass

    @abstractmethod
    def pesoIdeal(self, sexo: str, altura: float) -> float:
        pass

    @abstractmethod
    def relacionCinturaCadera(self, cintura: float, cadera: float) -> float:
        pass

    @abstractmethod
    def clasificarRCC(self, sexo: str, rcc: float) -> str:
        pass