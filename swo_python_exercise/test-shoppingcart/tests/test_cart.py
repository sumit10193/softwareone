from shoppingcart.cart import ShoppingCart
from shoppingcart.cart2 import ShoppingCart2


def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - €1.00"


def test_add_item_with_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 2)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 2 - €2.00"


def test_add_different_items():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 1 - €1.10"
    assert receipt[1] == "kiwi - 1 - €3.00"


# - Update the test suite to extend coverage and limit the number of tests which need changing when changes are introduced
def test_add_item_with_total():
    cart = ShoppingCart2()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt('json')
    print(receipt)

    assert receipt[0] == "apple - 1 - €1.00"
    assert receipt[1] == "Total - €1.00"


def test_add_item_with_multiple_quantity_with_total():
    cart = ShoppingCart2()
    cart.add_item("apple", 2)

    receipt = cart.print_receipt()
    
    assert receipt[0] == "apple - 2 - €2.00"
    assert receipt[1] == "Total - €2.00"


def test_add_different_items_with_total_and_ordering():
    cart = ShoppingCart2()
    cart.add_item("kiwi", 1)
    cart.add_item("banana", 1)

    receipt = cart.print_receipt()
    
    assert receipt[0] == "kiwi - 1 - €3.00"
    assert receipt[1] == "banana - 1 - €1.10"
    assert receipt[2] == "Total - €4.10"

def test_add_item_with_total_and_currency_conversion():
    cart = ShoppingCart2()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt('db', '£')

    assert receipt[0] == "apple - 1 - £0.87"
    assert receipt[1] == "Total - £0.87"


def test_add_item_with_multiple_quantity_with_total_and_currency_conversion():
    cart = ShoppingCart2()
    cart.add_item("apple", 2)

    receipt = cart.print_receipt('json', '$')
    
    assert receipt[0] == "apple - 2 - $2.00"
    assert receipt[1] == "Total - $2.00"


def test_add_different_items_with_total_and_currency_conversion():
    cart = ShoppingCart2()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt('json', '£')
    
    assert receipt[0] == "banana - 1 - £0.96"
    assert receipt[1] == "kiwi - 1 - £2.61"
    assert receipt[2] == "Total - £3.57"

test_add_different_items_with_total_and_ordering()
test_add_item_with_total_and_currency_conversion()
test_add_item_with_multiple_quantity_with_total_and_currency_conversion()
test_add_different_items_with_total_and_currency_conversion()
