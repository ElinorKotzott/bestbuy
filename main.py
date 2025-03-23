import products
import store


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


def start(my_store):
    """prints menu and calls function to validate user choice for the menu.
    exits if user wants to exit. otherwise, sends user choice in to be processed"""
    while True:
        print("1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit\n")
        user_choice = user_input_and_validate_range(1, 4, False)

        if user_choice == 1:
            show_products(my_store)
        elif user_choice == 2:
            print(f"Total product quantity: {my_store.get_total_quantity()}\n")
        elif user_choice == 3:
            show_products(my_store)
            process_order(my_store)
        elif user_choice == 4:
            print("Exiting...")
            return


def show_products(my_store):
    """prints products with quantity higher than zero, i. e. active products"""
    i = 0
    for product in my_store.get_all_products():
        i = i + 1
        print(f"{i}. {product.show()}")
    print()


def user_input_and_validate_range(lower_bound, upper_bound, allow_empty_input):
    """validates user input based on its parameters. returns none if user pressed enter while empty input was allowed. returns valid user input"""
    while True:
        user_choice = input().strip()
        if allow_empty_input:
            if not user_choice:
                return
        try:
            user_choice = int(user_choice)
            if lower_bound <= user_choice <= upper_bound:
                return user_choice
            else:
                print("Please enter a number within range!")
        except ValueError:
            print("Please enter a number!")


def process_order(my_store):
    """processes the order by asking for product type and amount,
    handling quantity, creating a shopping list and calling order"""

    shopping_list = []
    while True:
        print(f"\nWhich product would you like? (Enter 1 - {len(my_store.get_products_list())} or press Enter to quit)")
        user_input_for_product = user_input_and_validate_range(1, len(my_store.get_products_list()), True)
        # None means user pressed Enter without input
        if user_input_for_product is None:
            break

        selected_product = my_store.get_products_list()[user_input_for_product - 1]
        shopping_cart_quantity_for_product = 0
        for item in shopping_list:
            if item[0] == selected_product:
                shopping_cart_quantity_for_product += item[1]
        if shopping_cart_quantity_for_product == selected_product.quantity:
            print("There are no more products of this type available!")
            continue

        available_amount = selected_product.quantity - shopping_cart_quantity_for_product
        print(f"How many items do you want to purchase? (Enter 1 - {available_amount})")
        user_input_for_amount = user_input_and_validate_range(1, available_amount, False)
        shopping_list.append((selected_product, user_input_for_amount))
        print("Product added to list!")

    print(f"Total spendings: ${my_store.order(shopping_list)}\n")


if __name__ == "__main__":
    main()
