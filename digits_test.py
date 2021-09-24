from unittest import TestCase
from digits import (digit_factorial_sum, is_palindrome, is_pandigital,
    period_of_repeating_decimal)

class Digit_Factorial_Sum_Test(TestCase):
    def test_4(self):
        self.assertEqual(digit_factorial_sum(4), 24)
    
    def test_28(self):
        self.assertEqual(digit_factorial_sum(28), 40322)
    
    def test_100(self):
        self.assertEqual(digit_factorial_sum(100), 3)
    
    def test_145(self):
        self.assertEqual(digit_factorial_sum(145), 145)

class Is_Palindrome_Test(TestCase):
    def test_1(self):
        self.assertEqual(is_palindrome('1'), True)
    
    def test_10(self):
        self.assertEqual(is_palindrome('10'), False)
    
    def test_585(self):
        self.assertEqual(is_palindrome('585'), True)
    
    def test_1001001001(self):
        self.assertEqual(is_palindrome('1001001001'), True)

class Is_Pandigital_Test(TestCase):
    def test_123456789(self):
        self.assertEqual(is_pandigital('123456789'), True)
    
    def test_empty(self):
        self.assertEqual(is_pandigital(''), False)
    
    def test_635241879(self):
        self.assertEqual(is_pandigital('635241879'), True)
    
    def test_12345(self):
        self.assertEqual(is_pandigital('12345'), False)

class Period_Of_Repeating_Decimal_Test(TestCase):
    def test_1(self):
        self.assertEqual(period_of_repeating_decimal(1), 0)

    def test_2(self):
        self.assertEqual(period_of_repeating_decimal(2), 0)
    
    def test_3(self):
        self.assertEqual(period_of_repeating_decimal(3), 1)

    def test_5(self):
        self.assertEqual(period_of_repeating_decimal(5), 0)

    def test_7(self):
        self.assertEqual(period_of_repeating_decimal(7), 6)
    
    def test_20(self):
        self.assertEqual(period_of_repeating_decimal(20), 0)

    def test_30(self):
        self.assertEqual(period_of_repeating_decimal(30), 1)