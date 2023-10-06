from unittest import TestCase
from sums import digit_factorial_sum, digit_sum, sum_numbers, sum_square_numbers

class Digit_Factorial_Sum_Test(TestCase):
    def test_4(self):
        self.assertEqual(digit_factorial_sum(4), 24)
    
    def test_28(self):
        self.assertEqual(digit_factorial_sum(28), 40322)
    
    def test_100(self):
        self.assertEqual(digit_factorial_sum(100), 3)
    
    def test_145(self):
        self.assertEqual(digit_factorial_sum(145), 145)

class Digit_Sum_Test(TestCase):
    def test_1(self):
        self.assertEqual(digit_sum(1), 1)
    
    def test_24(self):
        self.assertEqual(digit_sum(24), 6)
    
    def test_googol(self):
        self.assertEqual(digit_sum(10 ** 100), 1)

class Sum_Numbers_Test(TestCase):
    def test_sum_numbers_1(self):
        self.assertEqual(sum_numbers(1), 0)
    
    def test_sum_numbers_2(self):
        self.assertEqual(sum_numbers(2), 1)
    
    def test_sum_numbers_3(self):
        self.assertEqual(sum_numbers(3), 3)

    def test_sum_numbers_11(self):
        self.assertEqual(sum_numbers(11), 55)

class Sum_Square_Numbers_Test(TestCase):
    def test_sum_square_numbers_1(self):
        self.assertEqual(sum_square_numbers(1), 0)
    
    def test_sum_square_numbers_2(self):
        self.assertEqual(sum_square_numbers(2), 1)
    
    def test_sum_square_numbers_3(self):
        self.assertEqual(sum_square_numbers(3), 5)
    
    def test_sum_square_numbers_4(self):
        self.assertEqual(sum_square_numbers(4), 14)
