import typing

from . import cart

from collections import OrderedDict

import json

import sqlite3

class ShoppingCart2(cart.ShoppingCart):
    def __init__(self):
        # - Make the receipt print items in the order that they were added
        self._items = OrderedDict()
        self.currency_rate = {"£": {"£":1.00, "€": 1.15, "$": 1.00},
                              "€": {"€":1.00, "£": 0.87, "$": 1.00},
                              "$": {"$":1.00, "£": 0.86, "€": 1.00}
                             }
        self._create_product_database()

    def _get_conversion_rate(self, currency_code, desired_currency_code):
        return self.currency_rate[currency_code][desired_currency_code]

    def print_receipt(self, source:str=None, desired_currency_code:str='€') -> typing.List[str]:
        lines = []
        total = 0.0

        for item in self._items.items():
            # - Be able to display the product prices in different currencies (not only Euro).
            unit_price, currency_code = self._get_product_price2(item[0], source)
            price = unit_price * item[1] * self._get_conversion_rate(currency_code, desired_currency_code)

            #- Add a 'Total' line to the receipt. This should be the full price we should charge the customer
            total += price

            price_string = desired_currency_code+"%.2f" % price

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

        total_string = desired_currency_code + "%.2f" % total

        lines.append("Total - " + total_string) #Appended total for the full price
        
        return lines

    def _get_product_price2(self, product_code: str, source: str=None) -> (float, str):
        # - Be able to fetch product prices from an external source (json file, database ...)
        if source == 'json':
            price, currency_code = self._get_product_price_json(product_code)
        elif source == 'db':
            price, currency_code = self._get_product_price_db(product_code)
        else: 
            price = self._get_product_price(product_code)
            currency_code = '€'

        return price, currency_code

    def _get_product_price_json(self, product_code: str) -> (float, str):
        # - Be able to fetch product prices from an external source (json file)
        with open('shoppingcart/products.json', 'r') as json_file:
            #print(json_file.read())
            json_data = json.load(json_file)

            price = json_data[product_code]['price']
            currency_code = json_data[product_code]['currency_code']

        return price, currency_code
        #return 1.0, 2.0

    def _get_product_price_db(self, product_code: str) -> (float, str):
        # - Be able to fetch product prices from an external source (database)
        db_conn = sqlite3.connect('products.db')
        cursor = db_conn.cursor()

        query_string = "SELECT price, currency_code FROM products WHERE product_code='%s';" %(product_code)
        #print(query_string)
        cursor.execute(query_string)

        price, currency_code = cursor.fetchone()

        return price, currency_code

    def _create_product_database(self):
        db_conn = sqlite3.connect('products.db')

        create_tbl_query = '''
        CREATE TABLE products(
        product_code TEXT PRIMARY KEY,
        price REAL NOT NULL,
        currency_code TEXT NOT NULL
        );
        '''
        drop_tbl_query = '''DROP TABLE products;'''
        db_conn.execute(drop_tbl_query)
        db_conn.execute(create_tbl_query)
        
        db_conn.execute('''INSERT INTO products (product_code, price, currency_code) VALUES ("apple",1.0,'€');''')
        db_conn.execute('''INSERT INTO products (product_code, price, currency_code) VALUES ("banana",1.1,'€');''')
        db_conn.execute('''INSERT INTO products (product_code, price, currency_code) VALUES ("kiwin",3.0,'€');''')
        db_conn.commit()
        db_conn.close()

