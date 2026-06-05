from enum import Enum

class Gender(Enum):
    MALE = "M"
    FEMALE = "F"

    def __str__(self) -> str:
        return self.value