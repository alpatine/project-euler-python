from unittest import TestCase
from primes import primes, prime_factors, count_divisors, nth_prime

class Primes_Test(TestCase):
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

class Prime_Factors_Test(TestCase):
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

class Count_Divisors_Test(TestCase):
    def test_count_divisors_1(self):
        self.assertEqual(count_divisors(1), 1)
    
    def test_count_divisors_3(self):
        self.assertEqual(count_divisors(3), 2)
    
    def test_count_divisors_6(self):
        self.assertEqual(count_divisors(6), 4)
    
    def test_count_divisors_10(self):
        self.assertEqual(count_divisors(10), 4)
    
    def test_count_divisors_15(self):
        self.assertEqual(count_divisors(15), 4)
    
    def test_count_divisors_21(self):
        self.assertEqual(count_divisors(21), 4)
    
    def test_count_divisors_28(self):
        self.assertEqual(count_divisors(28), 6)

class Nth_Prime_Test(TestCase):
    def test_nth_prime_1(self):
        self.assertEqual(nth_prime(1), 2)
    
    def test_nth_prime_2(self):
        self.assertEqual(nth_prime(2), 3)
    
    def test_nth_prime_3(self):
        self.assertEqual(nth_prime(3), 5)
    
    def test_nth_prime_6(self):
        self.assertEqual(nth_prime(6), 13)
    