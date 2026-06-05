from abc import ABC, abstractmethod
from .BMICategory import BMICategory
from .WHRCategory import WHRCategory
from .HealthData import HealthData


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
    def bmi(self, health_data: HealthData) -> float:
        """Calculate the Body Mass Index (BMI).
        
        :param health_data: HealthData object containing weight and height
        :return: BMI value (kg/m2)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def lorentz(self, health_data: HealthData) -> float:
        """Calculate the Ideal Body Weight (IBW).
        
        :param health_data: HealthData object containing gender and height
        :return: Lorentz value (kg)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def whr(self, health_data: HealthData) -> float:
        """Calculate the Waist-to-Hip Ratio (WHR).
        
        :param health_data: HealthData object containing waist and hip measurements
        :return: WHR value
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def whr_classification(self, health_data: HealthData, whr: float) -> WHRCategory:
        """Calculate the WHR classification of a person.
        
        :param health_data: HealthData object containing gender
        :param whr: WHR value
        :return: WHRCategory classification
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
