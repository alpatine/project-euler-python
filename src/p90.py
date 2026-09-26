from itertools import combinations


def p90() -> int:
    digits = list(range(10))
    squares = [n*n for n in range(1, 10)]
    valid_arrangements = set()

    for dice1 in combinations(digits, 6):
        for dice2 in combinations(digits, 6):
            reachable = set()
            for dice1_digit in dice1:
                for dice2_digit in dice2:
                    if dice1_digit in {6, 9}:
                        reachable.add(60 + dice2_digit)
                        reachable.add(90 + dice2_digit)
                        reachable.add(10 * dice2_digit + 6)
                        reachable.add(10 * dice2_digit + 9)
                    if dice2_digit in {6, 9}:
                        reachable.add(60 + dice1_digit)
                        reachable.add(90 + dice1_digit)
                        reachable.add(10 * dice1_digit + 6)
                        reachable.add(10 * dice1_digit + 9)
                    reachable.add(10 * dice1_digit + dice2_digit)
                    reachable.add(10 * dice2_digit + dice1_digit)
            for square in squares:
                if square not in reachable: break
            else:
                valid_arrangements.add(frozenset({frozenset(dice1),
                                                  frozenset(dice2)}))

    return len(valid_arrangements)

if __name__ == '__main__':
    print(p90())