from continued_fractions import convergents


def p65() -> int:
    # first 100 terms in the continued fraction for e
    e = [2]
    k = 2
    for position in range(2, 101):
        if position % 3 == 0:
            e.append(k)
            k += 2
        else:
            e.append(1)
    
    # sum digits in numerator of 100th convergent
    convergents_of_e = list(convergents(e))
    last_numerator =  convergents_of_e[-1].numerator
    return sum(map(int, str(last_numerator)))

if __name__ == '__main__':
    print(p65())
