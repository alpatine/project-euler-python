from farey import farey_sequence_length


def p72(n: int) -> int:
    return farey_sequence_length(n) - 2

if __name__ == '__main__':
    print(p72(8))
    print(p72(1000000))
