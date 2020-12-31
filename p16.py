def p16(base: int, power: int) -> int:
    total = 0
    multiple = base ** power
    multiple_str = str(multiple)
    for digit in multiple_str:
        total += int(digit)
    return total


if __name__ == '__main__':
    print(p16(2, 15))
    print(p16(2, 1000))
    