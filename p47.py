from number_theory import prime_factor_count_to, prime_factors

def p47(number_of_factors: int, stop: int) -> int:
    prime_factor_counts = prime_factor_count_to(stop)
    consecutive_target_count = 0
    first_found = 0
    for trial_number in range(1, stop):
        if prime_factor_counts[trial_number] == number_of_factors:
            consecutive_target_count += 1
            if consecutive_target_count == 1:
                first_found = trial_number
            if consecutive_target_count == number_of_factors:
                return first_found
        else:
            consecutive_target_count = 0

if __name__ == '__main__':
    print(p47(1, 11))
    print(p47(2, 21))
    print(p47(3, 701))
    print(p47(4, 140001))
