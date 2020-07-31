import unittest
from primes import primes, prime_factors, nth_prime

class Primes_Test(unittest.TestCase):
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

class Prime_Factors_Test(unittest.TestCase):
    def test_prime_factors_1(self):
        self.assertEqual(list(prime_factors(1)), [])
    
    def test_prime_factors_2(self):
        self.assertEqual(list(prime_factors(2)), [2])
    
    def test_prime_factors_3(self):
        self.assertEqual(list(prime_factors(3)), [3])
    
    def test_prime_factors_10(self):
        self.assertEqual(list(prime_factors(10)), [2, 5])
    
    def test_prime_factors_20(self):
        self.assertEqual(list(prime_factors(20)), [2, 5])

class Nth_Prime_Test(unittest.TestCase):
    def test_nth_prime_1(self):
        self.assertEqual(nth_prime(1), 2)
    
    def test_nth_prime_2(self):
        self.assertEqual(nth_prime(2), 3)
    
    def test_nth_prime_3(self):
        self.assertEqual(nth_prime(3), 5)
    
    def test_nth_prime_6(self):
        self.assertEqual(nth_prime(6), 13)
    