from enum import Enum

class Language(Enum):

    ENGLISH = "EN"
    SPANISH = "ES"

    def __str__(self) -> str:
        return self.value