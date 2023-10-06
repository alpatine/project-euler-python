from typing import Iterator
from math import floor, pow, sqrt, log

def fibonacci(upper: int) -> Iterator[int]:
    """Generate the fibonacci sequence of numbers.

    The sequence outputs 1 once e.g. 1, 2, 3, 5, ...
    The sequence stops with the highest value less than upper.
    """
    a, b = 1, 2
    while a < upper:
        yield a
        a, b = b, a+b

def largest_fib_index_with_n_digits(n: int) -> int:
    phi = (1.0 + sqrt(5)) / 2.0
    index = floor(n / log(phi, 10) + 0.5 * log(5, phi))
    return index