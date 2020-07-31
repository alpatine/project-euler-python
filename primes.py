from math import sqrt, floor, log
from itertools import islice

def primes(upper):
    prime_list = [True] * upper
    max_factor = floor(sqrt(upper))

    for i in range(2, upper):
        if prime_list[i] == True:
            yield i
            if i <= max_factor:
                for j in range(i*i, upper, i):
                    prime_list[j] = False

def prime_factors(number):
    result = set()
    current_factor = 2
    while number > 1:
        dividend, remainder = divmod(number, current_factor)
        if remainder == 0:
            number = dividend
            result.add(current_factor)
            current_factor = current_factor - 1
        current_factor = current_factor + 1
    return result

def estimate_nth_prime(n):
    # As n gets larger, the nth prime ~ n * ln(n)
    return int(n * log(n))

def nth_prime(n):
    if n == 1: return 2
    if n == 2: return 3
    estimate = estimate_nth_prime(n)
    #return list(primes(2 * estimate))
    return list(islice(primes(2 * estimate), n - 1, n))[0]
