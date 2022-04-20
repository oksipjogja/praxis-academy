import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")
    def test_sum_tuple(self):       
        self.assertEqual(sum((1,2,2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()  

""".F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/donie/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu ke 3/hari 3/test_sum_unittest.py", line 8, in test_sum_tuple
    self.assertEqual(sum((1,2,2)), 6, "Should be 6")
AssertionError: 5 != 6 : Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
"""

"""
donie@donie-ThinkPad-T430:~/praxis-academy $ pip install nose2
Collecting nose2
  Downloading nose2-0.11.0-py2.py3-none-any.whl (144 kB)
     |████████████████████████████████| 144 kB 2.0 MB/s 
Collecting coverage>=4.4.1
  Downloading coverage-6.3.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (212 kB)
     |████████████████████████████████| 212 kB 9.9 MB/s 
Collecting six>=1.7
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: coverage, six, nose2
Successfully installed coverage-6.3.2 nose2-0.11.0 six-1.16.0
donie@donie-ThinkPad-T430:~/praxis-academy $ python3 -m nose2

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
donie@donie-ThinkPad-T430:~/praxis-academy $ python3 -m nose2

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
donie@donie-ThinkPad-T430:~/praxis-academy $ python -m nose2

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK"""

def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"
def test_sum_tuple():
    assert sum((1,2,2)) == 6, "Should be 6"