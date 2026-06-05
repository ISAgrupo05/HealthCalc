from enum import Enum


class BMICategory(Enum):

    SEVERE_THINNESS = "Severe Thinness"
    MODERATE_THINNESS = "Moderate Thinness"
    MILD_THINNESS = "Mild Thinness"
    NORMAL = "Normal"
    OVERWEIGHT = "Overweight"
    OBESE_CLASS_I = "Obese Class I"
    OBESE_CLASS_II = "Obese Class II"
    OBESE_CLASS_III = "Obese Class III"

    def __str__(self) -> str:
        return self.value
