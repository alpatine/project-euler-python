from number_theory import hexagonal_number, is_pentagonal_number, is_triangle_number

def p45(start: int, stop: int) -> int:
    for base in range(start, stop):
        number = hexagonal_number(base)
        if is_pentagonal_number(number) and is_triangle_number(number):
            return number

if __name__ == '__main__':
    print(p45(1, 2))
    print(p45(2, 145))
    print(p45(145, 100000))
