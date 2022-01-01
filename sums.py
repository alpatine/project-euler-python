def sum_numbers(upper: int) -> int:
    """Calculate the sum of naturals less than upper."""
    n = upper - 1
    return n * (n + 1) // 2

def sum_square_numbers(upper: int) -> int:
    """Calculate the sum of the squares of the naturals less than upper."""
    n = upper - 1
    return n * (2 * n + 1) * (n + 1) // 6
