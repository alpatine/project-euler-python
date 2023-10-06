from math import floor, sqrt
from number_theory import composites, primes

def p46(upper: int) -> int:
    prime_list = list(primes(upper))

    for c in composites(upper):
        if c % 2 == 1:  # odd
            max_n = floor(sqrt((c - 3) / 2))
            found = False
            for n in range(1, max_n + 1):
                prime_candidate = c - 2 * n * n
                if prime_candidate in prime_list:
                    found |= True
                    break
            if not found:
                return c

if __name__ == '__main__':
    print(p46(34))
    print(p46(5778))
