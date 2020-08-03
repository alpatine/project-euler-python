from primes import nth_prime

def p7(n: int) -> int:
    return nth_prime(n)

if __name__ == '__main__':
    print(list(p7(6))[0])
    print(list(p7(10001))[0])