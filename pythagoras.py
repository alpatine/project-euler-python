from typing import Tuple

def calculate_next_triplets(triplet: Tuple[int, int, int]) -> Tuple[Tuple[int, int, int],
                                                                  Tuple[int, int, int],
                                                                  Tuple[int, int, int]]:
    a, b, c = triplet
    A = (a - 2 * b + 2 * c,
         2 * a - b + 2 * c,
         2 * a - 2 * b + 3 * c)
    
    B = (a + 2 * b + 2 * c,
         2 * a + b + 2 * c,
         2 * a + 2 * b + 3 * c)

    C = (-a + 2 * b + 2 * c,
         -2 * a + b + 2 * c,
         -2 * a + 2 * b + 3 * c)

    return (A, B, C)