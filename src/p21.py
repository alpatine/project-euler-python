from number_theory import divisor_sums_to

def p21(number: int) -> int:
    divisor_sums = divisor_sums_to(number)
    amicable_sum = 0
    for a in range(1, number):
        b = divisor_sums[a]
        if a == b or b >= number: continue
        b_sum = divisor_sums[b]
        if b_sum >= number: continue
        if a == b_sum: amicable_sum += a
    return amicable_sum

if __name__ == '__main__':
    print(p21(301))
    print(p21(10000))
