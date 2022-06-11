from itertools import chain, cycle

from continued_fractions import convergents, terms_for_sqrt_of


def p66(stop: int) -> int:
    max_x = 0
    radicand_producing_max_x = 0
    for radicand in range(2, stop):
        continued_fraction = terms_for_sqrt_of(radicand, 2*stop)
        
        # if radicand was a square number we have no solutions
        repeating_terms = continued_fraction[1]
        if len(repeating_terms) == 0:
            continue
        
        # build an infinite term generator
        static_terms = continued_fraction[0]
        all_terms = chain(static_terms, cycle(repeating_terms))

        # test each of the convergents for a solution. The first one
        # will be minimal in x
        for fraction in convergents(all_terms):
            x = fraction.numerator
            y = fraction.denominator
            if x*x - radicand*y*y == 1:
                #print(f'Solution radicand={radicand}, x={x}, y={y}')
                if x > max_x:
                    max_x = x
                    radicand_producing_max_x = radicand
                break
    
    return radicand_producing_max_x

if __name__ == '__main__':
    print(p66(8))
    print(p66(1001))
