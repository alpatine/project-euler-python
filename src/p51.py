from collections import Counter
from itertools import combinations, dropwhile
from number_theory import primes

def p51(stop: int) -> int:
    prime_dict = {n: True for n in dropwhile(lambda x: x < 1000, primes(stop))}
    for prime in prime_dict:
        prime_str = str(prime)
        for most_common_number, most_common_count in Counter(prime_str).most_common():
            if most_common_count < 3:
                break
            
            # Find the positions of the repeating digits
            positions = []
            for index in range(0, len(prime_str)):
                if prime_str[index] == most_common_number:
                    positions.append(index)
            
            # replace the repeating digits in groups of three
            for position_combo in combinations(positions, 3):
                if position_combo[-1] == len(prime_str) - 1:
                    # Replacing the final digit will yield too many even numbers
                    # so try another combination
                    continue
                candidate_prime_chars = list(prime_str)
                family_count = 0
                for replace_value in '0123456789':
                    for replace_position in position_combo:
                        candidate_prime_chars[replace_position] = replace_value
                    candidate_prime = int("".join(candidate_prime_chars))
                    if prime_dict.get(candidate_prime, False):
                        family_count += 1
                if family_count >= 8:
                    return prime

if __name__ == '__main__':
    print(p51(1000000))
