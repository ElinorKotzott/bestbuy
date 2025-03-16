class Product:

    def __init__(self, name, price, quantity):
        """instantiates Product"""
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: 'name' cannot be empty, and 'price' and 'quantity' cannot be negative!")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """returns quantity"""
        return self.quantity


    def set_quantity(self, quantity):
        """sets quantity and deactivates product if quantity is zero"""
        if quantity == 0:
            self.deactivate()
        self.quantity = quantity


    def activate(self):
        """activates product"""
        self.active = True


    def deactivate(self):
        """deactivates product"""
        self.active = False


    def is_active(self):
        """returns whether the product is active"""
        return self.active


    def show(self):
        """string representation of a product"""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """buys the product if enough quantity is available and updates quantity. returns total price"""
        print(f"Buying {quantity}x {self.name}...")
        if quantity > self.quantity:
            raise ValueError(f"Not that many {self.name}s available")
        self.set_quantity(self.quantity - quantity)
        return quantity * self.price
