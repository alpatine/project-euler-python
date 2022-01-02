def p43() -> int:
    sum_components = []
    d1_candidates = range(0, 10)
    for d1 in d1_candidates:
        d2_candidates = [x for x in range(0, 10)
                         if x != d1]
        for d2 in d2_candidates:
            d3_candidates = [x for x in range(0, 10)
                             if x not in [d1, d2]]
            for d3 in d3_candidates:
                d4_candidates = [x for x in range(0, 10, 2)
                                 if x not in [d1, d2, d3]]
                for d4 in d4_candidates:
                    d5_candidates = [x for x in range((2 * (d3 + d4)) % 3, 10, 3)
                                     if x not in [d1, d2, d3, d4]]
                    for d5 in d5_candidates:
                        d6_candidates = [x for x in range(0, 10, 5)
                                         if x not in [d1, d2, d3, d4, d5]]
                        for d6 in d6_candidates:
                            if d6 == 0:
                                d7_candidates = [x for x in range((5 * d5) % 7, 10, 7)
                                                 if x not in [d1, d2, d3, d4, d5, d6]]
                            elif d6 == 5:
                                d7_candidates = [x for x in range((5 * d5 + 6) % 7, 10, 7)
                                                 if x not in [d1, d2, d3, d4, d5, d6]]
                            else:
                                d7_candidates = []
                            for d7 in d7_candidates:
                                d8_candidates = [x for x in range((d7 + 10 * d6) % 11, 10, 11)
                                                 if x not in [d1, d2, d3, d4, d5, d6, d7]]
                                for d8 in d8_candidates:
                                    d9_candidates = [x for x in range((3 * (10 * d7 + d8)) % 13, 10, 13)
                                                     if x not in [d1, d2, d3, d4, d5, d6, d7, d8]]
                                    for d9 in d9_candidates:
                                        d10_candidates = [x for x in range((7 * (10 * d8 + d9)) % 17, 10, 17)
                                                          if x not in [d1, d2, d3, d4, d5, d6, d7, d8, d9]]
                                        for d10 in d10_candidates:
                                            number = 0
                                            for digit in [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]:
                                                number *= 10
                                                number += digit
                                            sum_components.append(number)
    return sum(sum_components)

if __name__ == '__main__':
    print(p43())
