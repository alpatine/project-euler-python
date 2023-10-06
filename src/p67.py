from json import load

from p18 import p18


def p67(path: str) -> int:
    triangle = load_triangle(path)
    return p18(triangle)
    
def load_triangle(path: str) -> list[list[int]]:
    with open(path) as triangle_file:
        return [list(map(int, line.split())) for line in triangle_file]

if __name__ == '__main__':
    print(p67('./data/p067_triangle_given.txt'))
    print(p67('./data/p067_triangle.txt'))
