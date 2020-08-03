from typing import Iterator

def fibonacci(upper: int) -> Iterator[int]:
    """Generate the fibonacci sequence of numbers.

    The sequence outputs 1 once e.g. 1, 2, 3, 5, ...
    The sequence stops with the highest value less than upper.
    """
    a, b = 1, 2
    while a < upper:
        yield a
        a, b = b, a+b
