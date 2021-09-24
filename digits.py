def digit_factorial_sum(number: int) -> int:
    """Sums the factorial of each digit in number.

    Example: for 28 this returns 2! + 8! = 40322
    """
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return sum(factorials[int(d)] for d in str(number))

def is_palindrome(n: str) -> bool:
    """Determine if a number is a palindrome.

    Expects the number as a string. Checks if n is equal to the reverse of n.
    """
    return n == n[::-1]

def is_pandigital(n: str) -> bool:
    """Determines if a number n is pandigital.

    Checks that each digit from 1 to 9 is present in the numbwe exactly once.
    """
    for check_digit in range(1, 10):
        check_digit_str = str(check_digit)
        found_count = sum(1 for n_char in n if n_char == check_digit_str)
        if found_count != 1: return False
    
    return True

def period_of_repeating_decimal(denominator: int) -> int:
    """Calculate the period of the repeating decimal 1/denominator

    If 1/denominator is not a repeating decimal the result is 0.
    """
    # Fact: If denominator == (2**a) * (5**b) * n where n > 1 and not
    #       divisible by 2 or 5, then the period r is the smallest integer
    #       such that 10**r is congruent to 1 (mod n)

    # calculate n by dividing out powers of 2 and 5 from denominator
    n = denominator
    while (n % 2 == 0): n //= 2
    while (n % 5 == 0): n //= 5

    # if n == 1 then no repeating cycle
    if n == 1: return 0 

    remainder = n + 1   # not equal to 1, but congruent to 1 mod n
    r = 0
    while (remainder != 1):
        remainder = (remainder * 10) % n
        r += 1
    
    # r is the smallest integer such that 10**r congruent to 1 mod n
    return r