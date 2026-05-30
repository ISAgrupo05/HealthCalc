from .BaseDecoratorRegion import BaseDecoratorRegion
from .HealthData import HealthData
from .health_hospital import HealthHospital


class DecoratorEU(BaseDecoratorRegion):
    """
    Decorador para la región EU.
    Utiliza el sistema métrico: kilogramos (kg), metros (m).
    No realiza conversión de unidades ya que el sistema interno también usa métrico.
    """

    def __init__(self, healthcalc: HealthHospital):
        super().__init__(healthcalc)
        self.region = "EU"


    def _convertir_peso_entrada(self, peso: float) -> float:
        """Convierte el peso de entrada de kg a gramos, porque el Adapter espera gramos."""
        return peso * 1000

    def _convertir_peso_salida(self, peso: float) -> float:
        """En EU, el peso se devuelve en kg, sin conversión adicional."""
        return peso

    def _convertir_altura_entrada(self, altura: float) -> float:
        """En EU, la altura ya está en m, sin conversión."""
        return altura

    def _convertir_altura_salida(self, altura: float) -> float:
        """En EU, la altura se devuelve en m, sin conversión."""
        return altura
