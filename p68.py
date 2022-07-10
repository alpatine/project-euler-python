from collections import Counter
from itertools import permutations


def p68(sides: int, str_len: int) -> int:
    ngons = generate_ngons(sides)
    max_value = 0
    for ngon in ngons:
        ngon_str = calculate_ngon_str(ngon)
        if len(ngon_str) == str_len:
            ngon_int = int(ngon_str)
            if ngon_int > max_value:
                max_value = ngon_int
    return max_value

def generate_ngons(sides: int) -> list[list[int]]:
    positions = 2 * sides
    valid_ngons = []
    test_counter = Counter(range(1, positions+1))
    for a0 in range(1, positions - 1):
        #a0 is the first outer position
        outer_seed_pool = range(a0 + 1, positions + 1)
        outer_seed_count = sides - 2
        for outer_seeds in permutations(outer_seed_pool, outer_seed_count):
            # outer_seeds = first sides-1 outer values
            outer_seeds = (a0, *outer_seeds)
            inner_seeds_pool = [seed for seed in range(1, positions + 1)
                                     if seed not in outer_seeds]
            for inner_seeds in permutations(inner_seeds_pool, 2):
                # inner_seeds = first 2 inner values
                ngon = [0] * positions
                ngon[0:sides-1] = outer_seeds
                ngon[sides:sides+2] = inner_seeds
                line_total = ngon[0] + ngon[sides] + ngon[sides + 1]

                # calc the remaining inner positions
                for ngon_pos in range(sides + 2, positions):
                    ngon[ngon_pos] = (line_total
                                    - ngon[ngon_pos - 1]
                                    - ngon[ngon_pos - sides - 1])
                
                # calculate the last outer position
                ngon[sides - 1] = line_total - ngon[-1] - ngon[sides]
                
                # test compliance of ngon
                if ngon[sides - 1] > outer_seeds[0]:
                    number_counter = Counter(ngon)
                    if number_counter == test_counter:
                        valid_ngons.append(ngon)
                        #print(ngon)
    return valid_ngons

def calculate_ngon_str(ngon: list[int]) -> str:
    sides = len(ngon) // 2
    char_list = []
    for offset in range(0, sides):
        char_list.append(ngon[offset])
        char_list.append(ngon[sides + offset])
        char_list.append(ngon[sides + ((offset + 1) % sides)])
    result_str = ''.join(map(str, char_list))
    return result_str

if __name__ == '__main__':
    print(p68(3, 9))
    print(p68(5, 16))
