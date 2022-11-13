from shooping_cart import ShoppingCart
import pytest

def test_can_add_item_to_cart():
	cart = ShoppingCart(2)
	cart.add('apple')
	assert cart.size() == 1

def test_item_added():
	cart = ShoppingCart(2)
	cart.add('apple')

	assert 'apple' in cart.get_items()


def test_when_add_more_than_max():
	cart = ShoppingCart(max_size=2)
	with pytest.raises(OverflowError):
		cart.add('apple')
		cart.add('apple')
		cart.add('apple')

	
