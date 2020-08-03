from typing import Iterator

def fibonacci(upper: int) -> Iterator[int]:
    a, b = 1, 2
    while a < upper:
        yield a
        a, b = b, a+b
