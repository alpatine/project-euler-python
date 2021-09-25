def champernowne_digit(position: int) -> int:
    """Returns the digit at a given position in the champernowne constant
    
    Champernownes constant is the numer 0.123456789101112131415... where the
    decimal portion is made up by concatenating the natural numbers.

    The position value is 0-based indexing including the front 0
    Example: position = 0 -> 0
    Example: position = 1 -> 1
    Example: position = 5 -> 5
    Example: position = 10 -> 1
    Example: position = 15 -> 2
    """
    if position == 0: return 0

    # the desired digit will be a part of one of the concatenated naturals
    # work out which order that natural number is in

    order = 0
    while True:
        if position <= digits_up_to_order_of_10(order): break
        order += 1

    # now work out which natural number it is
    position_in_order = position - digits_up_to_order_of_10(order - 1)
    position_in_order_zb = position_in_order - 1 # zero based indexing
    first_number_in_order = 10 ** order
    digits_per_number_in_order = order + 1
    target_natural = position_in_order_zb // digits_per_number_in_order + first_number_in_order

    # now extract the appropriate digit from that natural number
    position_in_target_natural_zb = position_in_order_zb % digits_per_number_in_order
    return int(str(target_natural)[position_in_target_natural_zb])

def digit_factorial_sum(number: int) -> int:
    """Sums the factorial of each digit in number.

    Example: for 28 this returns 2! + 8! = 40322
    """
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return sum(factorials[int(d)] for d in str(number))

def digits_in_order_of_10(order: int) -> int:
    """Counts the digits to write out naturals in an order of 10

    Covers the range [10^order, 10^(order+1)-1]
    
    Starts with the natural number 10^order and is equivalent to writing the
    numbers into a single long string and taking the length

    Example: order = 0 -> [1, 9] -> len(123456789) -> 9
    Example: order = 1 -> [10, 99] -> len(101112...979899) -> 180
    """
    return 9 * (order + 1) * (10 ** order)

def digits_up_to_order_of_10(order: int) -> int:
    """Counts the digits to write out natural numbers up to and including
    an order of 10
    
    Covers the range [1, 10^(order+1)-1]
    
    Starts with the natural number 1 and is equivalent to writing the
    numbers into a single long string and taking the length. Also equivalent
    of summing digits_in_order_of_10 for order from 0 to order.

    Example: order = 0 -> [1, 9] -> len(123456789) -> 9
    Example: order = 1 -> [1, 99] -> len(12345...979899) -> 189
    """
    return ((10 ** (order + 1)) * (9 * order + 8) + 1) // 9

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