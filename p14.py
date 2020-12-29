from collatz import collatz_length

def p14(stop: int) -> int:
    number_with_max_collatz_length = 0
    max_collatz_length = 0
    if stop == 1: return 1
    for n in range(stop//2, stop):
        length = collatz_length(n)
        if length > max_collatz_length:
            max_collatz_length = length
            number_with_max_collatz_length = n
    
    return number_with_max_collatz_length
            
if __name__ == '__main__':
    print(p14(16))
    print(p14(1000000))