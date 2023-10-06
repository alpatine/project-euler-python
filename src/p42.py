from number_theory import is_triangle_number
from number_words import word_score


def p42() -> int:
    with open('./data/p042_words.txt') as file:
        words = file.read().replace('"', '').split(',')
    
    triangle_words = [word for word in words
                      if is_triangle_number(word_score(word))]

    return len(triangle_words)

if __name__ == '__main__':
    print(p42())