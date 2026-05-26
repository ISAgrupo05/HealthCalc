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
            peso=metric_data.weight,
            altura=metric_data.height,
            imc=imc,
            sexo=metric_data.sex
        )
        return result

    def pesoCorporalIdeal(self, health_data: HealthData):
        result = self.healthH.pesoCorporalIdeal(health_data)
        metric_data = health_data.normalize()
        self.stats.addPaciente(
            altura=metric_data.height,
            sexo=metric_data.sex
        )
        return result