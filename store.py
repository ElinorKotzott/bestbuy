class Store:

    def __init__(self, products_list):
        """initializes Store with a list of offered products"""
        self.products_list = products_list


    def add_product(self, product):
        """appends a product to the product list"""
        self.products_list.append(product)


    def remove_product(self, product):
        """removes product from the products list"""
        if product in self.products_list:
            self.products_list.remove(product)

    def get_products_list(self):
        """returns products_list"""
        return self.products_list


    def get_total_quantity(self):
        """calculates and returns total amount of limited products in the store"""
        total_amount = sum(item.quantity for item in self.products_list)
        return total_amount


    def get_all_products(self):
        """returns all active products i.e. products with more than 0 quantity"""
        active_products = []
        for product in self.products_list:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """calls buy on each item in the shopping list and returns total order price"""
        total_price = 0
        for item in shopping_list:
            try:
                total_price = total_price + item[0].buy(item[1])
            except ValueError as e:
                print(e)
        return total_price
