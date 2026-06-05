from abc import ABC, abstractmethod
from .health_hospital import HealthHospital
from .HealthData import HealthData
from .BMICategory import BMICategory
from .WHRCategory import WHRCategory


class BaseDecoratorLanguage(HealthHospital, ABC):
    """
    Clase base abstracta para decoradores que manejan diferentes idiomas.
    Implementa el patrón Decorator para traducir mensajes según el idioma.
    """

    def __init__(self, healthcalc: HealthHospital):
        self.healthcalc = healthcalc

    def indiceMasaCorporal(self, health_data: HealthData) -> tuple:
        """
        Calcula el índice de masa corporal y traduce la clasificación al idioma del decorador.
        """
        result = self.healthcalc.indiceMasaCorporal(health_data)
        bmi = result[0]
        clasificacion_original = result[1]
        clasificacion_traducida = self._traducir_clasificacion_bmi(clasificacion_original)
        return bmi, clasificacion_traducida

    def pesoCorporalIdeal(self, health_data: HealthData) -> float:
        """
        Calcula el peso corporal ideal utilizando la implementación subyacente.
        """
        return self.healthcalc.pesoCorporalIdeal(health_data)

    def whr(self, health_data: HealthData) -> float:
        """
        Calcula el índice cintura-cadera utilizando la implementación subyacente.
        """
        return self.healthcalc.whr(health_data)

    def whr_classification(self, health_data: HealthData, whr: float) -> str:
        """
        Calcula la clasificación WHR y traduce al idioma del decorador.
        """
        result = self.healthcalc.whr_classification(health_data, whr)
        clasificacion_traducida = self._traducir_clasificacion_whr(result)
        return clasificacion_traducida

    @abstractmethod
    def _traducir_clasificacion_bmi(self, clasificacion: BMICategory) -> str:
        """
        Traduce la clasificación de BMI al idioma especificado.
        """
        pass

    @abstractmethod
    def _traducir_clasificacion_whr(self, clasificacion: WHRCategory) -> str:
        """
        Traduce la clasificación de WHR al idioma especificado.
        """
        pass
