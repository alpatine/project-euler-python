def fibonacci(upper):
    a, b = 1, 2
    while a < upper:
        yield a
        a, b = b, a+b
