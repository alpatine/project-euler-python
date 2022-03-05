def p48(stop: int) -> int:
    # brute force
    return sum(n**n for n in range(1, stop)) % 10000000000

if __name__ == '__main__':
    print(p48(11))
    print(p48(1001))
