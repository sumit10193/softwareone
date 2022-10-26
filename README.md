# softwareone
Python Coding Challenge

The class ShoppingCart2 in cart2.py extends class ShoppingCart in cart.py keeping in mind the O (Open for Extension, Closed for Modification) of SOLID design principles to implement the following functionalities:

- Make the receipt print items in the order that they were added
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer
- Be able to fetch product prices from an external source (json file, database ...)
- Be able to display the product prices in different currencies (not only Euro).
- Any other changes which improve the reliability of this code in production

The test suite file test_cart.py is updated to extend coverage and limit the number of tests which need changing when changes are introduced.
