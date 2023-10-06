from continued_fractions import terms_for_sqrt_of


def p64(stop: int) -> int:
    count = 0
    for number in range(2, stop):
        if len(terms_for_sqrt_of(number, 1000)[1]) % 2 == 1:
            count += 1
    
    return count

if __name__ == '__main__':
    print(p64(14))
    print(p64(10001))
