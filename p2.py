from fibonacci import fibonacci

def p2(upper):
    return sum(x for x in fibonacci(upper) if x % 2 == 0)

if __name__ == '__main__':
    print(p2(90))
    print(p2(4000001))
