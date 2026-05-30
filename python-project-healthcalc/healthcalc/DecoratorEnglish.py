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
