from math import inf
from number_theory import is_pentagonal_number, pentagonal_number

def p44() -> None:
    # Let Pa and Pb be two pentagonal numbers, with b > a ==> Pb > Pa 
    # Find minimised pentagonal Pd = Pb - Pa with pentagonal Ps = Pb + Pa
    # From these equations we see that:
    #   Ps = Pb + Pa ==> Pa < Pb < Ps
    #   Pd = Pb - Pa ==> Pd < Pb < Ps
    # We don't know the ordering of Pa and Pd
    # In terms of Pa and Pd:
    #   Pb = Pd + Pa
    #   Ps = Pb + Pa = Pd + 2*Pa

    # Start by assuming Pa <= Pd. This allows Pd to start low and increase,
    # while also capping Pa at Pd. The first answer found will be the smallest
    # for Pa <= Pd.
    solution_when_Pa_lte_Pd = 0
    d = 0
    while solution_when_Pa_lte_Pd == 0:
        d += 1
        Pd = pentagonal_number(d)
        for a in range(1, d + 1):
            Pa = pentagonal_number(a)
            Pb = Pa + Pd
            Ps = Pa + Pb
            if is_pentagonal_number(Pb) and is_pentagonal_number(Ps):
                solution_when_Pa_lte_Pd = Pd
                break

    # At this stage solution_when_Pa_lte_Pd is the correct answer.
    # The code block below this return statement will prove this, but it takes
    # a long time to execute. Instead, return the answer we know is correct.
    return solution_when_Pa_lte_Pd
    
    # Next, examine when Pd < Pa. This allows Pa to start low and increase.
    # To be more minimised Pd needs to be < solution_when_Pa_lte_Pd
    # Given Pa < Pb, the smallest possible difference between them is when Pb
    # is the next pentagonal number after Pa i.e. b = a + 1.
    # Therefore P(a+1) - Pa <= Pd < solution_when_Pa_lte_Pd
    a = 0
    largest_possible_d = d
    candidate_Pd = []
    while True:
        a += 1
        Pa = pentagonal_number(a)
        smallest_possible_Pd = pentagonal_number(a + 1) - Pa
        if smallest_possible_Pd >= solution_when_Pa_lte_Pd:
            break
        smallest_possible_d = estimate_pentagonal_base(smallest_possible_Pd)
        for d in range(smallest_possible_d, largest_possible_d):
            Pd = pentagonal_number(d)
            Pb = Pa + Pd
            Ps = Pa + Pb
            if is_pentagonal_number(Pb) and is_pentagonal_number(Ps):
                # By construction Pd < solution_when_Pa_lte_Pd
                candidate_Pd.append(Pd)

    # Now check if we found any smaller Pd values
    if len(candidate_Pd) > 0:
        candidate_Pd.sort()
        return candidate_Pd[0]
    else:
        return solution_when_Pa_lte_Pd

if __name__ == '__main__':
    print(p44())
