collatz_lengths = {}

def collatz_length(number: int) -> int:
    """Calculate the collatz sequence length for a number

    All values that are visited while generating the sequence
    will have their sequence length cached. This allows
    for greatly improved performance with multiple use.
    """

    length_if_known = collatz_lengths.get(number)
    if length_if_known is not None: return length_if_known

    visited_numbers = []
    length = 1
    current_value = number
    while current_value > 1:
        if current_value % 2 == 0: current_value //= 2
        else: current_value = 3 * current_value + 1
        
        length_if_known = collatz_lengths.get(current_value)
        if length_if_known is not None:
            length += length_if_known
            current_value = 1
        else:
            visited_numbers.append(current_value)
            length += 1

    collatz_lengths[number] = length
   
    adjusted_length = length
    for visited_number in visited_numbers:
        adjusted_length -= 1
        collatz_lengths[visited_number] = adjusted_length

    return length

def reset_cached_lengths():
    """Clear all known collatz lengths"""
    collatz_lengths.clear()

