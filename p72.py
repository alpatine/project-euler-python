from number_theory import totients_to


def p72(denominator_stop: int) -> int:
    if denominator_stop <= 1:
        return None

    # Set including 0/1 and 1/1 has size = 1 + sum of totients to n
    # We don't have 0/1 and 1/1, so subtract 1 from the sum instead
    totients = totients_to(denominator_stop)
    return sum(totients.values()) - 1

if __name__ == '__main__':
    print(p72(9))
    print(p72(1000001))
