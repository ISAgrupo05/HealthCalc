from .BaseDecoratorLanguage import BaseDecoratorLanguage
from .health_hospital import HealthHospital


class DecoratorEspanol(BaseDecoratorLanguage):
    """
    Decorador para idioma Español.
    Traduce todas las clasificaciones y mensajes al español.
    """

    def __init__(self, healthcalc: HealthHospital):
        super().__init__(healthcalc)
        self.idioma = "Español"

    def indiceMasaCorporal(self, peso: float, altura: float) -> tuple:
        """
        Calcula BMI y devuelve la clasificación en español.
        """
        result = self.healthcalc.indiceMasaCorporal(peso, altura)
        
        bmi = result[0]
        clasificacion_original = result[1]
        clasificacion_es = self._traducir_clasificacion_bmi(clasificacion_original)
        
        return bmi, clasificacion_es

    def pesoCorporalIdeal(self, sexo: str, altura: float) -> float:
        """
        Calcula el peso corporal ideal.
        """
        return self.healthcalc.pesoCorporalIdeal(sexo, altura)

    def _traducir_clasificacion_bmi(self, clasificacion: str) -> str:
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

    def _traducir_clasificacion_whr(self, clasificacion: str) -> str:
        """
        Traduce clasificación de WHR al español.
        """
        traducciones = {
            "Pear": "Forma de pera",
            "Apple": "Forma de manzana"
        }
        return traducciones.get(clasificacion, clasificacion)
