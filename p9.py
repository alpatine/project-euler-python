from typing import Tuple
from queue import SimpleQueue
from math import prod
from pythagoras import calculate_next_triplets

def p9(target_sum: int) -> Tuple[int, int, int]:
    initial_triplet = (3, 4, 5)
    q = SimpleQueue()
    q.put(initial_triplet)

    while not q.empty():
        triplet = q.get()
        triplet_sum = sum(triplet)
        quotient, remainder = divmod(target_sum, triplet_sum)
        if remainder == 0: return prod(triplet) * quotient ** 3
        elif triplet_sum < target_sum:
            a, b, c = calculate_next_triplets(triplet)
            q.put(a)
            q.put(b)
            q.put(c)

if __name__ == '__main__':
    print(p9(12))
    print(p9(1000))