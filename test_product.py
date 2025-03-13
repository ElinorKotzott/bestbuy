import pytest
from products import Product

# product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
#                  products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                  products.Product("Google Pixel 7", price=500, quantity=250),
#                  products.NonStockedProduct("Windows License", price=125),
#                  products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
#                ]
# best_buy = store.Store(product_list)


def test_normal_product():
    assert Product("iPod Nano 3rd Gen", price=1450, quantity=100)


def test_negative_price():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_negative_quantity():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=10, quantity=-100)


def test_empty_name():
    with pytest.raises(ValueError):
        Product("", price=10, quantity=100)


def test_price_is_zero():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=0, quantity=-100)


def test_inactive_if_quantity_zero():
    my_product = Product("MacBook Air M2", price=0, quantity=0)
    assert my_product.is_active() == False


def test_buying_modifies_quantity():
    my_product = Product("MacBook Air M2", price=20, quantity=100)
    my_product.buy(70)
    assert my_product.quantity == 30


def test_buying_produces_correct_output():
    my_product = Product("MacBook Air M2", price=20, quantity=100)
    assert my_product.buy(70) == 1400


def test_buying_too_much():
    my_product = Product("Awesome Cell Phone", price=500, quantity=300)
    with pytest.raises(ValueError):
        my_product.buy(400)
