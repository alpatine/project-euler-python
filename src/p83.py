from queue import PriorityQueue
from typing import NamedTuple

DATA_FILE_PATH = './data/p0083_matrix.txt'

class Position(NamedTuple):
    row: int
    col: int

class Front(NamedTuple):
    distance: int
    position: Position

type Grid = list[list[int]]

def p83(matrix: Grid) -> int:
    height = len(matrix)
    width = len(matrix[0])
    start_position = Position(0, 0)
    end_position = Position(height - 1, width - 1)

    max_path_length = sum(col for row in matrix for col in row)
    distances: Grid = [[max_path_length for col in row] for row in matrix]
    distances[start_position.row][start_position.col] = matrix[start_position.row][start_position.col]

    frontier: PriorityQueue[Front] = PriorityQueue()
    frontier.put_nowait(Front(matrix[start_position.row][start_position.col], start_position))
    visited: set[Position] = set()

    # Explore
    while not frontier.empty():
        distance, position = frontier.get_nowait()
        visited.add(position)

        for delta in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
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
                if next_position == end_position:
                    return trial_distance
                else:
                    frontier.put_nowait(Front(trial_distance, next_position))

    # Find the smallest value in the right column
    return min(distances[row][-1] for row in range(height))

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
    print(p83(example_matrix))

    matrix = load_data(DATA_FILE_PATH)
    print(p83(matrix))
