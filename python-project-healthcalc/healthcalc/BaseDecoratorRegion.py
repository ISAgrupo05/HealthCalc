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

    def indiceMasaCorporal(self, health_data: HealthData) -> tuple:
        """
        Calcula el índice de masa corporal usando datos normalizados a unidad métrica.
        """
        metric_data = health_data.normalize()
        return self.healthcalc.indiceMasaCorporal(metric_data)

    def pesoCorporalIdeal(self, health_data: HealthData) -> float:
        """
        Calcula el peso corporal ideal y convierte el resultado a las unidades de la región.
        """
        metric_data = health_data.normalize()
        peso_ideal_kg = self.healthcalc.pesoCorporalIdeal(metric_data)
        return self._convertir_peso_salida(peso_ideal_kg)

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
