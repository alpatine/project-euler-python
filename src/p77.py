from number_theory import primes
from p31 import p31

def p77(target_ways: int, search_stop: int) -> int:
    prime_list = list(primes(search_stop))
    for trial_number in range(1, search_stop):
        ways = p31(trial_number, prime_list)
        if ways >= target_ways:
            return trial_number
    

if __name__ == '__main__':
    print(p77(5, 11))
    print(p77(5000, 100))
