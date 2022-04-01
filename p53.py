from math import comb

def p53(n_start: int, n_stop: int, threshold: int) -> int:
    elements_above_threshold = 0
    for n in range(n_start, n_stop):
        if n % 2 == 0:
            # even n
            if comb(n, n // 2) > threshold:
                elements_above_threshold += 1
            for k in range((n // 2) - 1, 0, -1):
                if comb(n, k) > threshold:
                    elements_above_threshold += 2
        else:
            # odd n
            for k in range(n // 2, 0, -1):
                if comb(n, k) > threshold:
                    elements_above_threshold += 2

    return elements_above_threshold

if __name__ == '__main__':
    print(p53(1, 6, 10))
    print(p53(1, 7, 10))
    print(p53(1, 8, 10))
    print(p53(1, 101, 1000000))
