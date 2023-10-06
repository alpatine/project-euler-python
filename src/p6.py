from sums import sum_numbers, sum_square_numbers

def p6(upper: int) -> int:
    return sum_numbers(upper) ** 2 - sum_square_numbers(upper)

if __name__ == '__main__':
    print(p6(11))
    print(p6(101))
