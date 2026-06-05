from .health_hospital import HealthHospital
from .HealthData import HealthData
from .health_calc_impl import HealthCalcImpl


class Adapter(HealthHospital):

    def __init__(self, calc: HealthCalcImpl):
        self.calc = calc

    def indiceMasaCorporal(self, health_data: HealthData) -> tuple:
        metric_data = health_data.normalize()
        imc = self.calc.bmi(metric_data)
        return imc, self.calc.bmi_classification(imc)

    def pesoCorporalIdeal(self, health_data: HealthData) -> float:
        metric_data = health_data.normalize()
        return self.calc.lorentz(metric_data)
    