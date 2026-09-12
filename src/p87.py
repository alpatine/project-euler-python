from math import ceil

from number_theory import primes_to


def p87(stop: int) -> int:

    upper = max(
        ceil(pow(stop-24, 1/2)),
        ceil(pow(stop-20, 1/3)),
        ceil(pow(stop-12, 1/4))
    )
    primes = list(primes_to(upper))
    numbers_seen = set()

    for a in primes:
        a2 = a * a
        if a2 >= stop: break
        for b in primes:
            b3 = b * b * b
            a2_b3 = a2 + b3
            if a2_b3 >= stop: break
            for c in primes:
                c4 = c * c * c * c
                a2_b3_c4 = a2_b3 + c4
                if a2_b3_c4 >= stop: break
                numbers_seen.add(a2_b3_c4)

    return len(numbers_seen)

if __name__ == '__main__':
    print(p87(50))
    print(p87(50000000))
