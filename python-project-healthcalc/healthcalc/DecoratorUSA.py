from .BaseDecoratorRegion import BaseDecoratorRegion
from .health_hospital import HealthHospital


class DecoratorUSA(BaseDecoratorRegion):
    """
    Decorador para la región USA.
    Utiliza el sistema imperial: libras (lbs), pulgadas (inches).
    Convierte entre libras/pulgadas y kilogramos/metros.
    """

    def __init__(self, healthcalc: HealthHospital):
        super().__init__(healthcalc)
        self.region = "USA"

    def indiceMasaCorporal(self, peso: float, altura: float) -> tuple:
        """
        Calcula BMI. En USA, peso está en libras (lbs) y altura en pulgadas (inches).
        Convierte a kg y m para el cálculo interno.
        """
        peso_kg = self._convertir_peso_entrada(peso)
        altura_m = self._convertir_altura_entrada(altura)
        
        result = self.healthcalc.indiceMasaCorporal(peso_kg, altura_m)
        
        bmi = result[0]
        clasificacion = result[1]
        
        return bmi, clasificacion

    def pesoCorporalIdeal(self, sexo: str, altura: float) -> float:
        """
        Calcula peso corporal ideal. En USA, altura en pulgadas, resultado en libras.
        """
        altura_m = self._convertir_altura_entrada(altura)
        
        peso_ideal_kg = self.healthcalc.pesoCorporalIdeal(sexo, altura_m)
        peso_ideal_lbs = self._convertir_peso_salida(peso_ideal_kg)
        
        return peso_ideal_lbs

    def _convertir_peso_entrada(self, peso: float) -> float:
        """
        Convierte libras (lbs) a gramos (para el Adapter).
        1 lb = 0.453592 kg = 453.592 g
        """
        return peso * 453.592

    def _convertir_peso_salida(self, peso: float) -> float:
        """
        Convierte kilogramos (kg) a libras (lbs).
        1 kg = 2.20462 lbs
        """
        return peso * 2.20462

    def _convertir_altura_entrada(self, altura: float) -> float:
        """
        Convierte pulgadas (inches) a metros (m).
        1 pulgada = 0.0254 m
        """
        return altura * 0.0254

    def _convertir_altura_salida(self, altura: float) -> float:
        """
        Convierte metros (m) a pulgadas (inches).
        1 m = 39.3701 pulgadas
        """
        return altura * 39.3701
