def p4(digits: int) -> int:
    start, stop = 10 ** digits - 1, 10 ** (digits - 1) - 1
    max_palindrome = 0
    for a in range(start, stop, -1):
        for b in range(a, stop, -1):
            product = a * b
            if product < max_palindrome: break
            if str(product) == str(product)[::-1]:
                if product > max_palindrome:
                    max_palindrome = product
    
    return max_palindrome

if __name__ == "__main__":
    print(p4(2))
    print(p4(3))
    