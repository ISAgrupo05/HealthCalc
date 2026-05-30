from enum import Enum

class UnitSystem(Enum):

    METRIC = "METRIC"
    USA = "USA"
    GRAMS = "GRAMS"
    LBS = "LBS"
    INCHES = "INCHES"

    def __str__(self):
        return self.value