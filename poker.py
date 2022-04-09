from cgi import test
from collections import Counter
from enum import Enum
from typing import List, Tuple

class Card:
    def __init__(self, value: str) -> None:
        self.rank = value[0]
        self.suit = value[1]

class Hand:

    # Hand Types
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

    # Ranks
    MAX_VALUE = 15
    RANK_VALUE_MAP = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }

    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards
        self.value = self.calculate_hand_value()

    def calculate_hand_value(self) -> List[int]:
        hand_value = [Hand.MAX_VALUE] * 6
        suit_counter = Counter([card.suit for card in self.cards])
        rank_counter = Counter([card.rank for card in self.cards])
        rank_counts = rank_counter.most_common(5)
        
        high_to_low_rank_values = [Hand.RANK_VALUE_MAP[x]
                                   for x in rank_counter]
        high_to_low_rank_values.sort(reverse=True)

        max_run_length = 0
        current_run_length = 0
        high_rank = ''

        for rank in '23456789TJQKA':
            test_rank = rank_counter.get(rank)
            if test_rank is not None and test_rank > 0:
                current_run_length += 1
                max_run_length = max(max_run_length, current_run_length)
                high_rank = rank
            else:
                current_run_length = 0

        # royal flush
        # straight flush
        if len(suit_counter) == 1 and max_run_length == 5:
            if high_rank == 'A':
                hand_value[0] = Hand.ROYAL_FLUSH
            else:
                hand_value[0] = Hand.STRAIGHT_FLUSH
            hand_value[1:6] = high_to_low_rank_values

        # four of a kind
        elif rank_counts[0][1] == 4:
            hand_value[0] = Hand.FOUR_OF_A_KIND
            hand_value[1] = Hand.RANK_VALUE_MAP[rank_counts[0][0]]
            hand_value[2] = Hand.RANK_VALUE_MAP[rank_counts[1][0]]
        
        # full house
        elif rank_counts[0][1] == 3 and rank_counts[1][1] == 2:
            hand_value[0] = Hand.FULL_HOUSE
            hand_value[1] = Hand.RANK_VALUE_MAP[rank_counts[0][0]]
            hand_value[2] = Hand.RANK_VALUE_MAP[rank_counts[1][0]]

        # flush
        elif len(suit_counter) == 1:
            hand_value[0] = Hand.FLUSH
            hand_value[1:6] = high_to_low_rank_values
        
        # straight
        elif max_run_length == 5:
            hand_value[0] = Hand.STRAIGHT
            hand_value[1:6] = high_to_low_rank_values

        # three of a kind
        elif rank_counts[0][1] == 3 and rank_counts[1][1] == 1:
            hand_value[0] = Hand.THREE_OF_A_KIND
            hand_value[1] = Hand.RANK_VALUE_MAP[rank_counts[0][0]]            
            hand_value[2] = Hand.RANK_VALUE_MAP[rank_counts[1][0]]
            hand_value[3] = Hand.RANK_VALUE_MAP[rank_counts[2][0]]
            hand_value[2:4] = reversed(sorted(hand_value[2:4]))

        # two pairs
        elif rank_counts[0][1] == 2 and rank_counts[1][1] == 2:
            hand_value[0] = Hand.TWO_PAIR
            hand_value[1] = Hand.RANK_VALUE_MAP[rank_counts[0][0]]
            hand_value[2] = Hand.RANK_VALUE_MAP[rank_counts[1][0]]
            hand_value[3] = Hand.RANK_VALUE_MAP[rank_counts[2][0]]
            hand_value[1:3] = reversed(sorted(hand_value[1:3]))

        # one pair
        elif rank_counts[0][1] == 2 and rank_counts[1][1] == 1:
            hand_value[0] = Hand.ONE_PAIR
            hand_value[1] = Hand.RANK_VALUE_MAP[rank_counts[0][0]]
            hand_value[2] = Hand.RANK_VALUE_MAP[rank_counts[1][0]]
            hand_value[3] = Hand.RANK_VALUE_MAP[rank_counts[2][0]]
            hand_value[4] = Hand.RANK_VALUE_MAP[rank_counts[3][0]]
            hand_value[2:5] = reversed(sorted(hand_value[2:5]))

        # high card
        else:
            hand_value[0] = Hand.HIGH_CARD
            hand_value[1] = Hand.RANK_VALUE_MAP[rank_counts[0][0]]
            hand_value[2] = Hand.RANK_VALUE_MAP[rank_counts[1][0]]
            hand_value[3] = Hand.RANK_VALUE_MAP[rank_counts[2][0]]
            hand_value[4] = Hand.RANK_VALUE_MAP[rank_counts[3][0]]
            hand_value[5] = Hand.RANK_VALUE_MAP[rank_counts[4][0]]
            hand_value[1:6] = reversed(sorted(hand_value[1:6]))
        
        return hand_value

    def __eq__(self, other: 'Hand'):
        return self.value == other.value
    
    def __ne__(self, other: 'Hand'):
        return self.value != other.value
    
    def __gt__(self, other: 'Hand'):
        return self.value > other.value
    
    def __ge__(self, other: 'Hand'):
        return self.value >= other.value
    
    def __lt__(self, other: 'Hand'):
        return self.value < other.value
    
    def __le__(self, other: 'Hand'):
        return self.value <= other.value