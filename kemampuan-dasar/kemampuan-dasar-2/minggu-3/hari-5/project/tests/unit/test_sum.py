import my_app
import unittest
from fractions import Fraction

class MyTestCase(unittest.TestCase):
    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client(1)
    def test_home(self):
        result = self.app.get('/')
        # Make your assertions
import unittest

from my_app import sum
class TestSum(unittest.TestCase):
    
    def test_list_int(self):
        """
        Test that it can sum list of integers
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)
    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ =='__main__':
    unittest.main()

class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='fixtures/test_basic.json')
    
    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)
    
    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Orag XYZ")
        self.assertEqual(customer.address, "10 Red Road,Reading")

class TestComplexData(unittest.TestCase):
    def setUp(self):
        # load test data
        self.app = App(database='fixture/test_complex.json')
        
    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, u"バナナ")
        self.assertEqual(customer.address, "10 Red Road, Reading")    
    
if __name__ == "__main__":
    unittest.main() 

