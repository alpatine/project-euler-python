import unittest
from fibonacci import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(list(fibonacci(0)), [])
    
    def test_fibonacci_1(self):
        self.assertEqual(list(fibonacci(1)), [])
    
    def test_fibonacci_2(self):
        self.assertEqual(list(fibonacci(2)), [1])
    
    def test_fibonacci_10(self):
        self.assertEqual(list(fibonacci(10)), [1, 2, 3, 5, 8])
