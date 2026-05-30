from .BaseDecoratorLanguage import BaseDecoratorLanguage
from .HealthData import HealthData
from .health_hospital import HealthHospital
from .BMICategory import BMICategory
from .WHRCategory import WHRCategory


class DecoratorEnglish(BaseDecoratorLanguage):
    """
    Decorador para idioma Inglés.
    Mantiene todas las clasificaciones en inglés (comportamiento por defecto).
    """

    def __init__(self, healthcalc: HealthHospital):
        super().__init__(healthcalc)
        self.idioma = "English"

    def indiceMasaCorporal(self, health_data: HealthData) -> tuple:
        """
        Calcula BMI con clasificación en inglés.
        """
        result = self.healthcalc.indiceMasaCorporal(health_data)
        bmi = result[0]
        clasificacion_original = result[1]
        clasificacion_en = self._traducir_clasificacion_bmi(clasificacion_original)
        return bmi, clasificacion_en

    def pesoCorporalIdeal(self, health_data: HealthData) -> float:
        """
        Calcula el peso corporal ideal.
        """
        return self.healthcalc.pesoCorporalIdeal(health_data)

    def _traducir_clasificacion_bmi(self, clasificacion: BMICategory) -> str:
        """
        Mantiene clasificación de BMI en inglés (sin cambios).
        """
        return clasificacion

    def _traducir_clasificacion_whr(self, clasificacion: WHRCategory) -> str:
        """
        Mantiene clasificación de WHR en inglés (sin cambios).
        """
        return clasificacion
