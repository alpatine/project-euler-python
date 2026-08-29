from number_theory import primes_to
from math import floor, log, prod

def p5(upper: int) -> int:
    return prod(prime ** floor(log(upper, prime)) for prime in primes_to(upper))

if __name__ == '__main__':
    print(p5(11))
    print(p5(21))