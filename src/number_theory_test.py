from fractions import Fraction
from unittest import TestCase

from number_theory import (composites, count_divisors, divisor_sums_to,
                           heptagonal_numbers_to, hexagonal_number,
                           hexagonal_numbers_to, is_heptagonal_number,
                           is_hexagonal_number, is_lychrel_number,
                           is_octagonal_number, is_pentagonal_number, is_prime,
                           is_square_number, is_triangle_number, nth_prime,
                           octagonal_numbers_to, pentagonal_number,
                           pentagonal_numbers_to, prime_ceil_to,
                           prime_factor_count_to, prime_factors, primes,
                           square_numbers_to, totients_to, triangle_numbers_to)


class Composites_Test(TestCase):
    def test_composites_0(self):
        self.assertEqual(list(composites(0)), [])
    
    def test_composites_3(self):
        self.assertEqual(list(composites(4)), [])
    
    def test_composites_10(self):
        self.assertEqual(list(composites(11)), [4, 6, 8, 9, 10])
    
    def test_composites_100(self):
        expected = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26,
            27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49,
            50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70,
            72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 
            93, 94, 95, 96, 98, 99, 100]
        self.assertEqual(list(composites(101)), expected)

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

class Hexagonal_Number_Test(TestCase):
    def test_1_10(self):
        for n in range(1, 11):
            calculated = hexagonal_number(n)
            expected = n * (2 * n - 1)
            self.assertEqual(calculated, expected)

class Hexagonal_Numbers_To_Test(TestCase):
    def test_hexagonal_numbers_to_100(self):
        expected = [1, 6, 15, 28, 45, 66, 91]
        hexagonals = list(hexagonal_numbers_to(100))
        self.assertEqual(hexagonals, expected)

class Heptagonal_Numbers_To_Test(TestCase):
    def test_heptagonal_numbers_to_100(self):
        expected = [1, 7, 18, 34, 55, 81]
        heptagonals = list(heptagonal_numbers_to(100))
        self.assertEqual(heptagonals, expected)

class Is_Heptagonal_Number_Test(TestCase):
    def test_heptagonals(self):
        for number in range(1, 1001):
            heptagonal = number * (5 * number - 3) // 2
            self.assertEqual(is_heptagonal_number(heptagonal), True)
    
    def test_non_heptagonals(self):
        for number in range(1, 1001):
            heptagonal = (number * (5 * number - 3) // 2) + 1
            self.assertEqual(is_heptagonal_number(heptagonal), False)

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

class Is_Lychrel_Number_Test(TestCase):
    def test_47(self):
        self.assertFalse(is_lychrel_number(47, 50))
    
    def test_196(self):
        self.assertTrue(is_lychrel_number(196, 50))
    
    def test_349(self):
        self.assertFalse(is_lychrel_number(349, 50))
    
    def test_4994(self):
        self.assertTrue(is_lychrel_number(4994, 50))

class Is_Octagonal_Number_Test(TestCase):
    def test_octagonals(self):
        for number in range(1, 1001):
            octagonal = number * (3 * number - 2)
            self.assertEqual(is_octagonal_number(octagonal), True)
    
    def test_non_octagonals(self):
        for number in range(1, 1001):
            octagonal = number * (3 * number - 2) + 1
            self.assertEqual(is_octagonal_number(octagonal), False)

class Is_Pentagonal_Number_Test(TestCase):
    def test_first_10(self):
        for number in range(1, 11):
            pentagonal = number * (3 * number - 1) // 2
            self.assertEqual(is_pentagonal_number(pentagonal), True)

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
    
    def test_2_4(self):
        for number in range(2, 5):
            self.assertEqual(is_pentagonal_number(number), False)

class Is_Square_Number_Test(TestCase):
    def test_squares(self):
        for number in range(1, 1001):
            square = number * number
            self.assertEqual(is_square_number(square), True)
    
    def test_non_squares(self):
        for number in range(1, 1001):
            non_square = number * number + 1
            self.assertEqual(is_square_number(non_square), False)

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
    
    def test_nth_prime_1000(self):
        self.assertEqual(nth_prime(1000), 7919)

class Octagonal_Numbers_To_Test(TestCase):
    def test_octagonal_numbers_to_100(self):
        expected = [1, 8, 21, 40, 65, 96]
        octagonals = list(octagonal_numbers_to(100))
        self.assertEqual(octagonals, expected)

class Pentagonal_Number_Test(TestCase):
    def test_1_10(self):
        for n in range(1, 11):
            calculated = pentagonal_number(n)
            expected = n * (3 * n - 1) // 2
            self.assertEqual(calculated, expected)

class Pentagonal_Numbers_To_Test(TestCase):
    def test_pentagonal_numbers_to_100(self):
        expected = [1, 5, 12, 22, 35, 51, 70, 92]
        pentagonals = list(pentagonal_numbers_to(100))
        self.assertEqual(pentagonals, expected)

class Prime_Ceil_To(TestCase):
    def test_1(self):
        expected = {}
        self.assertEqual(prime_ceil_to(1), expected)
    
    def test_2(self):
        expected = {1: 2}
        self.assertEqual(prime_ceil_to(2), expected)

    def test_5(self):
        expected = {
            1: 2, 2: 2, 3: 3, 4: 5,
        }
        self.assertEqual(prime_ceil_to(5), expected)
    
    def test_6(self):
        expected = {
            1: 2, 2: 2, 3: 3, 4: 5, 5: 5,
        }
        self.assertEqual(prime_ceil_to(6), expected)
    
    def test_50(self):
        expected = {
            1: 2, 2: 2, 3: 3, 4: 5, 5: 5,
            6: 7, 7: 7, 8: 11, 9: 11, 10: 11,
            11: 11, 12: 13, 13: 13, 14: 17, 15: 17,
            16: 17, 17: 17, 18: 19, 19: 19, 20: 23,
            21: 23, 22: 23, 23: 23, 24: 29, 25: 29,
            26: 29, 27: 29, 28: 29, 29: 29, 30: 31,
            31: 31, 32: 37, 33: 37, 34: 37, 35: 37,
            36: 37, 37: 37, 38: 41, 39: 41, 40: 41,
            41: 41, 42: 43, 43: 43, 44: 47, 45: 47,
            46: 47, 47: 47, 48: 53, 49: 53, 50: 53,
        }
        self.assertEqual(prime_ceil_to(51), expected)
    
    def test_50_supplied_primes(self):
        list_of_primes = list(primes(60))
        expected = {
            1: 2, 2: 2, 3: 3, 4: 5, 5: 5,
            6: 7, 7: 7, 8: 11, 9: 11, 10: 11,
            11: 11, 12: 13, 13: 13, 14: 17, 15: 17,
            16: 17, 17: 17, 18: 19, 19: 19, 20: 23,
            21: 23, 22: 23, 23: 23, 24: 29, 25: 29,
            26: 29, 27: 29, 28: 29, 29: 29, 30: 31,
            31: 31, 32: 37, 33: 37, 34: 37, 35: 37,
            36: 37, 37: 37, 38: 41, 39: 41, 40: 41,
            41: 41, 42: 43, 43: 43, 44: 47, 45: 47,
            46: 47, 47: 47, 48: 53, 49: 53, 50: 53,
        }
        self.assertEqual(prime_ceil_to(51, list_of_primes), expected)

class Prime_Factor_Count_To(TestCase):
    def test_prime_factor_count_to_1(self):
        expected = {1: 0}
        self.assertEqual(prime_factor_count_to(2), expected)
    
    def test_prime_factor_count_to_2(self):
        expected = {1: 0, 2: 1}
        self.assertEqual(prime_factor_count_to(3), expected)
    
    def test_prime_factor_count_to_50(self):
        expected = {
            1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 1, 8: 1, 9: 1, 10: 2,
            11: 1, 12: 2, 13: 1, 14: 2, 15: 2, 16: 1, 17: 1, 18: 2, 19: 1, 20: 2,
            21: 2, 22: 2, 23: 1, 24: 2, 25: 1, 26: 2, 27: 1, 28: 2, 29: 1, 30: 3,
            31: 1, 32: 1, 33: 2, 34: 2, 35: 2, 36: 2, 37: 1, 38: 2, 39: 2, 40: 2,
            41: 1, 42: 3, 43: 1, 44: 2, 45: 2, 46: 2, 47: 1, 48: 2, 49: 1, 50: 2,
        }
        self.assertEqual(prime_factor_count_to(51), expected)

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

class Square_Numbers_To_Test(TestCase):
    def test_square_numbers_to_100(self):
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81]
        squares = list(square_numbers_to(100))
        self.assertEqual(squares, expected)

class Totients_To_Test(TestCase):
    def test_totients_to_1(self):
        expected = {1: 1}
        self.assertEqual(totients_to(2), expected)
    
    def test_totients_to_20(self):
        expected = {
            1: 1, 2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 7: 6, 8: 4, 9: 6, 10: 4,
            11: 10, 12: 4, 13: 12, 14: 6, 15: 8, 16: 8, 17: 16, 18: 6, 19: 18, 20: 8,
        }
        self.assertEqual(totients_to(21), expected)

class Triangle_Numbers_To_Test(TestCase):
    def test_triangle_numbers_to_100(self):
        expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
        triangles = list(triangle_numbers_to(100))
        self.assertEqual(triangles, expected)
