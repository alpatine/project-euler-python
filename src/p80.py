from decimal import Context, Decimal


def p80(start: int, stop: int) -> int:
    context = Context(prec=110)

    running_sum = 0
    for n in range(start, stop):
        number_str = str(Decimal(n, context).sqrt(context)).replace('.', '')
        if len(number_str) <= stop: continue
        running_sum += sum(map(int, number_str[:100]))

    return running_sum

if __name__ == '__main__':
    print(p80(2, 3))
    print(p80(1, 101))
