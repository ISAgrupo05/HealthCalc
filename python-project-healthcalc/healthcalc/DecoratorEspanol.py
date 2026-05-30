from .BaseDecoratorLanguage import BaseDecoratorLanguage
from .HealthData import HealthData
from .health_hospital import HealthHospital
from .BMICategory import BMICategory
from .WHRCategory import WHRCategory


class DecoratorEspanol(BaseDecoratorLanguage):
    """
    Decorador para idioma Español.
    Traduce todas las clasificaciones y mensajes al español.
    """

    def __init__(self, healthcalc: HealthHospital):
        super().__init__(healthcalc)
        self.idioma = "Español"

    def indiceMasaCorporal(self, health_data: HealthData) -> tuple:
        """
        Calcula BMI y devuelve la clasificación en español.
        """
        result = self.healthcalc.indiceMasaCorporal(health_data)
        bmi = result[0]
        clasificacion_original = result[1]
        clasificacion_es = self._traducir_clasificacion_bmi(clasificacion_original)
        return bmi, clasificacion_es

    def pesoCorporalIdeal(self, health_data: HealthData) -> float:
        """
        Calcula el peso corporal ideal.
        """
        return self.healthcalc.pesoCorporalIdeal(health_data)

    def _traducir_clasificacion_bmi(self, clasificacion: BMICategory) -> str:
        """
        Traduce clasificación de BMI al español.
        """
        traducciones = {
            "Underweight": "Peso insuficiente",
            "Normal weight": "Peso normal",
            "Overweight": "Sobrepeso",
            "Obesity": "Obesidad"
        }
        return traducciones.get(clasificacion, clasificacion)

    def _traducir_clasificacion_whr(self, clasificacion: WHRCategory) -> str:
        """
        Traduce clasificación de WHR al español.
        """
        traducciones = {
            "Pear": "Forma de pera",
            "Apple": "Forma de manzana"
        }
        return traducciones.get(clasificacion, clasificacion)
