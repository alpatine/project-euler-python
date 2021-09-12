from math import prod
from number_theory import is_pandigital
def p38():
    # n == 2 -> x in [5000, 9999]
    # n == 3 -> x in [100, 333]
    # n == 4 -> x in [25, 33]
    # n == 5 -> x in [5, 9]
    # n == 6 -> x == 3
    # n == 9 -> x == 1

    largest_pandigital = 0

    # ranges to try: (x_min, x_max, n_max)
    ranges_to_try = [(5000, 9999, 2), (100, 333, 3), (25, 33, 4), (5, 9, 5), (3, 3, 6), (1, 1, 9)]
    for x_min, x_max, n_max in ranges_to_try:
        n_stop = n_max + 1
        for x in range(x_max, x_min - 1, -1):
            product = calculate_concatenated_product(x, n_stop)
            if product < largest_pandigital: break
            else:
                if is_pandigital(str(product)):
                    largest_pandigital = product
    
    return largest_pandigital


def calculate_concatenated_product(x: int, n_stop: int) -> int:
    result = str(x)
    for n in range(2, n_stop):
        result += str(n * x)
    return int(result)

if __name__ == '__main__':
    print(p38())
