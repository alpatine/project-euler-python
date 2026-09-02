from queue import PriorityQueue
from typing import NamedTuple

DATA_FILE_PATH = './data/p0082_matrix.txt'

class Position(NamedTuple):
    row: int
    col: int

class Front(NamedTuple):
    distance: int
    position: Position

type Grid = list[list[int]]

def find_path(matrix: Grid, start: Position) -> int:
    """Finds the shortest path from the start node to any node in the
     right column"""
    height = len(matrix)
    width = len(matrix[0])

    max_path_length = sum(col for row in matrix for col in row)
    shortest_path = max_path_length
    distances: Grid = [[max_path_length for col in row] for row in matrix]
    distances[start.row][start.col] = matrix[start.row][start.col]

    frontier: PriorityQueue[Front] = PriorityQueue()
    frontier.put_nowait(Front(matrix[start.row][start.col], start))
    visited: set[Position] = set()

    # Explore
    while not frontier.empty():
        distance, position = frontier.get_nowait()
        if distance > shortest_path: break
        visited.add(position)

        for delta in [(0, 1), (-1, 0), (1, 0)]:
            next_position = Position(
                position.row + delta[0],
                position.col + delta[1])
            if next_position in visited: continue
            if next_position.row < 0 or next_position.row > height - 1: continue
            if next_position.col < 0 or next_position.col > width - 1: continue

            target_value = matrix[next_position.row][next_position.col]
            trial_distance = distance + target_value
            target_distance = distances[next_position.row][next_position.col]

            if trial_distance < target_distance:
                distances[next_position.row][next_position.col] = trial_distance
                if next_position.col == width - 1:
                    shortest_path = min(shortest_path, trial_distance)
                else:
                    frontier.put_nowait(Front(trial_distance, next_position))

    # Find the smallest value in the right column
    return min(distances[row][-1] for row in range(height))

def p82(matrix: Grid) -> int:

    shortest_path = sum(col for row in matrix for col in row)
    for row in range(len(matrix)):
        shortest_path = min(shortest_path, find_path(matrix, Position(row, 0)))

    return shortest_path

def load_data(path: str) -> list[list[int]]:
    with open(path) as file:
        matrix = [[int(value) for value in line.split(',')] for line in file]
        return matrix

if __name__ == '__main__':
    example_matrix = [
        [ 131, 673, 234, 103, 18 ],
        [ 201, 96, 342, 965, 150 ],
        [ 630, 803, 746, 422, 111 ],
        [ 537, 699, 497, 121, 956 ],
        [ 805, 732, 524, 37, 331 ],
    ]
    print(p82(example_matrix))

    matrix = load_data(DATA_FILE_PATH)
    print(p82(matrix))
