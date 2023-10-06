from number_theory import divisor_sums_to

def p23(stop: int) -> int:
    divisor_sums = divisor_sums_to(stop)

    abundant_numbers = [number for number, divisor_sum in divisor_sums.items() if divisor_sum > number]
    abundant_number_count = len(abundant_numbers)

    # all numbers >= 28124 are sums of two abundant numbers
    max_sum = min(stop, 28124)

    is_sum = [False] * max_sum

    for lower_index in range(0, abundant_number_count):
        for higher_index in range(lower_index, abundant_number_count):
            current_sum = abundant_numbers[lower_index] + abundant_numbers[higher_index]
            if current_sum < max_sum:
                is_sum[current_sum] = True
            else: break
            
    not_sums = [number for number, sum_flag in enumerate(is_sum) if sum_flag == False]

    return sum(not_sums)

if __name__ == '__main__':
    print(p23(28124))
