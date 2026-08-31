from collections import Counter, defaultdict
from functools import cmp_to_key
from itertools import combinations


def p79(attempts_file_path: list[str]) -> str:
    with open(attempts_file_path) as attempts_file:
        attempts = [line.strip() for line in attempts_file]

    ordering = defaultdict(set)
    digit_counter = Counter()

    for attempt in attempts:
        digit_counter.update(attempt)
        for first, second in combinations(attempt, 2):
            ordering[first].add(second)
    used_digits = list(digit_counter)

    def cmp_func(a: str, b: str) -> int:
        if b in ordering[a]: return -1
        elif a in ordering[b]: return 1
        else: return 0
    
    used_digits.sort(key=cmp_to_key(cmp_func))
    passcode = ''.join(used_digits)
    return passcode    

if __name__ == '__main__':
    print(p79('./data/p0079_keylog.txt'))
