from collections import defaultdict

from pythagoras import calculate_next_triplets


class ScaledTriple:
    def __init__(self: ScaledTriple,
                 primitive_a: int,
                 primitive_b: int,
                 primitive_c: int,
                 scale: int = 1):
        self.a = primitive_a * scale
        self.b = primitive_b * scale
        self.c = primitive_c * scale
        self.scale = scale
        self.primitive_a = primitive_a
        self.primitive_b = primitive_b
        self.primitive_c = primitive_c
        self.visited = False

    def next_triples(self: ScaledTriple) -> list[ScaledTriple]:
        result = []
        if self.scale == 1:
            t1, t2, t3 = calculate_next_triplets((self.a, self.b, self.c))
            result.append(ScaledTriple(*t1))
            result.append(ScaledTriple(*t2))
            result.append(ScaledTriple(*t3))
        
        result.append(ScaledTriple(
            self.primitive_a,
            self.primitive_b,
            self.primitive_c,
            self.scale + 1
            ))
        
        return result

    def __lt__(self: ScaledTriple, other: ScaledTriple):
        return (self.a, self.b) < (other.a, other.b)

    def __repr__(self):
        return f'({self.a},{self.b},{self.c})=({self.primitive_a},{self.primitive_b},{self.primitive_c})x{self.scale}'


def generate_cuboids(whole_side: int, split_side: int) -> set[frozenset[int]]:
    result = set()

    # We depend on the whole_side being the longest side of the cuboid
    if split_side > 2*whole_side:
        return result

    for split in range(1, split_side):
        cosplit = split_side - split
        if split > whole_side or cosplit > whole_side: continue
        cuboid = frozenset([whole_side, split, cosplit])
        result.add(cuboid)

    return result

def p86(target_num_cuboids: int) -> int:
    waiting: defaultdict[int, list[ScaledTriple]] = defaultdict(list)
    waiting[3].append(ScaledTriple(3, 4, 5))
    waiting[4].append(ScaledTriple(4, 3, 5))
    current_size = 0
    cuboids: set[frozenset[int]] = set()

    while True:
        triples = waiting[current_size]
        if len(triples) > 0:
            # count cuboids by splitting the longer side
            for t in triples:
                cuboids |= generate_cuboids(t.a, t.b)

            # check finish
            if len(cuboids) >= target_num_cuboids:
                return current_size

            # create waiting triples
            for t in triples:
                for next_t in t.next_triples():
                    waiting[next_t.a].append(next_t)

        del waiting[current_size]
        current_size += 1

if __name__ == '__main__':
    print(p86(2000))
    print(p86(1000000))
