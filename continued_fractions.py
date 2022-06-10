from collections import deque
from fractions import Fraction
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
