from math import floor, log
from number_theory import primes

def p29(base_stop: int, exponent_stop: int) -> int:
    # ranges: 2 <= base < base_stop
    #       : 2 <= exponent < exponent_stop
    # number = base ** exponent
    #        = (absolute_base ** base_exponent) ** exponent
    #        = absolute_base ** (base_exponent * exponent)
    #        = absolute_base ** exponent_product
    total_numbers = 0
    base_visited = [False] * base_stop
    for absolute_base in range(2, base_stop):
        if base_visited[absolute_base] == False:
            exponent_product_set = set()
            max_base_exponent = floor(log(base_stop - 1) / log(absolute_base))
            for base_exponent in range(1, max_base_exponent + 1):
                base = absolute_base ** base_exponent
                base_visited[base] = True
                for exponent in range(2, exponent_stop):
                    exponent_product = base_exponent * exponent
                    exponent_product_set.add(exponent_product)
            total_numbers += len(exponent_product_set)
    return total_numbers

if __name__ == '__main__':
    # print(p29(6, 6))
    print(p29(101, 101))
