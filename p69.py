from number_theory import totients_to


def p69(stop: int) -> int:
    max_ratio = 0
    max_ratio_n = 0
    totients = totients_to(stop)
    for n, totient_n in totients.items():
        ratio = n / totient_n
        if ratio > max_ratio:
            max_ratio = ratio
            max_ratio_n = n
    return max_ratio_n

if __name__ == '__main__':
    print(p69(11))
    print(p69(1000001))
