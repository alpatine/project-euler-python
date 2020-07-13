from math import sqrt, floor

def primes(upper):
    prime_list = [True] * upper
    max_factor = floor(sqrt(upper))

    for i in range(2, upper):
        if prime_list[i] == True:
            yield i
            if i <= max_factor:
                for j in range(i*i, upper, i):
                    prime_list[j] = False

def prime_factors(number):
    return (x for x in primes(number+1) if number % x == 0)
