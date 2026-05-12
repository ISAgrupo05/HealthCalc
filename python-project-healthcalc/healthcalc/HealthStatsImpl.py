from healthcalc.HealthStats import HealthStats


class HealthStatsImpl(HealthStats):

    def __init__(self):

        self.alturas = []
        self.pesos = []
        self.imcs = []

        self.hombres = 0
        self.mujeres = 0

    def addPaciente(self, peso=None, altura=None, imc=None, sexo=None):

        if peso is not None:
            self.pesos.append(peso)

        if altura is not None:
            self.alturas.append(altura)

        if imc is not None:
            self.imcs.append(imc)

        if sexo == "M":
            self.hombres += 1

        elif sexo == "F":
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