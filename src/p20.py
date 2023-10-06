from math import factorial

def p20(number: int) -> int:
    return sum([int(digit) for digit in str(factorial(number))])

if __name__ == '__main__':
    print(p20(10))
    print(p20(100))