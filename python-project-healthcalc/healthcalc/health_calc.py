from abc import ABC, abstractmethod
from healthcalc import InvalidHealthDataException
from .gender import Gender
from .BMICategory import BMICategory
from .WHRCategory import WHRCategory


class HealthCalc(ABC):
    """Interface for the calculator of health parameters."""

    @abstractmethod
    def bmi_classification(self, bmi: float) -> BMICategory:
        """Calculate the BMI classification of a person.

        :param bmi: Body Mass Index (kg/m2)
        :return: BMICategory classification
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def bmi(self, weight: float, height: float) -> float:
        """Calculate the Body Mass Index (BMI).
        
        :param weight: Weight (kg)
        :param height: Height (m)
        :return: BMI value (kg/m2)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def lorentz(self, gender: Gender, height: float) -> float:
        """Calculate the Ideal Body Weight (IBW).
        
        :param gender: Gender gender (M/F)
        :param height: Height (m)
        :return: Lorentz value (kg)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def whr(self, waist: float, hip: float) -> float:
        """Calculate the Waist-to-Hip Ratio (WHR).
        
        :param waist: Waist (m)
        :param hip: Hip (m)
        :return: WHR value
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def whr_classification(self, gender: Gender, whr: float) -> WHRCategory:
        """Calculate the WHR classification of a person.
        
        :param gender: Gender gender (M/F)
        :param whr: WHR value
        :return: WHRCategory classification
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
