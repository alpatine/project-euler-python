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
    result = set()
    current_factor = 2
    while number > 1:
        dividend, remainder = divmod(number, current_factor)
        if remainder == 0:
            number = dividend
            result.add(current_factor)
            current_factor = current_factor - 1
        current_factor = current_factor + 1
    return result