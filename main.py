import sys
import products
import store
import promotions
from products import NonStockedProduct


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)


    best_buy = store.Store(product_list)
    start(best_buy)


def start(my_store):
    """prints menu and determines actions based on user choice. handles choice number 3, order, in the inner while"""
    while True:
        print("1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit\n")
        user_choice = user_input_and_validate_range(1, 4, False)
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

            shopping_list = []
            while True:
                print(f"\nWhich product would you like? (Enter 1 - {len(my_store.get_all_products())} or press Enter to quit)")
                user_input_for_product = user_input_and_validate_range(1, len(my_store.get_all_products()), True)
                #None means user pressed Enter without input
                if user_input_for_product is None:
                    break

                #selected_product = my_store.get_products_list()[user_input_for_product - 1]
                selected_product = my_store.get_all_products()[user_input_for_product - 1]
                shopping_cart_quantity_for_product = 0
                for item in shopping_list:
                    if item[0] == selected_product:
                        shopping_cart_quantity_for_product += item[1]
                #only the limited products will be checked for availability
                if not isinstance(selected_product, NonStockedProduct) and shopping_cart_quantity_for_product == selected_product.quantity:
                    print("There are no more products of this type available!")
                    continue
                #extra logic for non-stocked products that can be bought infinitely
                if isinstance(selected_product, NonStockedProduct):
                    print("How many items do you want to purchase?")
                    user_input_for_amount = user_input_and_validate_range(1, float("inf"), False)
                else:
                    available_amount = selected_product.quantity - shopping_cart_quantity_for_product
                    print(f"How many items do you want to purchase? (Enter 1 - {available_amount})")
                    user_input_for_amount = user_input_and_validate_range(1, available_amount, False)
                shopping_list.append((selected_product, user_input_for_amount))
                print("Product added to list!")

            print(f"Total spendings: ${my_store.order(shopping_list)}")

        elif user_choice == 4:
            sys.exit()


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
        except (ValueError, IndexError):
            print("Please enter a number!")


if __name__ == "__main__":
    main()
