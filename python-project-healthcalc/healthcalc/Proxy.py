from .HealthData import HealthData
from .health_hospital import HealthHospital


class HealthCalcProxy(HealthHospital):

    def __init__(self, healthH, stats):
        self.healthH = healthH
        self.stats = stats

    def indiceMasaCorporal(self, health_data: HealthData):
        result = self.healthH.indiceMasaCorporal(health_data)
        imc = result[0]
        metric_data = health_data.normalize()
        self.stats.addPaciente(
            metric_data, imc
        )
        return result

    def pesoCorporalIdeal(self, health_data: HealthData):
        result = self.healthH.pesoCorporalIdeal(health_data)
        metric_data = health_data.normalize()
        self.stats.addPaciente(
            metric_data, None
        )
        return result