import sys

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
    while True:
        print("1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit\n")
        try:
            user_choice = int(input().strip())
            if user_choice == 1:
                i = 0
                for product in my_store.get_all_products():
                    i = i + 1
                    print(f"{i}. {product.show()}")
                print()
            elif user_choice == 2:
                print(f"Total product quantity: {my_store.get_total_quantity()}\n")
            elif user_choice == 3:
                j = 0
                for product in my_store.get_all_products():
                    j = j + 1
                    print(f"{j}. {product.show()}")
                purchase_list = []

                while True:
                    print(f"\nWhich product would you like? (Enter 1 - {len(my_store.products_list)})")
                    user_input_for_product = user_input_and_validate_range(1, len(my_store.products_list), True)
                    if user_input_for_product is None:
                        break

                    selected_product = my_store.products_list[user_input_for_product - 1]
                    print(f"How many items do you want to purchase? (Enter 1 - {selected_product.quantity})")
                    user_input_for_amount = user_input_and_validate_range(1, selected_product.quantity, False)
                    purchase_list.append((selected_product.name, user_input_for_amount))

                my_store.order(purchase_list)
            elif user_choice == 4:
                sys.exit()
            else:
                raise ValueError

        except ValueError:
            print("Please enter kjkj!\n")


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
        except (ValueError, IndexError) as e:
            print("Please enter a valid number!", e)





if __name__ == "__main__":
    main()
