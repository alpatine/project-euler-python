def p1(upper: int) -> int:
    return sum(x for x in range(upper) if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
    print(p1(10))
    print(p1(1000))
