from .health_calc import HealthCalc
from .exceptions import InvalidHealthDataException
from .gender import Gender
from .BMICategory import BMICategory
from .WHRCategory import WHRCategory

class HealthCalcImpl(HealthCalc):

    _instance = None

    @staticmethod
    def getInstance():

        if HealthCalcImpl._instance is None:
            HealthCalcImpl._instance = HealthCalcImpl()

        return HealthCalcImpl._instance

    def bmi_classification(self, bmi: float) -> BMICategory:

        if bmi < 0:
            raise InvalidHealthDataException(
                "BMI cannot be negative."
            )

        if bmi > 150:
            raise InvalidHealthDataException(
                "BMI must be within a possible biological range [0-150]."
            )

        if bmi < 16:
            return BMICategory.SEVERE_THINNESS

        elif bmi < 17:
            return BMICategory.MODERATE_THINNESS

        elif bmi < 18.5:
            return BMICategory.MILD_THINNESS

        elif bmi < 25:
            return BMICategory.NORMAL

        elif bmi < 30:
            return BMICategory.OVERWEIGHT

        elif bmi < 35:
            return BMICategory.OBESE_CLASS_I

        elif bmi < 40:
            return BMICategory.OBESE_CLASS_II

        return BMICategory.OBESE_CLASS_III

    def bmi(self, weight: float, height: float) -> float:
        if weight <= 0:
            raise InvalidHealthDataException("Weight must be positive.")
        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")
        if weight < 1 or weight > 700:
            raise InvalidHealthDataException("Weight must be within a possible biological range [1-700] kg.")
        if height < 0.30 or height > 3.00:
            raise InvalidHealthDataException("Height must be within a possible biological range [0.30-3.00] m.")
            
        return weight / (height ** 2)


    def lorentz(self, gender: Gender, height: float) -> float:
        try:
            height_value = float(height)
        except (ValueError, TypeError):
            raise InvalidHealthDataException("Height must be a valid number.")
        
        if height_value <= 0:
            raise InvalidHealthDataException("Height must be positive.")
        if height_value < 1.00 or height_value > 3.00:
            raise InvalidHealthDataException("Height must be within a possible biological range [1.00-3.00] m.")
        
        if gender == Gender.MALE:
            return (height_value*100 - 100) - ((height_value*100 - 150)/4)
        else:
            return (height_value*100 - 100) - ((height_value*100 - 150)/2)

        
    def whr(self, waist:float, hip:float) -> float:
        try:
            waist_value = float(waist)
            hip_value = float(hip)
        except (TypeError, ValueError):
            raise InvalidHealthDataException("Waist and hip must be numeric values.")

        if waist_value <= 0:
            raise InvalidHealthDataException("Waist perimeter must be positive.")
        if hip_value <= 0:
            raise InvalidHealthDataException("Hip perimeter must be positive.")
        if waist_value < 0.45 or waist_value > 3.00:
            raise InvalidHealthDataException("Waist perimeter must be within a possible biological range [0.45-3.00] m.")
        if hip_value < 0.45 or hip_value > 3.00:
            raise InvalidHealthDataException("Hip perimeter must be within a possible biological range [0.45-3.00] m.")

        return waist_value / hip_value
    
    def whr_classification(self, gender: Gender, whr: float) -> WHRCategory:
        if whr < 0:
            raise InvalidHealthDataException("WHR cannot be negative.")
        if whr > 5:
            raise InvalidHealthDataException("WHR must be within a possible biological range [0-5].")
        if gender is None:
            raise InvalidHealthDataException("Gender must be either 'M' (Male) or 'F' (Female).")

        result = WHRCategory.APPLE
        if gender == Gender.MALE:
            if whr <= 0.90:
                result = WHRCategory.PEAR
        else:
            if whr <= 0.85:
                result = WHRCategory.PEAR
            
        return result


