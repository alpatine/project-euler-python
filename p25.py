from fibonacci import largest_fib_index_with_n_digits

def p25(fib_number_len) -> int:
    return largest_fib_index_with_n_digits(fib_number_len-1) + 1

if __name__ == '__main__':
    print(p25(2))
    print(p25(3))
    print(p25(1000))
