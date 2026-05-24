from .gender import Gender

class Person:

    def __init__(
        self,
        weight: float,
        height: float,
        gender: Gender,
        age: int = 0
    ):

        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age