def p19() -> int:

    MONTH_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Sunday = 0, Monday = 1, ..., Saturday = 6
    weekday = 2
    sunday_count = 0

    for year in range(1901, 2001):
        
        # first day of Jan - check if Sunday
        if weekday == 0: sunday_count += 1

        # add days to roll to Feb
        weekday = (weekday + MONTH_LENGTHS[0]) % 7

        # first day of Feb - check if Sunday
        if weekday == 0: sunday_count += 1

        # determine how many leap days are required (0 or 1)
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): leap_days = 1
        else: leap_days = 0

        # add days to roll to Mar
        weekday = (weekday + MONTH_LENGTHS[1] + leap_days) % 7

        for month in range(2, 12):
            if weekday == 0: sunday_count += 1
            weekday = (weekday + MONTH_LENGTHS[month]) % 7
    
    return sunday_count

if __name__ == '__main__':
    print(p19())
