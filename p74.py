from collections import deque

from sums import digit_factorial_sum


def p74(stop: int, wanted_length: int) -> int:
    chain_length = {
        1: 1,
        2: 1,
        40585: 1,
        145: 1,
        169: 3,
        363601: 3,
        1454: 3,
        871: 2,
        45361: 2,
        872: 2,
        45362: 2,
    }
    correct_length_chains = 0

    for start in range(1, stop):
        visited_stack = deque()
        unwind_stack = False
        current_value = start
        
        while unwind_stack == False:
            if current_value in chain_length:
                # we know how many terms are left
                unwind_stack = True
                depth = chain_length[current_value]
            # elif current_value in visited_stack:
            #     # we have found a loop - code it in chain_length definition
            #     print(f'Visited {current_value}')
            #     unwind_stack = True
            #     depth = 0
            else:
                visited_stack.append(current_value)
                current_value = digit_factorial_sum(current_value)
        
        #unwind the stack, storing depths in chain_length
        while len(visited_stack) > 0:
            current_value = visited_stack.pop()
            depth += 1
            chain_length[current_value] = depth

        if depth == wanted_length:
            correct_length_chains += 1
    
    return correct_length_chains

if __name__ == '__main__':
    print(p74(10, 1))
    print(p74(1000000, 60))
