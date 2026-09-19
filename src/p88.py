from number_theory import divisors_to

type DivisorLists = dict[int, list[int]]

def factorise(n: int, max_factor: int, divisor_lists: DivisorLists) -> list[list[int]]:
    if n == 1:
        return [[]]

    result = []
    for factor in reversed(divisor_lists[n]):
        if factor > max_factor or factor == 1:
            continue

        factorisation = [factor]
        next_n = n // factor
        for sub_factorisation in factorise(next_n, factor, divisor_lists):
            result.append(factorisation + sub_factorisation)

    return result

def p88(max_set_size: int) -> int:
    max_number = max_set_size * 2
    divisor_lists = divisors_to(max_number+1)

    product_sum_sets: dict[int, int] = {}

    for number in range(2, max_number + 1):
        for factorisation in factorise(number, number-1, divisor_lists):
            factor_sum = sum(factorisation)
            set_size = len(factorisation) + number - factor_sum
            if set_size > max_set_size:
                continue
            if set_size not in product_sum_sets:
                product_sum_sets[set_size] = number

    result = sum(set(product_sum_sets.values()))

    return result
    
if __name__ == '__main__':
    print(p88(6))
    print(p88(12))
    print(p88(12000))
