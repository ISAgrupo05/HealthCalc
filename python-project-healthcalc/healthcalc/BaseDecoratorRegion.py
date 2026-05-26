from abc import ABC, abstractmethod
from .health_hospital import HealthHospital
from .HealthData import HealthData


class BaseDecoratorRegion(HealthHospital, ABC):
    """
    Clase base abstracta para decoradores que manejan diferentes regiones/unidades.
    Implementa el patrón Decorator para convertir unidades según la región.
    """

    def __init__(self, healthcalc: HealthHospital):
        self.healthcalc = healthcalc

    @abstractmethod
    def indiceMasaCorporal(self, health_data: HealthData) -> tuple:
        """
        Calcula el índice de masa corporal.
        Las unidades de entrada y salida dependen de la región.
        """
        pass

    @abstractmethod
    def pesoCorporalIdeal(self, health_data: HealthData) -> float:
        """
        Calcula el peso corporal ideal.
        Las unidades de entrada y salida dependen de la región.
        """
        pass

    @abstractmethod
    def _convertir_peso_entrada(self, peso: float) -> float:
        """
        Convierte el peso de entrada a kilogramos (formato interno).
        """
        pass

    @abstractmethod
    def _convertir_peso_salida(self, peso: float) -> float:
        """
        Convierte el peso de salida de kilogramos al formato de la región.
        """
        pass

    @abstractmethod
    def _convertir_altura_entrada(self, altura: float) -> float:
        """
        Convierte la altura de entrada a metros (formato interno).
        """
        pass

    @abstractmethod
    def _convertir_altura_salida(self, altura: float) -> float:
        """
        Convierte la altura de salida de metros al formato de la región.
        """
        pass
