from number_theory import partitions


def p78(desired_factor: int, search_stop: int) -> int:
    for number in range(search_stop):
        partition_count = partitions(number)
        if partition_count % desired_factor == 0:
            return number

if __name__ == '__main__':
    print(p78(7, 11))
    print(p78(1000000, 100000))
