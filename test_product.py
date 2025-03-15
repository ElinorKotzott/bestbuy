import pytest
from products import Product, LimitedProduct



def test_normal_product():
    assert LimitedProduct("iPod Nano 3rd Gen", price=1450, quantity=100)


def test_negative_price():
    with pytest.raises(ValueError):
        LimitedProduct("MacBook Air M2", price=-10, quantity=100)


def test_negative_quantity():
    with pytest.raises(ValueError):
        LimitedProduct("MacBook Air M2", price=10, quantity=-100)


def test_empty_name():
    with pytest.raises(ValueError):
        LimitedProduct("", price=10, quantity=100)


def test_price_is_zero():
    with pytest.raises(ValueError):
        LimitedProduct("MacBook Air M2", price=0, quantity=-100)


def test_inactive_if_quantity_zero():
    my_product = LimitedProduct("MacBook Air M2", price=0, quantity=0)
    assert my_product.is_active() == False


def test_buying_modifies_quantity():
    my_product = LimitedProduct("MacBook Air M2", price=20, quantity=100)
    my_product.buy(70)
    assert my_product.quantity == 30


def test_buying_produces_correct_output():
    my_product = LimitedProduct("MacBook Air M2", price=20, quantity=100)
    assert my_product.buy(70) == 1400


def test_buying_too_much():
    my_product = LimitedProduct("Awesome Cell Phone", price=500, quantity=300)
    with pytest.raises(ValueError):
        my_product.buy(400)


def test_second_half_price_with_one():

def test_second_half_price_with_two():
def test_second_half_price_with_three():

def test_third_one_free_with_two():
def test_third_one_free_with_three():
def test_third_one_free_with_four():

def test_percent_off():

def test_percent_off_raises_error_lower_end():
def test_percent_off_raises_error_higher_end():

