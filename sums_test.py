from unittest import TestCase
from sums import sum_numbers, sum_square_numbers

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