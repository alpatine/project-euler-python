from number_theory import prime_ceil_to, primes

def p50(stop: int) -> int:
    prime_list = list(primes(stop))
    next_prime_map = prime_ceil_to(stop)
    prime_list_len = len(prime_list)
    for sum_len in range(546, 0, -1):
        if sum_len == 6:
            pass
        for start_index in range(0, prime_list_len - sum_len + 1):
            primes_to_sum = prime_list[start_index:start_index + sum_len]
            sum_of_primes = sum(primes_to_sum)
            if sum_of_primes < stop and sum_of_primes == next_prime_map[sum_of_primes]:
                return sum_of_primes

if __name__ == '__main__':
    print(p50(101))
    print(p50(1001))
    print(p50(1000001))