from math import comb

def p15(grid_size: int) -> int:
    return comb(2 * grid_size, grid_size)

if __name__ == '__main__':
    print(p15(2))
    print(p15(20))