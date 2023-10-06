from unittest import TestCase
from digits import (champernowne_digit, digits_in_order_of_10,
                    digits_up_to_order_of_10, is_anagram, is_palindrome,
                    is_pandigital, period_of_repeating_decimal)

class Is_Anagram_Test(TestCase):
    def test_1_1(self):
        self.assertEqual(is_anagram('1', '1'), True)
    
    def test_1234_3124(self):
        self.assertEqual(is_anagram('1234', '3124'), True)
    
    def test_1212_2211(self):
        self.assertEqual(is_anagram('1212', '2211'), True)
    
    def test_111345_31415(self):
        self.assertEqual(is_anagram('111345', '31415'), False)
    
    def test_1(self):
        self.assertEqual(is_anagram('1', ''), False)

class Champernowne_Digit_Test(TestCase):
    def test_0(self):
        self.assertEqual(champernowne_digit(0), 0)
    
    def test_1(self):
        self.assertEqual(champernowne_digit(1), 1)
    
    def test_5(self):
        self.assertEqual(champernowne_digit(5), 5)
    
    def test_10(self):
        self.assertEqual(champernowne_digit(10), 1)
    
    def test_12(self):
        self.assertEqual(champernowne_digit(12), 1)
    
    def test_15(self):
        self.assertEqual(champernowne_digit(15), 2)
    
    def test_100(self):
        self.assertEqual(champernowne_digit(100), 5)
    
    def test_1000(self):
        self.assertEqual(champernowne_digit(1000), 3)
    
    def test_10000(self):
        self.assertEqual(champernowne_digit(10000), 7)
    
    def test_100000(self):
        self.assertEqual(champernowne_digit(100000), 2)
    
    def test_1000000(self):
        self.assertEqual(champernowne_digit(1000000), 1)

class Digits_In_Order_Of_10_Test(TestCase):
    def test_0(self):
        self.assertEqual(digits_in_order_of_10(0), 9)
    
    def test_1(self):
        self.assertEqual(digits_in_order_of_10(1), 180)
    
    def test_2(self):
        self.assertEqual(digits_in_order_of_10(2), 2700)

    def test_10(self):
        self.assertEqual(digits_in_order_of_10(10), 990000000000)

class Digits_Up_To_Order_Of_10_Test(TestCase):
    def test_0(self):
        self.assertEqual(digits_up_to_order_of_10(0), 9)
    
    def test_1(self):
        self.assertEqual(digits_up_to_order_of_10(1), 189)
    
    def test_5(self):
        self.assertEqual(digits_up_to_order_of_10(5), 5888889)

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
        self.assertEqual(is_pandigital(''), True)
    
    def test_635241879(self):
        self.assertEqual(is_pandigital('635241879'), True)
    
    def test_12345(self):
        self.assertEqual(is_pandigital('12345'), True)

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
