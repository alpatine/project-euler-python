from collections import Counter
from math import floor

def p52(max_digits: int) -> int:
    
    for number_of_digits in range(6, max_digits + 1):
        min_number = 10 ** (number_of_digits - 1) + 2
        max_number = (10 ** number_of_digits - 1) // 6

        for number in range(min_number, max_number + 1, 3):
            number_counter = Counter(str(number))
            if number_counter['0'] == 0 and number_counter['5'] == 0:
                continue
            found = True
            for multiplier in range(2, 7):
                multiple = number * multiplier
                multiple_counter = Counter(str(multiple))
                if number_counter != multiple_counter:
                    found = False
                    break
            if found:
                return number

if __name__ == '__main__':
    print(p52(6))
