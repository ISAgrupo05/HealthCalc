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
