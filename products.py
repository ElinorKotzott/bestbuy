class Product:

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input: 'name' cannot be empty, and 'price' and 'quantity' cannot be negative!")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        if quantity == 0:
            Product.deactivate(self)
        self.quantity = quantity


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def is_active(self):
        return self.active


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        print(f"Buying {quantity}x {self.name}...")
        if quantity > self.quantity:
            raise ValueError(f"Not that many {self.name}s available")
        Product.set_quantity(self, self.quantity - quantity)
        return quantity * self.price

def main():
    bose = Product("Bose QuietComfort Earbuds", 250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(120))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()