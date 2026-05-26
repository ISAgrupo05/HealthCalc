from healthcalc.HealthStats import HealthStats
from healthcalc.gender import Gender

class HealthStatsImpl(HealthStats):

    def __init__(self):

        self.alturas = []
        self.pesos = []
        self.imcs = []

        self.hombres = 0
        self.mujeres = 0

    def _add_if_not_none(self, lst, value):
        if value is not None:
            lst.append(value)

    def addPaciente(self, person, imc=None):

        self._add_if_not_none(
            self.pesos,
            person.weight
        )

        self._add_if_not_none(
            self.alturas,
            person.height
        )

        self._add_if_not_none(
            self.imcs,
            imc
        )

        if person.gender == Gender.MALE:
            self.hombres += 1

        elif person.gender == Gender.FEMALE:
            self.mujeres += 1

    def alturaMedia(self) -> float:

        if len(self.alturas) == 0:
            return 0

        return sum(self.alturas) / len(self.alturas)

    def pesoMedio(self) -> float:

        if len(self.pesos) == 0:
            return 0

        return sum(self.pesos) / len(self.pesos)

    def imcMedio(self) -> float:

        if len(self.imcs) == 0:
            return 0

        return sum(self.imcs) / len(self.imcs)

    def numSexoH(self) -> int:
        return self.hombres

    def numSexoM(self) -> int:
        return self.mujeres

    def numTotalPacientes(self) -> int:
        return (len(self.imcs) + self.hombres + self.mujeres)