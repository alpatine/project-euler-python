from collections import Counter
from itertools import dropwhile
from math import floor, sqrt
from number_theory import primes, totients_to

def p70(stop: int) -> int:
    PRIME_SPREAD = 1000
    sqrt_stop = floor(sqrt(stop))
    min_ratio = stop
    min_n = stop
    # prime_numbers = [p for p in primes(sqrt_stop + PRIME_SPREAD)
    #                 if p > sqrt_stop - PRIME_SPREAD]
    prime_numbers = list(dropwhile(lambda p: p < sqrt_stop - PRIME_SPREAD,
                                   primes(sqrt_stop + PRIME_SPREAD)))
    
    for p in prime_numbers:
        for q in prime_numbers:
            if q == p:
                break

            n = p * q
            if n >= stop:
                break

            totient = (p - 1) * (q - 1)

            n_str = str(n)
            totient_str = str(totient)
            if len(n_str) == len(totient_str):
                if Counter(n_str) == Counter(totient_str):
                    ratio = n / totient
                    if ratio < min_ratio:
                        min_ratio = ratio
                        min_n = n
    
    if min_n != stop:
        return min_n

if __name__ == '__main__':
    print(p70(10**7))
