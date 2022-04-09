from number_theory import is_lychrel_number


def p55(stop: int) -> int:
    lychrel_number_count = 0
    for number in range(1, stop):
        if is_lychrel_number(number, 50):
            lychrel_number_count += 1
    return lychrel_number_count

if __name__ == '__main__':
    print(p55(10000))
