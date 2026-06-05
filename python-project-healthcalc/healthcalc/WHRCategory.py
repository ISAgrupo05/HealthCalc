from enum import Enum


class WHRCategory(Enum):
    PEAR = "Pear"
    APPLE = "Apple"

    def __str__(self) -> str:
        return self.value    