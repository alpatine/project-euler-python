from math import ceil, prod
from typing import List, Set
from digits import is_pandigital

def p32() -> int:
    pandigital_products = set()
    pandigital_products.update(find_pandigital(2, 8, 1234, 9876, 1234, 9876))
    pandigital_products.update(find_pandigital(12, 98, 123, 987, 1234, 9876))
    return sum(pandigital_products)

def find_pandigital(
        a_min: int, a_max: int,
        b_min: int, b_max: int,
        c_min: int, c_max: int
        ) -> Set[int]:
    
    pandigital_products = set()
    
    for a in range(a_min, a_max + 1):
        b_start = max(b_min, ceil(c_min / a))
        b_stop = min(b_max, c_max // a) + 1
        for b in range(b_start, b_stop):
            c = a * b
            check_str = str(a) + str(b) + str(c)
            if is_pandigital(check_str):
                pandigital_products.add(c)
    
    return pandigital_products

if __name__ == '__main__':
    print(p32())
