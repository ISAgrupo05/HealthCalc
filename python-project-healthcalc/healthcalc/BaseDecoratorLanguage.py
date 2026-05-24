from abc import ABC, abstractmethod
from .health_hospital import HealthHospital


class BaseDecoratorLanguage(HealthHospital, ABC):
    """
    Clase base abstracta para decoradores que manejan diferentes idiomas.
    Implementa el patrón Decorator para traducir mensajes según el idioma.
    """

    def __init__(self, healthcalc: HealthHospital):
        self.healthcalc = healthcalc

    @abstractmethod
    def indiceMasaCorporal(self, peso: float, altura: float) -> tuple:
        """
        Calcula el índice de masa corporal con clasificación en el idioma especificado.
        """
        pass

    @abstractmethod
    def pesoCorporalIdeal(self, sexo: str, altura: float) -> float:
        """
        Calcula el peso corporal ideal.
        """
        pass

    @abstractmethod
    def _traducir_clasificacion_bmi(self, clasificacion: str) -> str:
        """
        Traduce la clasificación de BMI al idioma especificado.
        """
        pass

    @abstractmethod
    def _traducir_clasificacion_whr(self, clasificacion: str) -> str:
        """
        Traduce la clasificación de WHR al idioma especificado.
        """
        pass
