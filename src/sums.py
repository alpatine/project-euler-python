def digit_factorial_sum(number: int) -> int:
    """Sums the factorial of each digit in number.

    Example: for 28 this returns 2! + 8! = 40322
    """
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return sum(factorials[int(d)] for d in str(number))

def digit_sum(number: int) -> int:
    """Sums the digits in number"""
    return sum(int(digit) for digit in str(number))

def sum_numbers(upper: int) -> int:
    """Calculate the sum of naturals less than upper."""
    n = upper - 1
    return n * (n + 1) // 2

def sum_square_numbers(upper: int) -> int:
    """Calculate the sum of the squares of the naturals less than upper."""
    n = upper - 1
    return n * (2 * n + 1) * (n + 1) // 6
