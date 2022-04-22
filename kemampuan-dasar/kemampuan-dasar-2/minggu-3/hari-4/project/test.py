# import unittest
# from unittest import result
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


# output
"""
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
# unittest comes with lots of methods to assert on the value, types and existence of variables. Here some of the most commonly used methods :
"""
method                        equivalent to
.assertEqual(a,b)             a == b
.assertTrue(x)                bool(x) is True
.assertFalse(x)               bool(x) is False
.assertIs(a,b)                a is b
.assertIsNone(x)              x is None
.assertIn(x)                  a in b
.assertIsInstance(a,b)        isinstance(a,b)
.assertIs(),.assertIsNone(),.assertIn(),and .assertIsIntance()
all have opposite methods, names .assertIsNot(), and so forth
"""
import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
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
if __name__ == '__main__':
    unittest.main()


# output
"""
donie@donie-ThinkPad-T430:~/praxis-academy $ /bin/python3.10 "/home/donie/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu-3/hari-4/project/test.py"
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
# jika menjalankan di terminal python3 -m unittest test maka outputnya sebagai berikut:


"""
donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu-3/hari-4/project$ python3 -m unittest test
F.
======================================================================
FAIL: test_list_fraction (test.TestSum)
Test that it can sum a list of fractions
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/donie/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu-3/hari-4/project/test.py", line 56, in test_list_fraction
    self.assertEqual(result, 1)
AssertionError: Fraction(9, 10) != 1

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
"""

