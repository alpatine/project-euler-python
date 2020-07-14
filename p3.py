from primes import prime_factors

def p3(number):
    return max(prime_factors(number))

print(p3(600851475143))