from poker import Card, Hand

def p54(data_file_path: str) -> int:
    player_1_wins = 0
    with open(data_file_path) as file:
        for line in file:
            cards = line.split()
            player_1_hand = Hand(list(map(Card, cards[0:5])))
            player_2_hand = Hand(list(map(Card, cards[5:10])))
            if player_1_hand > player_2_hand:
                player_1_wins += 1
    
    return player_1_wins

if __name__ == '__main__':
    print(p54('./data/p054_poker.txt'))
