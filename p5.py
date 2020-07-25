from primes import primes
from math import floor, log, prod

def p5(upper):
    return prod(prime ** floor(log(upper, prime)) for prime in primes(upper))

if __name__ == '__main__':
    print(p5(11))
    print(p5(21))