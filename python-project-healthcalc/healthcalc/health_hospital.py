from abc import ABC, abstractmethod
from .HealthData import HealthData

class HealthHospital(ABC):

    @abstractmethod
    def indiceMasaCorporal(self, health_data: HealthData) -> tuple:
        pass

    @abstractmethod
    def pesoCorporalIdeal(self, health_data: HealthData) -> float:
        pass
