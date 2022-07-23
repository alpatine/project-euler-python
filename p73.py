from argparse import _MutuallyExclusiveGroup
from collections import deque
from fractions import Fraction

from farey import term_left_of

def p73(n: int, start: Fraction, end: Fraction) -> int:
    # counts the number of fractions in the Farey sequence
    # F_(farey_denominator) between start and end, not including start/end
    left_of_start = term_left_of(n, start)
    end_tuple = (end.numerator, end.denominator)
    count = 0
    (a, b, c, d) = (left_of_start.numerator, left_of_start.denominator,
                    start.numerator, start.denominator)
    while (c, d) != end_tuple:
        k = (n + b) // d
        (a, b, c, d) = (c, d, k*c - a, k*d - b)
        count += 1
    
    return (count - 1)

if __name__ == '__main__':
    print(p73(8, Fraction(1, 3), Fraction(1, 2)))
    print(p73(12000, Fraction(1, 3), Fraction(1, 2)))

