from abc import ABC, abstractmethod
from promotion import Promotion


class Product(ABC):

    def __init__(self, name, price, promotion=None):
        """initializes Product with entered name and price. active will be true by default"""
        if not name or price < 0:
            raise ValueError("Invalid input: Name cannot be empty and price must not be negative!")
        self.name = name
        self.price = price
        self.active = True
        self.promotion = promotion


    def is_active(self):
        """returns whether the product is currently active"""
        return self.active

    def get_promotion(self):
        """returns the promotion, returns None if there is none"""
        return self.promotion


    def show(self):
        """returns a string with name, price and possibly the promotion of the product"""
        self_representation = f"{self.name}, Price: ${self.price}"
        if self.promotion is not None:
            return self_representation + f", Promotion: {self.promotion}"
        else:
            return self_representation


    def buy(self, quantity):
        """prints what is being bought and returns price. price will be calculated differently
        depending on whether or not there is a promo"""
        print(f"Buying {quantity}x {self.name}...")
        if self.promotion is not None:
            return Promotion.apply_promotion(self.promotion, self, quantity) #TODO is this good?? how is this supposed to even work?? check again later
        return quantity * self.price


class NonStockedProduct(Product):

    def __init__(self, name, price):
        """initializes non stocked product by calling the parent constructor"""
        super().__init__(name, price)


class LimitedProduct(Product):

    def __init__(self, name, price, quantity):
        """initializes limited product using the parent constructor and initializes quantity """
        super().__init__(name, price)
        if quantity < 0:
            raise ValueError("Invalid input: Quantity' cannot be negative!")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()


    def get_quantity(self):
        """returns quantity"""
        return self.quantity


    def set_quantity(self, quantity):
        """sets quantity. if quantity is zero, calls deactivate"""
        if quantity == 0:
            self.deactivate()
        self.quantity = quantity


    def activate(self):
        """activates the product"""
        self.active = True


    def deactivate(self):
        """deactivates the product"""
        self.active = False


    def show(self):
        """string representation of the limited product using the show method of the parent"""
        return f"{super().show()}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """buys specified amount of product if enough products ara available. adjusts available quantity and returns price of bought items"""
        if quantity > self.quantity:
            raise ValueError(f"Not that many {self.name}s available")
        self.set_quantity(self.quantity - quantity)
        return super().buy(quantity)
