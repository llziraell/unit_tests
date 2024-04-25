from unittest import TestCase, main

from calculator import f_sum
from calculator import f_mul
from calculator import f_sub
from calculator import f_div
from calculator import f_pow
from calculator import f_sqrt
from calculator import f_fact

class CalculatorTest(TestCase):
    def test_sum(self):
        self.assertEqual(f_sum(2, 2), 4)
        self.assertEqual(f_sum(5, -3), 2)

    def test_sub(self):
        self.assertEqual(f_sub(2, 2), 0)
        self.assertEqual(f_sub(8, -3), 11)

    def test_mul(self):
        self.assertEqual(f_mul(2, -2), -4)
        self.assertEqual(f_mul(0, 5), 0)

    def test_div(self):
        self.assertEqual(f_div(8, 2), 4)
        self.assertEqual(f_div(15, 0), -7.5)
        self.assertRaises(ZeroDivisionError, f_div, 5, 0)

    def test_pow(self):
        self.assertEqual(f_pow(2, 2), 4)
        self.assertEqual(f_pow(5, -2), 0.04)
        self.assertEqual(f_pow(0, 8), 0)

    def test_sqrt(self):
        self.assertEqual(f_sqrt(4), 2)
        self.assertRaises(ValueError, f_sqrt, -15)
        self.assertEqual(f_sqrt(0), 0)

    def test_fact(self):
        self.assertEqual(f_fact(0), 1)
        self.assertEqual(f_fact(1), 1)
        self.assertEqual(f_fact(4), 24)
        self.assertRaises(ValueError, f_fact, -1)

if __name__ == '__main__':
    main()