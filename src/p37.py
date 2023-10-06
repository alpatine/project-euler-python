from number_theory import is_prime, primes

def p37():
    prime_numbers = list(primes(740000))
    truncatable_prime_list = []
    for prime in prime_numbers:
        if prime < 10: continue
        prime_str = str(prime)
        if prime_str[-1] not in ('3', '7'): continue
        if prime_str[0] not in ('2', '3', '5', '7'): continue

        right_truncatable_prime = False
        right_truncated_str = prime_str[:-1]
        while len(right_truncated_str) > 0:
            right_truncated = int(right_truncated_str)
            if is_prime(right_truncated, prime_numbers) == False: break
            right_truncated_str = right_truncated_str[:-1]
        else: right_truncatable_prime = True
        if right_truncatable_prime == False: continue

        left_truncatable_prime = False
        left_truncated_str = prime_str[1:]
        while len(left_truncated_str) > 0:
            left_trucated = int(left_truncated_str)
            if is_prime(left_trucated, prime_numbers) == False: break
            left_truncated_str = left_truncated_str[1:]
        else: left_truncatable_prime = True

        if left_truncatable_prime and right_truncatable_prime:
            truncatable_prime_list.append(prime)
    
    return sum(truncatable_prime_list)

if __name__ == '__main__':
    print(p37())
