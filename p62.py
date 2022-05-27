from collections import Counter

class Hashable_Counter(Counter):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

def p62(count_required: int) -> int:
    counters = {}
    for base in range(1, 10000):
        cube_str = str(base ** 3)
        cube_digits_count = Hashable_Counter(cube_str)
        counter_numbers = counters.setdefault(cube_digits_count, [])
        counter_numbers.append(cube_str)
        if len(counter_numbers) == count_required:
            return int(counter_numbers[0])

if __name__ == '__main__':
    print(p62(3))
    print(p62(5))
