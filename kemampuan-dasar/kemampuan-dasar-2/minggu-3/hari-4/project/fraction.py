
import unittest
from unittest import result
# from my_sum import sum
# class TestSum(unittest.TestCase):
#     def test__list__int(self):
#         """
#         Test that it can sum a list of integers
#         """
#         data = [1,2,3]
#         result = sum(data)
#         self.assertEqual(result, 6)

# if __name__ == '__main__':
#     unittest.main()
    
  
from fractions import Fraction 

# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """
#         Test that it can sum a list of integers
#         """
#         data = [1,2,3]
#         result = sum(data)
#         self.assertEqual(result, 6)
   
def test_list_fraction(self):
    """
    Test that it can sum a list of fractions
    """
    data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
    result = sum(data)
    self.assertEqual(result, 2)
    if __name__ == '__main__':
            unittest.main()

