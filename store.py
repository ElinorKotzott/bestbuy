class Store:

    def __init__(self, products_list):
        """instantiates store with a list of objects (products)"""
        self.products_list = products_list


    def add_product(self, product):
        """adds a product to the list of products"""
        self.products_list.append(product)


    def remove_product(self, product):
        """removes a product from the list of products"""
        if product in self.products_list:
            self.products_list.remove(product)


    def get_products_list(self):
        """returns list of products"""
        return self.products_list


    def get_total_quantity(self):
        """returns total amount of products available in the store"""
        total_amount = sum(item.quantity for item in self.products_list)
        return total_amount


    def get_all_products(self):
        """returns active products i. e. products with a quantity higher than zero"""
        active_products = []
        for product in self.products_list:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """calls buy on all items in our shopping list and then returns the total price of the order"""
        total_price = 0
        for item in shopping_list:
            total_price = total_price + item[0].buy(item[1])
        return total_price
