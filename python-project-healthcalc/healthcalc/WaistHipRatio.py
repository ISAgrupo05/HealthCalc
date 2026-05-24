from abc import ABC, abstractmethod
from .person import Person


class WaistHipRatio(ABC):
    """
    Interfaz para una métrica adicional (WHRCategory / OtraMétrica).

    Esta interfaz define operaciones para calcular una métrica a partir de un
    objeto `person` o directamente a partir de valores numéricos (cintura/ cadera),
    además de obtener una categoría asociada al valor calculado.
    """

    @abstractmethod
    def m(self, person: Person) -> float:
        """Calcula la métrica a partir de un objeto `person`.

        Parámetro `person` es deliberadamente genérico para permitir distintas
        representaciones (objeto, dict, etc.) según la implementación.
        """
        pass

    @abstractmethod
    def WaistHipRatio(self, waist: float, hip: float) -> float:
        """Calcula el WHR (waist-to-hip ratio) a partir de medidas numéricas."""
        pass

    @abstractmethod
    def category(self, sex: str, value: float) -> str:
        """Devuelve la categoría (p.ej. 'Pear' o 'Apple') según sexo y valor."""
        pass
