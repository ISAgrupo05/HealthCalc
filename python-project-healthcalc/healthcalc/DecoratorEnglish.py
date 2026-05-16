from .BaseDecoratorLanguage import BaseDecoratorLanguage
from .health_hospital import HealthHospital


class DecoratorEnglish(BaseDecoratorLanguage):
    """
    Decorador para idioma Inglés.
    Mantiene todas las clasificaciones en inglés (comportamiento por defecto).
    """

    def __init__(self, healthcalc: HealthHospital):
        super().__init__(healthcalc)
        self.idioma = "English"

    def indiceMasaCorporal(self, peso: float, altura: float) -> tuple:
        """
        Calcula BMI con clasificación en inglés.
        """
        result = self.healthcalc.indiceMasaCorporal(peso, altura)
        
        bmi = result[0]
        clasificacion_original = result[1]
        clasificacion_en = self._traducir_clasificacion_bmi(clasificacion_original)
        
        return bmi, clasificacion_en

    def pesoCorporalIdeal(self, sexo: str, altura: float) -> float:
        """
        Calcula el peso corporal ideal.
        """
        return self.healthcalc.pesoCorporalIdeal(sexo, altura)

    def _traducir_clasificacion_bmi(self, clasificacion: str) -> str:
        """
        Mantiene clasificación de BMI en inglés (sin cambios).
        """
        return clasificacion

    def _traducir_clasificacion_whr(self, clasificacion: str) -> str:
        """
        Mantiene clasificación de WHR en inglés (sin cambios).
        """
        return clasificacion
