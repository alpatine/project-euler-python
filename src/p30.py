def p30(power: int) -> int:
    # can these bounds be tightened?
    search_start = 10

    # We can stop looking when the maximum achievable sum has fewer
    # digits than the number of digits raised and summed...
    # The maximim achievable raised sum of n digits occurs when all n digits
    # are the number 9 and equals: n * (9 ** power)
    # It needs to be larger than the smallest number with n
    # digits, which is 1 followed by n-1 digits, which equals 10 ** (n - 1)

    n = 2
    min_number_with_n_digits = 10
    max_achievable_sum = 2 * (9 ** power)
    while (max_achievable_sum >= min_number_with_n_digits):
        n += 1
        max_achievable_sum = n * (9 ** power)
        min_number_with_n_digits = 10 ** (n - 1)

    # n stops at the first value that won't work, so it is too big by 1
    search_end = (n - 1) * (9 ** power)
    
    result_sum = 0
    for number in range(search_start, search_end):
        digits_raised = [int(digit) ** power for digit in str(number)]
        digits_raised_sum = sum(digits_raised)
        if digits_raised_sum == number:
            result_sum += number
    
    return result_sum

if __name__ == '__main__':
    print('4:', p30(4))
    print('5:', p30(5))