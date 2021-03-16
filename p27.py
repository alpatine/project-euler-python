from number_theory import isPrime, primes
def p27(a_start: int, a_stop: int, b_start: int, b_stop: int) -> int:
    # b needs to be prime to get a prime when n == 0, so b >= 2
    b_start = max(b_start, 2)

    # when n == b then all terms are a multiple of b, so this is the
    # limit of what needs to be searched
    largest_output = (b_stop - 1) * ((b_stop - 1) + (a_stop - 1) + 1)
    prime_factors = list(primes(largest_output))

    # calcuate offset for start of a: a must be odd, unless b == 2
    a_start_even = a_start % 2 == 0

    (max_a, max_b, max_n) = (0, 0, 0)

    for b in prime_factors:
        if b < b_start: continue
        if b >= b_stop: break
        
        if a_start_even != (b == 2):
            a_start_offset = 1
        else:
            a_start_offset = 0 
        
        for a in range(a_start + a_start_offset, a_stop, 2):
            for n in range(0, b):
                quadratic_value = n * n + a * n + b
                if quadratic_value < 0: break
                if not isPrime(quadratic_value, prime_factors): break
            if n > max_n:
                (max_a, max_b, max_n) = (a, b, n)
    
    return max_a * max_b

if __name__ == '__main__':
    print(p27(-999, 1000, -1000, 1001))

