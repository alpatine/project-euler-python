from number_theory import is_palindrome
def p36(stop: int) -> int:

    # Rather than test every number we'll build the palindrome
    # numbers in base 10. We'll need the first half of the digits in
    # the maximum value. If the length of the max is odd then we need
    # to collect the middle digit as well.
    # Cases: max value -> first half
    # Case 1: 1 -> 1
    # Case 2: 12 -> 1
    # Case 3: 123 -> 12
    # Case 4: 1234 -> 12 etc.
    max_n = stop - 1
    max_n_str = str(max_n)
    max_n_len = len(max_n_str)
    first_half_max_n_digits_len = max_n_len // 2 + max_n_len % 2
    first_half_max_n_digits = max_n_str[:first_half_max_n_digits_len]

    palindromes = [n for n in range(1, min(10, stop))]

    # generate list of candidate palindromes
    for generating_digits in range(0, int(first_half_max_n_digits) + 1):
        generating_digits_str = str(generating_digits)

        # determine left and right most digits
        left_digits = generating_digits_str
        right_digits = left_digits[::-1]
        
        # even length palindromes (len: 2x)
        even_palindrome = int(left_digits + right_digits)
        if even_palindrome >= stop: break 
        palindromes.append(even_palindrome)

        # odd length palindromes (len: 2x + 1)
        for middle_digit in range(0, 10):
            odd_palindrome = int(left_digits + str(middle_digit) + right_digits)
            if odd_palindrome >= stop: break
            palindromes.append(odd_palindrome)

    # now sum those that are also palindromes in base 2
    return sum(n for n in palindromes if is_palindrome(bin(n)[2:]))

if __name__ == '__main__':
    print(p36(30))
    print(p36(1000000))
