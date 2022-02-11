from math import exp
from unittest import TestCase
from number_theory import (count_divisors, divisor_sums_to,
                           is_hexagonal_number, is_pentagonal_number, is_prime,
                           is_triangle_number, nth_prime, pentagonal_number,
                           prime_factors, primes)


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

class Divisor_Sums_To_Test(TestCase):
    def test_2(self):
        self.assertEqual(divisor_sums_to(2), {0:0, 1: 0})
    
    def test_3(self):
        self.assertEqual(divisor_sums_to(3), {0:0, 1: 0, 2: 1})
    
    def test_4(self):
        self.assertEqual(divisor_sums_to(4), {0:0, 1: 0, 2: 1, 3: 1})
    
    def test_11(self):
        self.assertEqual(divisor_sums_to(11),
            { 0:0, 1: 0, 2: 1, 3: 1, 4: 3, 5: 1,
              6: 6, 7: 1, 8: 7, 9: 4, 10: 8})

class Is_Hexagonal_Number_Test(TestCase):
        def test_1(self):
            self.assertEqual(is_hexagonal_number(1), True)
        
        def test_2_5(self):
            for number in range(2, 6):
                self.assertEqual(is_hexagonal_number(number), False)
        
        def test_first_10(self):
            for base in range(1, 11):
                number = base * (2 * base - 1)
                self.assertEqual(is_hexagonal_number(number), True)

class Is_Prime_Test(TestCase):
    def test_1(self):
        self.assertEqual(is_prime(1), False)
        
    def test_2(self):
        self.assertEqual(is_prime(2), True)
    
    def test_19(self):
        self.assertEqual(is_prime(19), True)
    
    def test_35(self):
        self.assertEqual(is_prime(35), False)
    
    def test_10(self):
        self.assertEqual(is_prime(10), False)
    
    def test_10_coprime_true(self):
        self.assertEqual(is_prime(10, [3, 7]), True)
    
    def test_10_coprime_false(self):
        self.assertEqual(is_prime(10, [2, 3]), False)

class Is_Pentagonal_Number_Test(TestCase):
    def test_first_10(self):
        for number in range(1, 11):
            pentagonal = number * (3 * number - 1) // 2
            self.assertEqual(is_pentagonal_number(pentagonal), True)
    
    def test_2_4(self):
        for number in range(2, 5):
            self.assertEqual(is_pentagonal_number(number), False)

class Is_Triangle_Number_Test(TestCase):
    def test_1_55(self):
        for number in range(1, 11):
            triangle = number * (number + 1) // 2
            self.assertEqual(is_triangle_number(triangle), True)
    
    def test_2(self):
        self.assertEqual(is_triangle_number(2), False)

class Nth_Prime_Test(TestCase):
    def test_nth_prime_1(self):
        self.assertEqual(nth_prime(1), 2)
    
    def test_nth_prime_2(self):
        self.assertEqual(nth_prime(2), 3)
    
    def test_nth_prime_3(self):
        self.assertEqual(nth_prime(3), 5)
    
    def test_nth_prime_6(self):
        self.assertEqual(nth_prime(6), 13)

class Pentagonal_Number_Test(TestCase):
    def test_1_10(self):
        for n in range(1, 11):
            calculated = pentagonal_number(n)
            expected = n * (3 * n - 1) // 2
            self.assertEqual(calculated, expected)

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
