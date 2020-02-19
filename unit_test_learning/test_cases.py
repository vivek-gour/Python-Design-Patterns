__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2018'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'viv30ek@gmail.com'
__status__ = 'development'

import unittest

import calc


class calcTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5, 10), 15)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 2), 8)

    def test_mul(self):
        self.assertEqual(calc.mul(5, 10), 50)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)

        with self.assertRaises(ValueError):
            calc.div(10, 0)


if __name__ == "__main__":
    unittest.main()
