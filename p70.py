from collections import Counter
from number_theory import totients_to


def p70(stop: int) -> int:
    # TODO: This is too slow. Look at the totient formula and see what the
    # shortcut is.
    totients = totients_to(stop)
    del totients[1]
    min_ratio = stop
    min_n = stop

    for n, totient in totients.items():
        n_str = str(n)
        totient_str = str(totient)
        if len(n_str) == len(totient_str):
            if Counter(n_str) == Counter(totient_str):
                #print(f'{n}, {totient}')
                ratio = n / totient
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_n = n
    
    if min_n != stop:
        return min_n

if __name__ == '__main__':
    print(p70(10**7))
