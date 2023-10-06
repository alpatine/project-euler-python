from math import gcd

def p33() -> int:
    fractions = []
    for a in range(10, 99):
        for b in range(a+1, 100):
            if (can_digit_cancel(a, b)):
                fractions.append((a, b))
    
    numerator_product = 1
    denominator_product = 1
    for fraction in fractions:
        numerator_product *= fraction[0]
        denominator_product *= fraction[1]
    
    greatest_divisor = gcd(numerator_product, denominator_product)
    return denominator_product // greatest_divisor

def can_digit_cancel(a: int, b: int) -> bool:
    a_str, b_str = str(a), str(b)
    a0, a1 = int(a_str[0]), int(a_str[1])
    b0, b1 = int(b_str[0]), int(b_str[1])

    # both numbers ending in 0 is a trivial case and
    # not a solution
    if a1 == 0 and b1 == 0: return False

    quotient = a / b

    if b0 != 0:
        if a0 == b1 and a1 / b0 == quotient:
            return True
        if a1 == b1 and a0 / b0 == quotient:
            return True
    if b1 != 0:
        if a0 == b0 and a1 / b1 == quotient:
            return True
        if a1 == b0 and a0 / b1 == quotient:
            return True
    
    return False

if __name__ == '__main__':
    print(p33())