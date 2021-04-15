from number_theory import is_prime, primes

def p35(stop: int) -> int:
    circular_primes = set()
    primes_to_check = list(primes(stop))
    for prime in primes_to_check:
        prime_str = str(prime)
        
        prime_len = len(prime_str)
        rotated_str = prime_str
        rotations = [rotated_str]
        prime_rotations = 1
        for rotation_number in range(prime_len - 1):
            rotated_str = rotate(rotated_str)
            rotations.append(rotated_str)
            if is_prime(int(rotated_str), primes_to_check):
                prime_rotations += 1
            else:
                break
        
        if prime_rotations == prime_len:
            # all rotations are prime
            circular_primes.update(rotations)
    
    print(circular_primes)
    return len(circular_primes)

def rotate(list_to_rotate: list) -> list:
    return list_to_rotate[1:] + list_to_rotate[:1]

if __name__ == '__main__':
    print(p35(100))
    print(p35(1000000))

