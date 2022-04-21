import unittest
from my_sum import sum
class TestSum(unittest.TestCase):
    def test__list__int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
# output
"""
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
# unittest baris perintah di terminal vs code
"""
donie@donie-ThinkPad-T430:~/praxis-academy $ python3 -m unittest test

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
"""
# provide additional options to change the output. One of those is -v for verbose. Try it
"""
donie@donie-ThinkPad-T430:~/praxis-academy $ python3 -m unittest -v test

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
"""
# instead of providing the name of a module containing tests, you can requests an auto discovery using the following
"""
donie@donie-ThinkPad-T430:~/praxis-academy $ python3 -m unittest discover

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
"""
# you can provide the name of the directory instead by using the -s flag and the name of the directory
"""
donie@donie-ThinkPad-T430:~/praxis-academy $ python3 -m unittest discover -s test
.....................s.....................
----------------------------------------------------------------------
Ran 43 tests in 5.494s

OK (skipped=1)
"""
# knowing unittest where must run test till can import module
"""
donie@donie-ThinkPad-T430:~/praxis-academy /kemampuan-dasar/kemampuan-dasar-2/minggu-3/hari-4/project$ python3 -m unittest discover -s test -t src
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
"""
from fractions import Fraction
