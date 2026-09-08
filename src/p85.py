from math import ceil, floor


def p85(target: int) -> int:
    min_dist = target
    best_width = None
    best_height = None

    max_width = floor((4 * target) ** (1./4.))
    for width in range(1, max_width + 1):
        min_height = floor(-0.5 + ((16 * target + width * (width + 1)) / (4 * width * (width + 1))) ** 0.5)
        max_height = ceil(-0.5 + ((16 * target + width * (width + 1)) / (4 * width * (width + 1))) ** 0.5)
        for height in range(min_height, max_height + 1):
            rectangles = width * (width + 1) * height * (height + 1) // 4
            dist = abs(target - rectangles)
            if dist < min_dist:
                min_dist = dist
                best_width = width
                best_height = height

    return best_width * best_height

if __name__ == '__main__':
    print(p85(11))
    print(p85(2000000))
