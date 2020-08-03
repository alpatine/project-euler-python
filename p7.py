from primes import nth_prime

def p7(n: int) -> int:
    return nth_prime(n)

if __name__ == '__main__':
    print(p7(6))
    print(p7(10001))