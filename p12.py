from number_theory import count_divisors, primes

def p12(divisor_target: int) -> int:
    prime_number_list = list(primes(1000))
    previous_factor_divisors = 1
    for n in range (1, 2 ** 30):
        current_factor = n + 1
        if current_factor % 2 == 0:
            current_factor //= 2
        
        current_factor_divisors = count_divisors(current_factor, prime_number_list)
        divisor_count = previous_factor_divisors * current_factor_divisors
        if divisor_count >= divisor_target:
            return n * (n + 1) // 2

        previous_factor_divisors = current_factor_divisors

if __name__ == '__main__':
    print(p12(5))
    print(p12(500))