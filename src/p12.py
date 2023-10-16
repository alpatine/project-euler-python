from number_theory import count_divisors, primes

def p12(divisor_target: int) -> int:
    prime_number_list = list(primes(1000))
    for n in range (1, 2 ** 30):
        triangle_number = n * (n + 1) // 2
        number_of_divisors = count_divisors(triangle_number, prime_number_list)
        if number_of_divisors >= divisor_target:
            return triangle_number

if __name__ == '__main__':
    print(p12(5))
    print(p12(500))