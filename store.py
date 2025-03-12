import products


class Store:

    def __init__(self, products_list):
        self.products_list = products_list

    def add_product(self, product):
        self.products_list.append(product)


    def remove_product(self, product):
        if product in self.products_list:
            self.products_list.remove(product)


    def get_total_quantity(self):
        return len(self.products_list)


    def get_all_products(self):
        active_products = []
        for product in self.products_list:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            total_price = total_price + products.Product.buy(item[0], item[1])
        return total_price

def main():

    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Total order cost: ${price}.")

if __name__ == "__main__":
    main()

