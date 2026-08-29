from number_theory import primes_to

def p10(upper: int) -> int:
    return sum(primes_to(upper))

if __name__ == '__main__':
    print(p10(10))
    print(p10(2000000))