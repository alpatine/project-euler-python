def p22() -> int:
    # open the file
    with open('./data/p022_names.txt', 'r') as names_file:
        names_list = [name.strip('"') for name in names_file.read().split(',')]
    
    names_list.sort()

    letter_scores = {'A':  1, 'B':  2, 'C':  3, 'D':  4, 'E':  5, 'F':  6,
                     'G':  7, 'H':  8, 'I':  9, 'J': 10, 'K': 11, 'L': 12,
                     'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
                     'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
                     'Y': 25, 'Z': 26}

    file_score = 0
    for name_pos in range(0, len(names_list)):
        file_score +=  (name_pos + 1) * sum(letter_scores[letter] for letter in names_list[name_pos])
        
    return file_score

if __name__ == '__main__':
    print(p22())
