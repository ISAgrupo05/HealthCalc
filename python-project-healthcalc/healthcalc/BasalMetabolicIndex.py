from abc import ABC, abstractmethod
from healthcalc.BMICategory import BMICategory


class BasalMetabolicIndex(ABC):
    """Interface for the calculator of basal metabolic index."""

    @abstractmethod
    def basalMetabolicIndex(self, person) -> float:
        """Calculate the Basal Metabolic Index (BMI).

        :param person: Person object with health data
        :return: BMI value (float)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def category(self, person) -> BMICategory:
        """Calculate the BMI category classification of a person.

        :param person: Person object with health data
        :return: BMICategory enum
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
