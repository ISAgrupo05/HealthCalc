from .health_hospital import HealthHospital
from .health_calc_impl import HealthCalcImpl

class HealthCalcAdapter(HealthHospital):

    def __init__(self):
        self.calc = HealthCalcImpl.getInstance()

    def calcularIMC(self, peso: float, altura: float) -> float:
        peso_kg = peso / 1000
        return self.calc.bmi(peso_kg, altura)
    
    def clasificarIMC(self, imc: float) -> str:
        return self.calc.bmi_classification(imc)
    
    def pesoIdeal(self, sexo: str, altura: float) -> float:
        return self.calc.lorentz(sexo, altura)
    
    def relacionCinturaCadera(self, cintura: float, cadera: float) -> float:
        return self.calc.whr(cintura, cadera)
    
    def clasificarRCC(self, sexo: str, rcc: float) -> str:
        return self.calc.whr_classification(sexo, rcc)
    
