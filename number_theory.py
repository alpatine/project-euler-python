from math import ceil, sqrt, floor, log
from itertools import islice
from typing import Iterator, Set, List, Dict

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

def is_hexagonal_number(number: int) -> bool:
    """Returns true if number is an hexagonal number, false otherwise"""
    potential_base = (1 + sqrt(1 + 8 * number)) * 0.25
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
