from typing import List

def p31(amount: int, coins: List[int]) -> int:

    # The desired count is recursive: A + B
    # Select a coin: X
    # A: Reduce the amount by X and then count ways
    # B: Remove the selected coin from the set and then count ways
    # Exmaple: Amount = 10, Coins = (5, 2, 1)
    # f(10, [5, 2, 1]) = f(5=10-5, [5, 2, 1]) + f(10, [2, 1])

    number_of_coins = len(coins)

    # build a table: rows run from 0 to amount, and columns represent the count of ways
    # when all coins in columns to the right (higher column position) are excluded
    count_table = [[0 for coin_position in range(len(coins))] for value in range(amount+1)]

    # there is always only one way to build the amount 0, no matter how many coins
    for coin_position in range(number_of_coins):
        count_table[0][coin_position] = 1
    
    for value in range(1, amount + 1):
        for coin_position in range(number_of_coins):
            coin_value = coins[coin_position]

            # check the count when the value is reduced by the current coin
            a, b = 0, 0
            if value - coin_value >= 0:
                a = count_table[value - coin_value][coin_position]
            
            # check the count when the current coin (and those to the right) are exluded
            if coin_position > 0:
                b = count_table[value][coin_position - 1]
            
            # now sum the two sub-cases to get the count for this case
            count_table[value][coin_position] = a + b
    
    # with a full table, just read the result off the last cell
    return count_table[-1][-1]

if __name__ == '__main__':
    print(p31(3, [1, 2]))
    print(p31(6, [1, 2, 5]))
    print(p31(200, [1, 2, 5, 10, 20, 50, 100, 200]))
