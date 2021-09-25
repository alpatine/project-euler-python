from math import prod
from typing import List
from digits import champernowne_digit

def p40(positions: List[int]) -> int:
    return prod(champernowne_digit(n) for n in positions)

if __name__ == '__main__':
    print(p40([1, 10, 100, 1000, 10000, 100000, 1000000]))
