from pythagoras import calculate_next_triplets
from queue import SimpleQueue

def p39(triplet_sum_stop: int) -> int:
    initial_triplet = (3, 4, 5)
    q = SimpleQueue()
    q.put(initial_triplet)

    triplet_sum_counts = [0] * triplet_sum_stop
    
    while not q.empty():
        triplet = q.get()
        triplet_sum = sum(triplet)
        if triplet_sum < triplet_sum_stop:
            for triplet_sum_multiple in range(triplet_sum, triplet_sum_stop, triplet_sum):
                triplet_sum_counts[triplet_sum_multiple] += 1
            a, b, c = calculate_next_triplets(triplet)
            q.put(a)
            q.put(b)
            q.put(c)
    
    largest_triplet_sum = 0
    largest_triplet_sum_count = 0
    for triplet_sum in range(12, triplet_sum_stop):
        triplet_sum_count = triplet_sum_counts[triplet_sum]
        if triplet_sum_count > largest_triplet_sum_count:
            largest_triplet_sum_count = triplet_sum_count
            largest_triplet_sum = triplet_sum
    
    return largest_triplet_sum

if __name__ == '__main__':
    print(p39(121))
    print(p39(1001))
