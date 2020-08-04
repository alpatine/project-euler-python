from primes import primes

def p10(upper: int) -> int:
    return sum(primes(upper))

if __name__ == '__main__':
    print(p10(10))
    print(p10(2000000))