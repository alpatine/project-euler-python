from math import ceil, floor, log, log10
from typing import Counter


def p63() -> int:
    # b and p are natural numbers
    # we can show that 1 <= b <= 9
    # for any b: 1 <= p <= log(10/b, 10)
    
    count = 0
    for base in range(1, 10):
        max_power = floor(log(10, 10/base))
        count += max_power
    
    return count

if __name__ == '__main__':
    print(p63())
