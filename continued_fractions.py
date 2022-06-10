from collections import deque
from fractions import Fraction
from math import floor, sqrt
from typing import Iterator, List


def convergents(partial_fraction: List[int]) -> Iterator[Fraction]:
    """Generates the convergents of a continued fraction"""
    numerators = deque([0, 1])
    denominators = deque([1, 0])
    for coefficient in partial_fraction:
        new_numerator = coefficient*numerators[1] + numerators[0]
        new_denominator = coefficient*denominators[1] + denominators[0]
        yield Fraction(new_numerator, new_denominator)
        numerators.append(new_numerator)
        numerators.popleft()
        denominators.append(new_denominator)
        denominators.popleft()
    pass

def terms_for_sqrt_of(number: int, max_iterations: int) -> tuple[list[int],
                                                                 list[int]]:
    """Returns the continued fraction for sqrt(number)
    
    Returns a tuple containing two lists. The first contains the non-repeating
    partial denominators, the second contains the repeating partial
    denominators.
    """
    # not dealing with complex numbers
    if number < 0:
        return None
    
    # early check for perfect squares
    a0 = floor(sqrt(number))
    if a0 ** 2 == number:
        return ([a0], [])

    # seed the process
    iteration = 0
    m = 0
    d = 1
    a = a0

    terms = []
    # generate the terms
    while a != 2 * a0 and iteration < max_iterations:
        iteration += 1
        m = d*a - m
        d = (number - (m*m)) / d
        a = floor((a0 + m) / d)
        terms.append(a)
    
    return ([a0], terms)
