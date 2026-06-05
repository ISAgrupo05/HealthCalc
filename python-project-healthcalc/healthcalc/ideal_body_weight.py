from abc import ABC, abstractmethod
from .person import Person

class IdealBodyWeight(ABC):

    @abstractmethod
    def idealBodyWeight(self, person: Person) -> float:
        """
        Calcula el Peso Corporal Ideal (IBW)

        :param person: Objeto Person
        :return: Peso ideal en kg
        """
        pass