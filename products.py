
class Product:

    def __init__(self, name, price, promotion=None):
        """initializes Product with entered name and price. active will be true by default"""
        if not name or price < 0:
            raise ValueError("Invalid input: Name cannot be empty and price must not be negative!")
        self.name = name
        self.price = price
        self.active = True
        self.promotion = promotion
        self.quantity = 0


    def is_active(self):
        """returns whether the product is currently active"""
        return self.active


    def get_promotion(self):
        """returns the promotion"""
        return self.promotion


    def get_quantity(self):
        """returns quantity"""
        return self.quantity


    def get_price(self):
        """returns the price"""
        return self.price


    def set_promotion(self, promotion):
        """sets the promotion"""
        self.promotion = promotion


    def show(self):
        """returns a string with name, price and possibly the promotion of the product"""
        self_representation = f"{self.name}, Price: ${self.price}"
        if self.promotion is not None:
            return self_representation + f", Promotion: {self.promotion.name}"
        else:
            return self_representation


    def buy(self, quantity):
        """prints what is being bought and returns price. price will be calculated differently
        depending on whether or not there is a promo"""
        print(f"Buying {quantity}x {self.name}...")
        if self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)
        return quantity * self.price


class NonStockedProduct(Product):

    def __init__(self, name, price, promotion=None):
        super().__init__(name, price, promotion)


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum, promotion=None):
        """initializes limited product using the parent constructor and initializes quantity """
        super().__init__(name, price, promotion)
        if quantity < 0:
            raise ValueError("Invalid input: Quantity cannot be negative!")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()
        if maximum <= 0:
            raise ValueError("Invalid input: Maximum must be greater than zero!")
        self.maximum = maximum


    def get_maximum(self):
        """returns maximum"""
        return self.maximum


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
        return f"{super().show()}, Quantity: {self.quantity}, Maximum: {self.maximum}"


    def buy(self, quantity):
        """buys specified amount of product if enough products ara available. adjusts available quantity and returns price of bought items"""
        if quantity > self.quantity:
            raise ValueError(f"Not that many {self.name}s available")
        self.set_quantity(self.quantity - quantity)
        return super().buy(quantity)
