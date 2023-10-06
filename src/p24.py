from typing import List
from math import factorial

def p24(chars: List[str], permutation_number: int) -> List[str]:
    # permutation_number is 1 based, but permute_chars is 0 based
    return permute_chars(chars, permutation_number - 1)

def permute_chars(chars: List[str], permutation_number: int) -> List[str]:
    # Select a charcter
    permutations_per_char = factorial(len(chars) - 1)
    (selected_char_index, permutations_remaining) = divmod(permutation_number, permutations_per_char)
    selected_char = chars[selected_char_index]
    unselected_chars = [char for index, char in enumerate(chars) if index != selected_char_index]
    
    # Permute remaining characters (if permitations remain)
    if permutations_remaining > 0:
        next_chars = permute_chars(unselected_chars, permutations_remaining)
    else:
        next_chars = unselected_chars
    
    # Combine selected character with permuted remaining characters
    return [selected_char] + next_chars

if __name__ == '__main__':
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print (p24(chars, 1000000))