def chain_result(number: int) -> int:
    if number in {1, 89}:
        return number

    next_number = sum(n*n for n in map(int, str(number)))
    return chain_result(next_number)

def p92(stop: int) -> int:
    reached_89_count = 0
    results: dict[int, int] = dict()

    for number in range(1, stop):
        working = number
        seen: list[int] = []

        while working != 1 and working != 89:
            seen.append(working)
            if working in results:
                working = results[working]
            else:
                working = sum(n*n for n in map(int, str(working)))

        if working == 89:
            reached_89_count += 1
        
        results.update({seen_number: working for seen_number in seen})

    return reached_89_count

if __name__ == '__main__':
    print(p92(10000000))
