import pytest
from products import Product, LimitedProduct, NonStockedProduct



def test_normal_product():
    assert LimitedProduct("iPod Nano 3rd Gen", price=1450, quantity=100, maximum=3)


def test_negative_price():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=20)


def test_negative_quantity():
    with pytest.raises(ValueError):
        LimitedProduct("MacBook Air M2", price=10, quantity=-100, maximum=1)


def test_empty_name():
    with pytest.raises(ValueError):
        NonStockedProduct("", price=10)


def test_price_is_zero():
    with pytest.raises(ValueError):
        LimitedProduct("MacBook Air M2", price=0, quantity=-100, maximum=20)


def test_inactive_if_quantity_zero():
    my_product = LimitedProduct("MacBook Air M2", price=0, quantity=0, maximum=5)
    assert my_product.is_active() == False


def test_buying_modifies_quantity():
    my_product = LimitedProduct("MacBook Air M2", price=20, quantity=100, maximum=400)
    my_product.buy(70)
    assert my_product.quantity == 30


def test_buying_produces_correct_output():
    my_product = LimitedProduct("MacBook Air M2", price=20, quantity=100, maximum=1)
    assert my_product.buy(1) == 20


def test_buying_too_much():
    my_product = LimitedProduct("Awesome Cell Phone", price=500, quantity=300, maximum=1)
    with pytest.raises(ValueError):
        my_product.buy(400)
