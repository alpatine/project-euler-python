from number_theory import primes


def p69(stop: int) -> int:
    running_product = 1
    for prime_number in primes(stop):
        if running_product * prime_number < stop:
            running_product *= prime_number
        else:
            return running_product

if __name__ == '__main__':
    print(p69(11))
    print(p69(1000001))
