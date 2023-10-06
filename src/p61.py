from itertools import dropwhile
from typing import Iterator

from number_theory import (heptagonal_numbers_to, hexagonal_numbers_to,
                           octagonal_numbers_to, pentagonal_numbers_to,
                           square_numbers_to, triangle_numbers_to)


def p61() -> int:
    figurate_generators = [
        triangle_numbers_to,
        square_numbers_to,
        pentagonal_numbers_to,
        hexagonal_numbers_to,
        heptagonal_numbers_to,
        octagonal_numbers_to,
    ]

    under_1010 = lambda x: x < 1010
    figurate_numbers = []
    for generator in figurate_generators:
        figurate_numbers.append(
            bucket_numbers(dropwhile(under_1010, generator(10000))))

    for head, tail_list in figurate_numbers[0].items():
        for tail in tail_list:
            cycle = extend_cycle(head, tail, figurate_numbers, [0])
            if cycle is not None:
                cycle = [head + tail] + cycle
                return sum(map(int, cycle))

def bucket_numbers(source: Iterator[int]) -> dict[str, str]:
    output = {}
    for n_str in map(str, source):
        key = n_str[0:2]
        if key[0] == '0':
            continue
        value = n_str[2:4]
        if value[0] == '0':
            continue
        output.setdefault(key, []).append(value)
    return output

def extend_cycle(
        root: int,
        head: int,
        figurate_numbers: list[dict[str, str]],
        figures_included: list[int]) -> list[str]:
    not_enough_depth = len(figures_included) < len(figurate_numbers) - 1
    for figurate_numbers_index in range(0, len(figurate_numbers)):
        if figurate_numbers_index in figures_included:
            continue
            
        for tail in figurate_numbers[figurate_numbers_index].get(head, []):
            if not_enough_depth:
                # Not at required depth, keep going
                end_of_cycle = extend_cycle(
                    root,
                    tail,
                    figurate_numbers,
                    figures_included + [figurate_numbers_index],
                )
                if end_of_cycle is not None:
                    return [head + tail] + end_of_cycle
            else:
                # Can we close the cycle?
                if root == tail:
                    return [head + tail]

if __name__ == '__main__':
    print(p61())
