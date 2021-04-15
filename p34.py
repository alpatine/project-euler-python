from number_theory import digit_factorial_sum

def p34():
    result_sum = 0
    for n in range(3, 50000):
        if n == digit_factorial_sum(n):
            result_sum += n
    
    return result_sum

if __name__ == '__main__':
    print(p34())
