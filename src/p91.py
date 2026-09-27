from collections import deque
from math import gcd


def p91(max_size: int) -> int:
    triangle_count = 0
    queue: deque[tuple[int, int]] = deque()
    all_points = ((x, y) for x in range(max_size+1) for y in range(max_size+1))
    queue.extend(all_points)

    # the first point, (0, 0), is special and we can calculate triangles on it
    queue.popleft()
    triangle_count += max_size * max_size

    # now, put the riht angle at every other lattice point
    while len(queue) > 0:
        x, y = queue.popleft()
        scaling = gcd(x, y)
        dx = -y // scaling
        dy = x // scaling

        # step in one direction
        test_x = x + dx
        test_y = y + dy
        while 0 <= test_x <= max_size and 0 <= test_y <= max_size:
            triangle_count += 1
            test_x += dx
            test_y += dy

        # step in the other
        test_x = x - dx
        test_y = y - dy
        while 0 <= test_x <= max_size and 0 <= test_y <= max_size:
                triangle_count += 1
                test_x -= dx
                test_y -= dy
        
    return triangle_count

if __name__ == '__main__':
    print(p91(2))
    print(p91(3))
    print(p91(50))
