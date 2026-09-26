from writing import RomanNumerals

DATA_FILE_PATH = './data/p0089_roman.txt'

def p89(input: list[str]) -> int:
    rn = RomanNumerals()

    total_input_chars = sum(map(len, input))
    total_output_chars = 0

    for line in input:
        rn.set_str(line)
        total_output_chars += len(rn.shortest_str())

    return total_input_chars - total_output_chars

def load_data(path: str) -> list[str]:
    with open(path) as file:
        output = [line.strip() for line in file.readlines()]
        return output
    
if __name__ == '__main__':
    print(p89(['XIIIIII']))

    problem_data = load_data(DATA_FILE_PATH)
    print(p89(problem_data))
