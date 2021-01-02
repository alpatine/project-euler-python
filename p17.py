from number_words import number_to_words

def p17(stop: int) -> int:
    return sum([len(number_to_words(n)) for n in range (1, stop)])

if __name__ == '__main__':
    print(p17(6))
    print(p17(1001))