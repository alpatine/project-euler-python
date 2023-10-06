def number_to_words(number: int) -> str:
    """Convert a number into words

    Takes a number and converts it into its written word form. Uses the small
    scale for million, billion, etc. There are no spaces inserted between the
    words.
    """
    ONES_WORDS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    TENS_WORDS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    TEENS_WORDS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    SCALE_WORDS = ['', 'thousand', 'million', 'billion', 'trillion']

    number_str = str(number)
    number_len = len(number_str)
    pad_len = (3 - (number_len % 3)) % 3

    # build a list from the digits in the number
    digit_list = [0] * pad_len + [int(digit) for digit in number_str]
    digit_list_len = len(digit_list)

    output_string = ''

    for position in range(0, digit_list_len, 3):
        hundreds_digit = digit_list[position]
        tens_digit = digit_list[position + 1]
        ones_digit = digit_list[position + 2]

        if hundreds_digit > 0:
            output_string += ONES_WORDS[hundreds_digit] + 'hundred'
            if (tens_digit != 0 or ones_digit != 0):
                output_string += 'and'
        if tens_digit == 1:
            output_string += TEENS_WORDS[ones_digit]
        else:
            output_string += TENS_WORDS[tens_digit] + ONES_WORDS[ones_digit]
        
        if (hundreds_digit != 0 or tens_digit != 0 or ones_digit != 0):
            output_string += SCALE_WORDS[(digit_list_len - position) // 3 - 1]
    
    return output_string

def word_score(word: str) -> int:
    """Takes a word and calculates its word score

    The word score is found by comverting to upper case, then equating A = 1,
    B = 2, etc. and then summing over the letters in the word.
    """
    LETTER_SCORES = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
        'Z': 26,
    }

    return sum(LETTER_SCORES[letter] for letter in word.upper())
    