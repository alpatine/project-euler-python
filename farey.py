from fractions import Fraction
from typing import Iterable

from number_theory import totients_to


def calculate_mediant(left: Fraction, right: Fraction) -> Fraction:
    """Calculates the mediant of two fractions"""
    return Fraction(left.numerator + right.numerator,
                    left.denominator + right.denominator)

def farey_sequence(n: int) -> Iterable[int]:
    """ Generate ordered set of fractions up to specified denominator
    
    Sequence always starts with 0/1, 1/denominator, ...
    Example: F_5 = [0/1, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 1/1]
    """
    yield Fraction(0, 1)

    (a, b, c, d) = (0, 1, 1, n)
    while (c <= n):
        yield Fraction(c, d)
        k = (n + b) // d
        (a, b, c, d) = (c, d, k*c - a, k*d - b)

def farey_sequence_length(n: int) -> int:
    """Claculate number of terms in a Farey sequence.
    
    Includes the 0/1 and 1/1 terms in the count.
    """
    if n < 1:
        return None
    
    totients = totients_to(n + 1)
    return 1 + sum(totients.values())

def term_left_of(n: int, target: Fraction) -> Fraction:
    """Finds the term left of 'term' in the Farey sequence F_n"""
    candidate = Fraction(0, 1)
    mediant = calculate_mediant(candidate, target)
    while mediant.denominator <= n:
        candidate = mediant
        mediant = calculate_mediant(candidate, target)
    
    return candidate
