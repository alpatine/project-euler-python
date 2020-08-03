from primes import prime_factors

def p3(number: int) -> int:
    return max(prime_factors(number))

if __name__ == "__main__":
    print(p3(600851475143))