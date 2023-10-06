from typing import List
from digits import is_anagram
from number_theory import prime_ceil_to, primes

def p49() -> List[List[int]]:
    list_of_primes = [n for n in primes(10000) if n >= 1000]
    next_prime_map = prime_ceil_to(10000)
    number_of_primes = len(list_of_primes)
    result = []
    for a_index in range(0, number_of_primes):
        a = list_of_primes[a_index]
        for b_index in range(a_index + 1, number_of_primes):
            b = list_of_primes[b_index]
            candidate_c = 2 * b - a
            if candidate_c > 9999:
                break
            if candidate_c == next_prime_map[candidate_c]:
                if is_anagram(str(a), str(b)):
                    if is_anagram(str(a), str(candidate_c)):
                        result.append([a, b, candidate_c])
            if len(result) == 2: # we know there are only two
                break
        if len(result) == 2: # we know there are only two
            break

    return result

if __name__ == '__main__':
    for list in p49():
        print(''.join(map(str, list)))