from typing import List
from number_theory import convergents

def p57(partial_fraction: List[int]) -> int:
    count = 0
    for fraction in convergents(partial_fraction):
        if len(str(fraction.numerator)) > len(str(fraction.denominator)):
            count += 1
    
    return count

if __name__ == '__main__':
    print(p57([1] + [2] * 8))
    print(p57([1] + [2] * 1000))
