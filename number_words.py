def number_to_words(number: int) -> str:
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