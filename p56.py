from argparse import _MutuallyExclusiveGroup
from functools import reduce
from sums import digit_sum

def p56() -> int:
    return reduce(max, [digit_sum(base ** power)
                        for base in range(1, 100)
                        for power in range(1, 100)])

if __name__ == '__main__':
    print(p56())
