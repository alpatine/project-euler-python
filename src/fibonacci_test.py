from unittest import TestCase
from fibonacci import fibonacci, largest_fib_index_with_n_digits

class Fibonacci_Test(TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(list(fibonacci(0)), [])
    
    def test_fibonacci_1(self):
        self.assertEqual(list(fibonacci(1)), [])
    
    def test_fibonacci_2(self):
        self.assertEqual(list(fibonacci(2)), [1])
    
    def test_fibonacci_10(self):
        self.assertEqual(list(fibonacci(10)), [1, 2, 3, 5, 8])

class Largest_Fib_Index_With_N_Digits_Test(TestCase):
    def test_1(self):
        self.assertEqual(largest_fib_index_with_n_digits(1), 6)
    
    def test_2(self):
        self.assertEqual(largest_fib_index_with_n_digits(2), 11)

    def test_3(self):
        self.assertEqual(largest_fib_index_with_n_digits(3), 16)