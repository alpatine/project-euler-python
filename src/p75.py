from queue import SimpleQueue

from pythagoras import calculate_next_triplets


def p75(triplet_sum_stop: int) -> int:
    initial_triplet = (3, 4, 5)
    q = SimpleQueue()
    q.put(initial_triplet)

    triplet_sum_counts = [0] * triplet_sum_stop

    while not q.empty():
        triplet = q.get()
        triplet_sum = sum(triplet)
        if triplet_sum < triplet_sum_stop:
            if triplet_sum == 12:
                pass
            for triplet_sum_multiple in range(triplet_sum,
                                              triplet_sum_stop,
                                              triplet_sum):
                triplet_sum_counts[triplet_sum_multiple] += 1
            a, b, c = calculate_next_triplets(triplet)
            q.put(a)
            q.put(b)
            q.put(c)

    equals_one = lambda x: x == 1
    count_of_ones = sum(map(equals_one, triplet_sum_counts))
    return count_of_ones

if __name__ == '__main__':
    print(p75(51))
    print(p75(1500001))
