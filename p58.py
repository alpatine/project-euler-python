from number_theory import is_prime, primes

def p58(max_ratio: float) -> int:
    prime_list = list(primes(1000000))
    layer = 0
    ratio = 1
    prime_count = 0
    number_count = 1
    while ratio > max_ratio:
        layer += 1
        for corner_number in range(4):
            number = 2 * layer * (2 * (layer - 1) + corner_number + 1) + 1
            if is_prime(number, prime_list):
                prime_count += 1
        number_count += 4
        ratio = prime_count / number_count
    
    return 2 * layer + 1

if __name__ == '__main__':
    print(p58(0.5))
    print(p58(0.1))
