# Convering a Number into Words
Converting numbers to words comes up a few times in these problems. This will
describe a function that can take a number and output that number as words.
Spaces have not been a factor in the problems encountered, so to keep this
simple spaces are not added to the output.

For example, $103$ will be output as `onehundredandthree`.

## Defining the words to be used
First, we define the words that represent the different numbers. We will need a
list of words for ones digits, special words for the teens, words for the tens
digit, and then scale words as we go through thousand, million, etc.

Each list will contain a number word based on it's position in the list.

```python
ONES_WORDS = ['', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']
TENS_WORDS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
TEENS_WORDS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen','sixteen', 'seventeen', 'eighteen', 'nineteen']
SCALE_WORDS = ['', 'thousand', 'million', 'billion', 'trillion']
```

## Padding the number
The algorithm used works in blocks of three digits. The digit length of a number
is not always a multiple of three, so the first step in preparing the number is
to left pad it with $0$ until it's length is a multiple of three.

### Examples
$$\begin{aligned}
54 &\rightarrow 054 \\
400 &\rightarrow 400 \\
1789 &\rightarrow 001789
\end{aligned}$$

## Processing the number
Once the padding is complete, we can process the number in blocks of three digits. We can process the block as though it was a three-digit number itself and then append the relevant scale word based on how many unprocessed digits remain.

### Examples
$$\begin{aligned}
054 &\rightarrow \text{fiftyfour} \\
400 &\rightarrow \text{fourhundred} \\
001789 &\rightarrow \text{one} + \text{thousand} + \text{sevenhundredandeightynine}
\end{aligned}$$

## Python implementation
``` python
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
```