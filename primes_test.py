import unittest
from primes import primes

class PrimesTest(unittest.TestCase):
    def test_primes_0(self):
        self.assertEqual(list(primes(0)), [])
    
    def test_primes_1(self):
        self.assertEqual(list(primes(1)), [])

    def test_primes_2(self):
        self.assertEqual(list(primes(2)), [])
    
    def test_primes_3(self):
        self.assertEqual(list(primes(3)), [2])
    
    def test_primes_10(self):
        self.assertEqual(list(primes(10)), [2, 3, 5, 7])
