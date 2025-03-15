from abc import ABC, abstractmethod


class Promotion(ABC):

    def __init__(self, name):
        if not name:
            raise ValueError("Name must not be empty!")
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        pass


class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        pass
