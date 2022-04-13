from itertools import combinations
from number_theory import is_prime, primes
from math import comb

def p60(set_size: int, max_include_prime: int, max_check_prime: int) -> int:
    check_primes_list = list(primes(max_check_prime))[1:]
    include_primes_list = [p for p in check_primes_list
                           if p < max_include_prime]
    concat_map = prepare_concat_map(include_primes_list, check_primes_list)
    results = {
        'smallest_sum': set_size * max_include_prime,
        'valid_sets': []
    }
    walk_prime_tree(concat_map,
                    set(),
                    set_size,
                    0,
                    results)
    return min(map(sum, results['valid_sets']))

def prepare_concat_map(source_primes: list[int],
                       check_primes: list[int]) -> dict[int, set[int]]:
    left_to_right = {}
    for prime_pair in combinations(source_primes, 2):
        left_prime = str(prime_pair[0])
        right_prime = str(prime_pair[1])
        left_right_prime = is_prime(int(left_prime + right_prime),
                                    check_primes)
        right_left_prime = is_prime(int(right_prime + left_prime),
                                    check_primes)
        if left_right_prime and right_left_prime:
            left_to_right.setdefault(prime_pair[0], set()).add(prime_pair[1])
    return left_to_right

def walk_prime_tree(primes_available: dict[int, list[int]],
                    primes_collected: set[int],
                    number_primes_to_find: int,
                    running_sum: int,
                    outputs: list[set[int]]) -> None:
    for p in primes_available:
        if running_sum + p >= outputs['smallest_sum']:
            return
        p_targets = primes_available[p]
        target_intersect = p_targets & primes_available.keys()
        if len(target_intersect) == 0:
            if number_primes_to_find == 1:
                result = primes_collected.copy()
                result.add(p)
                outputs['valid_sets'].append(result)
                outputs['smallest_sum'] = running_sum + p
            continue
        else:
            next_primes_available = {p:primes_available[p]
                                     for p in target_intersect}
            next_primes_collected = primes_collected.copy()
            next_primes_collected.add(p)
            walk_prime_tree(next_primes_available,
                            next_primes_collected,
                            number_primes_to_find - 1,
                            running_sum + p,
                            outputs)
    

def check_prime_set(primes: list[int], concat_map: list[int]) -> bool:
    base_set = set(concat_map[primes[0]])
    for next_prime in primes[1:]:
        base_set &= set(concat_map[next_prime])
        if base_set == {}:
            return False
    return True

if __name__ == '__main__':
    print(p60(4, 1000, 1000000))
    #print(p60(5, 10000, 1000000))
