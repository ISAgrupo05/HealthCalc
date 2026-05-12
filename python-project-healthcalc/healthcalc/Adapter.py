from .health_hospital import HealthHospital
from .health_calc_impl import HealthCalcImpl

class Adapter(HealthHospital):


    def __init__(self, calc):
        self.calc = calc

    def indiceMasaCorporal(self, peso: float, altura: float) -> float:
        peso_kg = peso / 1000
        imc = self.calc.bmi(peso_kg, altura)
        return imc, self.calc.bmi_classification(imc)   
    
    def pesoCorporalIdeal(self, sexo: str, altura: float) -> float:
        return self.calc.lorentz(sexo, altura)
    