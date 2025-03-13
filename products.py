from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.active = True


    def is_active(self):
        return self.active


    def show(self):
        return f"{self.name}, Price: ${self.price}"


    def buy(self, quantity):
        print(f"Buying {quantity}x {self.name}...")
        return quantity * self.price


class NonStockedProduct(Product):

    def __init__(self, name, price):
        super().__init__(name, price)


class LimitedProduct(Product):

    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: 'name' cannot be empty, and 'price' and 'quantity' cannot be negative!")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity == 0:
            self.deactivate()
        self.quantity = quantity


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return f"{super().show()}, Quantity: {self.quantity}"


    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError(f"Not that many {self.name}s available")
        self.set_quantity(self.quantity - quantity)
        return super().buy(quantity)
