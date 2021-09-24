from digits import period_of_repeating_decimal

def p26(stop: int) -> int:
    # Fact: The period of repeating decimal (1/n) is always < n.

    n_with_max_period = 0
    max_period = 0
    for n in range(stop - 1, 0, -1):
        if n <= max_period: break   # per fact above
        period = period_of_repeating_decimal(n)
        if period > max_period:
            max_period = period
            n_with_max_period = n
    
    return n_with_max_period

if __name__ == '__main__':
    print(p26(10))
    print(p26(1000))