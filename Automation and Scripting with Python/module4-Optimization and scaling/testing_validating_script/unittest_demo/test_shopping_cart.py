import unittest
from shopping_cart import calculate_discount

# Defining a test case class for shopping cart functionalities it inherits from unittest.TestCase
class TestShoppingCart(unittest.TestCase):
    # definig a test method to check discount calculation
    def test_discount_calculation(self):
        original_price = 100 
        discount_percentage = 20
        expected_discounted_price = 80.00

        discounted_price = calculate_discount(original_price, discount_percentage)
        self.assertEqual(discounted_price, expected_discounted_price)

# this block triggers the test execution
if __name__ == '__main__':
    unittest.main()