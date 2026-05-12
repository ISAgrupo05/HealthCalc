from .health_hospital import HealthHospital


class HealthCalcProxy(HealthHospital):

    def __init__(self, healthH, stats):

        self.healthH = healthH
        self.stats = stats

    def indiceMasaCorporal(self, peso, altura):

        result = self.healthH.indiceMasaCorporal(
            peso,
            altura
        )

        imc = result[0]

        self.stats.addPaciente(
            peso=peso,
            altura=altura,
            imc=imc
        )

        return result

    def pesoCorporalIdeal(self, sexo, altura):

        result = self.healthH.pesoCorporalIdeal(
            sexo,
            altura
        )

        self.stats.addPaciente(
            altura=altura,
            sexo=sexo
        )

        return result