from unittest import TestCase
from number_theory import (count_divisors, digit_factorial_sum, divisor_sums_to, is_palindrome, is_pandigital, is_prime,
    nth_prime, period_of_repeating_decimal, prime_factors, primes)

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

class Digit_Factorial_Sum_Test(TestCase):
    def test_4(self):
        self.assertEqual(digit_factorial_sum(4), 24)
    
    def test_28(self):
        self.assertEqual(digit_factorial_sum(28), 40322)
    
    def test_100(self):
        self.assertEqual(digit_factorial_sum(100), 3)
    
    def test_145(self):
        self.assertEqual(digit_factorial_sum(145), 145)

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

class Nth_Prime_Test(TestCase):
    def test_nth_prime_1(self):
        self.assertEqual(nth_prime(1), 2)
    
    def test_nth_prime_2(self):
        self.assertEqual(nth_prime(2), 3)
    
    def test_nth_prime_3(self):
        self.assertEqual(nth_prime(3), 5)
    
    def test_nth_prime_6(self):
        self.assertEqual(nth_prime(6), 13)

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
