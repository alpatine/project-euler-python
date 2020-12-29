from math import sqrt, floor, log
from itertools import islice
from typing import Iterator, Set, List

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

def estimate_nth_prime(n: int) -> int:
    """Estimate the n'th prime number.

    Estimation is based on n * ln(n) because the primes get closer to
    this value as n gets larger.
    """
    # As n gets larger, the nth prime ~ n * ln(n)
    return int(n * log(n))

def nth_prime(n: int) -> int:
    """Calculate the n'th prime number."""
    if n == 1: return 2
    if n == 2: return 3
    estimate = estimate_nth_prime(n)
    #return list(primes(2 * estimate))
    return list(islice(primes(2 * estimate), n - 1, n))[0]
