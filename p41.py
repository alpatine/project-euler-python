from number_theory import primes
from digits import is_pandigital

def p41():
    primes_list = [p for p in primes(10000000) if len(str(p)) in [4, 7]]
    primes_list.reverse()
    return next(pandigital_prime
                for pandigital_prime in primes_list
                if is_pandigital(str(pandigital_prime)))

if __name__ == '__main__':
    print(p41())
