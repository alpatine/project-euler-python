from collections import deque
from fractions import Fraction
from itertools import islice
from math import ceil, floor, log, sqrt
from typing import Dict, Iterator, List, Set

from digits import is_palindrome


def composites(upper: int) -> Iterator[int]:
    """Generate the composite numbers.

    The sequence starts with 4 and continues until upper is reached.
    The value upper is not included in the sequence.
    """
    prime_list = [True] * upper
    max_factor = floor(sqrt(upper))

    for i in range(2, upper):
        if prime_list[i] == True:
            if i <= max_factor:
                for j in range(i*i, upper, i):
                    prime_list[j] = False
        else:
            yield i

def convergents(partial_fraction: List[int]) -> Iterator[Fraction]:
    """Generates the convergents of a partial fraction"""
    numerators = deque([0, 1])
    denominators = deque([1, 0])
    for coefficient in partial_fraction:
        new_numerator = coefficient*numerators[1] + numerators[0]
        new_denominator = coefficient*denominators[1] + denominators[0]
        yield Fraction(new_numerator, new_denominator)
        numerators.append(new_numerator)
        numerators.popleft()
        denominators.append(new_denominator)
        denominators.popleft()
    pass

def count_divisors(number: int, prime_numbers: Iterator[int] = None) -> int:
    """Count the divisors of number.

    By default a list of prime numbers is generated on each use of this function.
    A pre-generated custom list of primes can be supplied via the optional
    prime_numbers parameter.
    """
    if prime_numbers is None:
        prime_numbers = primes(number + 1)

    divisors = 1
    for prime in prime_numbers:
        factor = prime
        prime_power = 1
        while factor <= number:
            if number % factor == 0:
                factor *= prime
                prime_power += 1
            else: break
        divisors *= prime_power
    return divisors

def divisor_sums_to(number: int) -> Dict[int, int]:
    """Returns a dictionary of numbers with the sum of their proper divisors, stopping before number

    Proper divisors of a number are the numbers less than that number that divide
    evenly into it e.g. the proper divisors of 10 are: 1, 2, 5 and the sum is 8.
    """
    divisor_sums = {n: 0 for n in range(0, number)}
    for n in range(1, number):
        for multiple_of_n in range(2 * n, number, n):
            divisor_sums[multiple_of_n] += n

    return divisor_sums

def estimate_nth_prime(n: int) -> int:
    """Estimate the n'th prime number.

    Estimation is based on n * ln(n) because the primes get closer to
    this value as n gets larger.
    """
    # As n gets larger, the nth prime ~ n * ln(n)
    return int(n * log(n))

def hexagonal_number(n: int) -> int:
    """Calculates the n'th hexagonal number"""
    return n * (2 * n - 1)

def is_heptagonal_number(number: int) -> bool:
    """Returns true if number if an heptagonal number, false otherwise"""
    potential_base = (3 + sqrt(40 * number + 9)) * 0.1
    return ceil(potential_base) == floor(potential_base)

def is_hexagonal_number(number: int) -> bool:
    """Returns true if number is an hexagonal number, false otherwise"""
    potential_base = (1 + sqrt(1 + 8 * number)) * 0.25
    return ceil(potential_base) == floor(potential_base)

def is_lychrel_number(number: int, iteration_stop: int) -> bool:
    """Returns true if number is a Lychrel number
    
    There are no numbers proven to be Lychrel. This process will use
    iteration limited by the iteration_stop value.
    """
    test_number = number
    for _ in range(iteration_stop):
        test_number = test_number + int(str(test_number)[::-1])
        if is_palindrome(str(test_number)):
            return False
            
    return True

def is_octagonal_number(number: int) -> bool:
    """Returns true if number is an octagonal number, false otherwise"""
    potential_base = (sqrt(3 * number + 1) + 1) / 3
    return ceil(potential_base) == floor(potential_base)

def is_pentagonal_number(number: int) -> bool:
    """Returns true if number is a pentagonal number, false otherwise"""
    potential_base = (sqrt(24 * number + 1) + 1) / 6
    return ceil(potential_base) == floor(potential_base)

def is_prime(n: int, list_of_factors: List[int] = None) -> bool:
    """Determine if a number n is prime (or coprime to a list of factors)"""
    if n < 2: return False
    max_factor = floor(sqrt(n))
    if list_of_factors is None:
        list_of_factors = primes(max_factor + 1)
    
    for factor in list_of_factors:
        if factor > max_factor: break
        if n % factor == 0:
            return False
    
    return True

def is_square_number(number: int) -> bool:
    """Returns true if number is a square number, false otherwise."""
    potential_base = sqrt(number)
    return ceil(potential_base) == floor(potential_base)

def is_triangle_number(number: int) -> bool:
    """Returns true if number is a triangle number, false otherwise."""
    potential_base = (sqrt(8 * number + 1) - 1) * 0.5
    return ceil(potential_base) == floor(potential_base)

def nth_prime(n: int) -> int:
    """Calculate the n'th prime number."""
    if n == 1: return 2
    if n == 2: return 3
    estimate = estimate_nth_prime(n)
    #return list(primes(2 * estimate))
    return list(islice(primes(2 * estimate), n - 1, n))[0]

def pentagonal_number(n: int) -> int:
    """Calculates the n'th pentagonal number"""
    return n * (3 * n - 1) // 2

def prime_ceil_to(stop: int, list_of_primes: List[int] = None) -> List[int]:
    """Generates a dict of the 'ceiling' to the next prime number
    
    Keys start at 1 and go to stop (exclusive). Values contain the smallest
    prie number that is greater than or equal to the key.
    
    Example: Key 4 will have the value 5 because 5 is the smallest prime
    that is greater than or equal to 4 (greater than in this case).

    Example: Key 5 will have the value 5 because 5 is the smallest prime
    that is greater than or equal to 5 (equal to in this case)."""
    if list_of_primes == None:
        list_of_primes = list(primes(stop * 2)) # bertrand's postulate
    result = {}
    key_value_start = 1
    for prime in list_of_primes: 
        for key_number in range(key_value_start, min(stop, prime + 1)):
            result[key_number] = prime
        key_value_start = prime + 1
        if prime >= stop:
            break
    
    return result

def prime_factor_count_to(stop: int) -> Dict[int, int]:
    """Generates the prime factor counts up to stop (exclusive)
    
    Generates a dictionary where the keys are the natural numbers
    and the values are the number of distinct primes that divide
    the key.
    """
    prime_factor_counts = {n: 0 for n in range(1, stop)}
    for base_prime in primes(stop):
        for number in range(base_prime, stop, base_prime):
            prime_factor_counts[number] += 1
    
    return prime_factor_counts

def prime_factors(number: int) -> Set[int]:
    """Calculate the primes that will divide number.

    Prime numbers with a power of zero are not included.
    Prime numbers with a power greater than 1 are not repeated.
    """
    result = set()
    current_factor = 2
    while number > 1:
        quotient, remainder = divmod(number, current_factor)
        if remainder == 0:
            number = quotient
            result.add(current_factor)
            current_factor = current_factor - 1
        current_factor = current_factor + 1
    return result

def primes(upper: int) -> Iterator[int]:
    """Generate the prime numbers.

    The sequence starts with 2 and continues until upper is reached.
    The value upper is not included in the sequence.
    """
    prime_list = [True] * upper
    max_factor = floor(sqrt(upper))

    for i in range(2, upper):
        if prime_list[i] == True:
            yield i
            if i <= max_factor:
                for j in range(i*i, upper, i):
                    prime_list[j] = False

def totients_to(stop: int) -> Dict[int, int]:
    """Generates euler totients up to stop (exclusive)"""
    totient_set = {n: n for n in range(1, stop)}
    for prime_factor in primes(stop):
        for number in range(prime_factor, stop, prime_factor):
            totient_set[number] = totient_set[number] * (prime_factor - 1) // prime_factor

    return totient_set
