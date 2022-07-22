from fractions import Fraction
from math import floor


def p71(target: Fraction, denominator_stop: int) -> Fraction:
    # n = numerator, d = denominator
    # lim(k->inf, (nk+a)/(dk+b)) = n/d
    # Set k = 1, and find the a,b that is closest to target from below
    n = target.numerator
    d = target.denominator
    best_a = 0
    best_b = 0
    smallest_shortfall = target

    for a in range(0, n):
        for b in range(0, d):
            shortfall = target - (n+a)/(d+b)
            if shortfall > 0:
                if shortfall < smallest_shortfall:
                    smallest_shortfall = shortfall
                    best_a = a
                    best_b = b
                break

    k = floor((denominator_stop - best_b - 1) / d)
    result_numerator = n * k + best_a
    result_denominator = d * k + best_b
    return Fraction(result_numerator, result_denominator)

if __name__ == '__main__':
    print(p71(Fraction(3, 7), 9))
    print(p71(Fraction(3, 7), 1000001))
