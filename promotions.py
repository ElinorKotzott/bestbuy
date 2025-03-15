from abc import ABC, abstractmethod


class Promotion(ABC):

    def __init__(self, name):
        if not name:
            raise ValueError("Name must not be empty!")
        self.name = name


    def get_name(self):
        """returns the name of the promotion"""
        return self.name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        """is an abstract method implemented in each of the children"""
        pass


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        if quantity >= 2:
            return product.get_price() * (quantity - 0.5)
        else:
            return product.get_price * quantity



class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        if quantity >= 3:
            return product.get_price() * (quantity - 1)
        else:
            return product.get_price() * quantity


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        if 0 < percent <= 100:
            self.percent = percent
        else: raise ValueError("Please enter a number between 0 (exclusive) and 100 (inclusive)!")


    def apply_promotion(self, product, quantity):
        return product.get_price() * quantity * (1 - self.percent)
