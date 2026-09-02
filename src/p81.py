DATA_FILE_PATH = './data/p0081_matrix.txt'

def p81(matrix: list[list[int]]) -> int:
    height = len(matrix)
    width = len(matrix[0])

    for col in range(width-1, -1, -1):
        for row in range(height-1, -1, -1):
            options = []
            cell_value = matrix[row][col]
            if col < width - 1:
                options.append(cell_value + matrix[row][col+1])
            if row < height - 1:
                options.append(cell_value + matrix[row+1][col])
            if len(options) > 0:
                matrix[row][col] = min(options)

    return matrix[0][0]

def load_data(path: str) -> list[list[int]]:
    with open(path) as file:
        matrix = [[int(value) for value in line.split(',')] for line in file]
        return matrix

if __name__ == '__main__':
    matrix = load_data(DATA_FILE_PATH)
    print(p81(matrix))
