from collections import Counter

SQUARES: list[str] = [
    'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
    'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
    'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
    'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
]
NUM_SQUARES = len(SQUARES)

SQUARE = {name: index for index, name in enumerate(SQUARES)}

type RollProbability = tuple[int, float]
type PositionProbability = tuple[int, float]
type Vector = list[float]
type Matrix = list[list[float]]

def calculate_roll_probabilities(dice_size: int) -> list[RollProbability]:
    # assumes 2 dice
    outcomes = [a+b+2 for a in range(dice_size) for b in range(dice_size)]
    num_outcomes = len(outcomes)
    outcome_counts = Counter(outcomes)
    probabilities = [(outcome, count / num_outcomes) for outcome, count in outcome_counts.items()]
    return probabilities

def find_next(start_char: str, start_square: str) -> int:
    for pos in range(start_square + 1, start_square + 41):
        if SQUARES[pos % NUM_SQUARES].startswith(start_char):
            return pos % NUM_SQUARES

def resolve_square(square: int) -> list[PositionProbability]:
    running_probability_sum = [0.] * NUM_SQUARES

    if SQUARES[square].startswith('CC'):
        running_probability_sum[SQUARE['GO']] += 1./16.
        running_probability_sum[SQUARE['JAIL']] += 1./16.
        running_probability_sum[square] += 14./16.
    elif SQUARES[square].startswith('CH'):
        running_probability_sum[SQUARE['GO']] += 1./16.
        running_probability_sum[SQUARE['JAIL']] += 1./16.
        running_probability_sum[SQUARE['C1']] += 1./16.
        running_probability_sum[SQUARE['E3']] += 1./16.
        running_probability_sum[SQUARE['H2']] += 1./16.
        running_probability_sum[SQUARE['R1']] += 1./16.
        running_probability_sum[find_next('R', square)] += 2./16.
        running_probability_sum[find_next('U', square)] += 1./16.

        for pos, pos_prob in resolve_square((square + NUM_SQUARES - 3) % NUM_SQUARES):
            running_probability_sum[pos] += pos_prob * 1./16.

        running_probability_sum[square] += 6./16.
    elif SQUARES[square] == 'G2J':
        running_probability_sum[SQUARE['JAIL']] = 1.
    else:
        running_probability_sum[square] = 1.

    return [(pos, prob) for pos, prob in enumerate(running_probability_sum)]

def calculate_transition_matrix(rolls: list[RollProbability]) -> Matrix:
    # Build a map from initial landing square to final square at end of move.
    landing_final_map = [resolve_square(landing) for landing in range(NUM_SQUARES)]

    dice_size = (len(rolls) + 1) // 2
    doubles_prob = 1. / (dice_size * dice_size)

    # Create a right/row markov transition matrix
    # 'From' will be rows, 'To' will be the columns
    matrix: Matrix = []
    for start_pos in range(NUM_SQUARES):
        end_pos_probs = [0] * NUM_SQUARES
        for roll, roll_prob in rolls:
            next_pos_probs = landing_final_map[(start_pos + roll) % NUM_SQUARES]

            # Need to consider doubles now
            jail_prob = ((roll + 1) % 2) * doubles_prob * doubles_prob
            safe_prob = roll_prob - jail_prob

            end_pos_probs[SQUARE['JAIL']] += jail_prob
            for pos, pos_pob in next_pos_probs:
                end_pos_probs[pos] += safe_prob * pos_pob

        matrix.append(end_pos_probs)

    return matrix

def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    # Assumes square matrix
    size = len(left)

    result = [[0. for _ in range(size)] for _ in range(size)]

    for left_row in range(size):
        for right_col in range(size):
            for step in range(size):
                result[left_row][right_col] += left[left_row][step] * right[step][right_col]
                
    return result

def exponentiate_matrix(matrix: Matrix, exponent: int) -> Matrix:
    result = matrix
    for _ in range(exponent):
        result = matrix_mul(result, matrix)
    return result

def p84(dice_size: int) -> str:
    # calculate all possible roll probabilities
    roll_probabilities = calculate_roll_probabilities(dice_size)

    # calculate transition matrix
    transition_matrix = calculate_transition_matrix(roll_probabilities)

    # exponentiate transition matrix
    transition_matrix = exponentiate_matrix(transition_matrix, 200)

    # extract stationary probability vector and associate with squares
    stationary_vector = transition_matrix[0]

    # sort and extract required code
    square_probs = list((prob, pos) for pos, prob in enumerate(stationary_vector))
    square_probs.sort(reverse=True)

    return f'{square_probs[0][1]:02}{square_probs[1][1]:02}{square_probs[2][1]:02}'

if __name__ == '__main__':
    print(p84(6))
    print(p84(4))
