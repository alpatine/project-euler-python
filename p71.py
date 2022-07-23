from fractions import Fraction
from farey import term_left_of

def p71(n: int, target: Fraction) -> Fraction:
    return term_left_of(n, target)

if __name__ == '__main__':
    print(p71(8, Fraction(3, 7)))
    print(p71(1000000, Fraction(3, 7)))
