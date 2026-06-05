from .health_calc import HealthCalc
from .exceptions import InvalidHealthDataException
from .gender import Gender
from .BMICategory import BMICategory
from .WHRCategory import WHRCategory
from .HealthData import HealthData

class HealthCalcImpl(HealthCalc):

    _instance = None

    @staticmethod
    def getInstance():

        if HealthCalcImpl._instance is None:
            HealthCalcImpl._instance = HealthCalcImpl()

        return HealthCalcImpl._instance

    def _to_float(self, value, field_name):
            try:
                return float(value)
            except (ValueError, TypeError):
                raise InvalidHealthDataException(f"{field_name} must be a valid number.")

    def _validate_positive(self, value, field_name):
        if value <= 0:
            raise InvalidHealthDataException(f"{field_name} must be positive.")

    def _validate_range(self, value, min_val, max_val, field_name):
        if not (min_val <= value <= max_val):
            raise InvalidHealthDataException(
                f"{field_name} must be within a possible biological range [{min_val}-{max_val}]."
            )
#=================================
# BMI
#=================================

    def bmi_classification(self, bmi: float) -> BMICategory:
        self._validate_positive(bmi, "BMI")
        self._validate_range(bmi, 0, 150, "BMI")

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

    def bmi(self, health_data: HealthData) -> float:
        weight = self._to_float(health_data.weight, "Weight")
        height = self._to_float(health_data.height, "Height")

        self._validate_positive(weight, "Weight")
        self._validate_positive(height, "Height")
        self._validate_range(weight, 1, 700, "Weight (kg)")
        self._validate_range(height, 0.30, 3.00, "Height (m)")

        return weight / (height ** 2)

#=================================
# LORENZ
#=================================

    def lorentz(self, health_data: HealthData) -> float:
        height = self._to_float(health_data.height, "Height")
        self._validate_positive(height, "Height")
        self._validate_range(height, 1.00, 3.00, "Height (m)")
        
        if health_data.gender == Gender.MALE:
            return (height*100 - 100) - ((height*100 - 150)/4)
        else:
            return (height*100 - 100) - ((height*100 - 150)/2)

#=================================
# WHR
# =================================
  
    def whr(self, health_data: HealthData) -> float:
        waist = self._to_float(health_data.waist, "Waist")
        hip = self._to_float(health_data.hip, "Hip")
        self._validate_positive(waist, "Waist")
        self._validate_positive(hip, "Hip")
        self._validate_range(waist, 0.45, 3.00, "Waist (m)")
        self._validate_range(hip, 0.45, 3.00, "Hip (m)")

        return waist / hip
    
    def whr_classification(self, health_data: HealthData, whr: float) -> WHRCategory:
        self._validate_positive(whr, "WHR")
        self._validate_range(whr, 0, 5, "WHR")

        if health_data.gender is None:
            raise InvalidHealthDataException("Gender must be either 'M' (Male) or 'F' (Female).")

        
        if health_data.gender == Gender.MALE:
            return WHRCategory.PEAR if whr <= 0.90 else WHRCategory.APPLE
        else:
            return WHRCategory.PEAR if whr <= 0.85 else WHRCategory.APPLE


