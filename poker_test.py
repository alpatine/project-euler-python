from itertools import product
from unittest import TestCase
from poker import Card, Hand

class Card_Test(TestCase):
    def test_cards(self):
        for (rank, suit) in product('23456789TJQKA', 'SDCH'):
            card = Card(''.join([rank, suit]))
            self.assertEqual(card.rank, rank)
            self.assertEqual(card.suit, suit)

class Hand_Test(TestCase):
    def test_royal_flush(self):
        cards = list(map(Card, ['AH', 'KH', 'QH', 'JH', 'TH']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.ROYAL_FLUSH)

    def test_straight_flush(self):
        cards = list(map(Card, ['4D', '6D', '7D', '5D', '3D']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.STRAIGHT_FLUSH)

    def test_four_of_a_kind(self):
        cards = list(map(Card, ['4D', '4H', '7D', '4C', '4S']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.FOUR_OF_A_KIND)
    
    def test_full_house(self):
        cards = list(map(Card, ['6D', '6H', '2H', '6S', '2C']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.FULL_HOUSE)
    
    def test_flush(self):
        cards = list(map(Card, ['6H', '8H', '2H', 'AH', 'KH']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.FLUSH)
    
    def test_straight(self):
        cards = list(map(Card, ['6C', '8H', '7H', '9H', '5H']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.STRAIGHT)
    
    def test_three_of_a_kind(self):
        cards = list(map(Card, ['6D', '6H', '2H', '6S', '3C']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.THREE_OF_A_KIND)
    
    def test_two_pairs(self):
        cards = list(map(Card, ['6D', '6H', '2H', '3S', '2C']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.TWO_PAIR)
    
    def test_one_pair(self):
        cards = list(map(Card, ['6D', '6H', '2H', '3S', '4C']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.ONE_PAIR)
    
    def test_high_card(self):
        cards = list(map(Card, ['6D', '8C', 'TH', '3S', '2C']))
        hand = Hand(cards)
        value = hand.value
        self.assertEqual(value[0], Hand.HIGH_CARD)
    
    def test_comparing_different_hand_types(self):
        hands = [
            Hand(list(map(Card, ['2D', '4C', '6H', '8S', 'TD']))), #HC
            Hand(list(map(Card, ['2D', '4C', '4D', '5H', '8D']))), #OP
            Hand(list(map(Card, ['2C', '3H', '3C', '6D', '6C']))), #TP
            Hand(list(map(Card, ['3D', '4H', '4D', '4S', 'TC']))), #TK
            Hand(list(map(Card, ['7S', '8C', '9H', 'TC', 'JD']))), #S
            Hand(list(map(Card, ['3H', '5H', 'JH', 'AH', '2H']))), #F
            Hand(list(map(Card, ['5D', 'TC', 'TH', '5S', '5H']))), #FH
            Hand(list(map(Card, ['7H', '7D', '7C', '7S', '8H']))), #FK
            Hand(list(map(Card, ['8D', '9D', 'TD', 'JD', 'QD']))), #SF
            Hand(list(map(Card, ['TC', 'JC', 'QC', 'KC', 'AC']))), #RF
        ]

        for left_index in range(0, len(hands)):
            for right_index in range(left_index + 1, len(hands)):
                self.assertTrue(hands[right_index] > hands[left_index])
    
    def test_comparing_royal_flush(self):
        hands = [
            Hand(list(map(Card, ['AH', 'KH', 'QH', 'JH', 'TH']))),
            Hand(list(map(Card, ['TS', 'QS', 'KS', 'JS', 'AS']))),
            Hand(list(map(Card, ['AD', 'KD', 'QD', 'JD', 'TD']))),
            Hand(list(map(Card, ['AC', 'KC', 'QC', 'JC', 'TC']))),
        ]

        for left_index in range(0, len(hands)):
            for right_index in range(left_index + 1, len(hands)):
                self.assertEqual(hands[left_index], hands[right_index])
    
    def test_comparing_straight_flush(self):
        hands = [
            Hand(list(map(Card, ['3H', '4H', '5H', '6H', '7H']))),
            Hand(list(map(Card, ['3S', '4S', '5S', '6S', '7S']))),
            Hand(list(map(Card, ['6D', '7D', '8D', '9D', 'TD']))),
        ]

        self.assertEqual(hands[0], hands[1])
        self.assertTrue(hands[2] > hands[1])
    
    def test_comparing_four_of_a_kind(self):
        hands = [
            Hand(list(map(Card, ['4H', '4C', '4D', '4S', '2H']))),
            Hand(list(map(Card, ['4H', '4C', '4D', '4S', '3S']))),
            Hand(list(map(Card, ['4H', '4C', '4D', '4S', '7S']))),
            Hand(list(map(Card, ['4H', '4C', '4D', '4S', '8S']))),
            Hand(list(map(Card, ['5H', '5C', '5D', '5S', '7S']))),
            Hand(list(map(Card, ['5H', '5C', '5D', '5S', '8S']))),
        ]

        for left_index in range(0, len(hands)):
            for right_index in range(left_index + 1, len(hands)):
                self.assertTrue(hands[right_index] > hands[left_index])
    
    def test_comparing_full_house(self):
        hands = [
            Hand(list(map(Card, ['3H', '3C', '3D', '2S', '2H']))),
            Hand(list(map(Card, ['3H', '3C', '3D', '4S', '4H']))),
            Hand(list(map(Card, ['4H', '4C', '4D', '2S', '2H']))),
            Hand(list(map(Card, ['4H', '4C', '4D', '3S', '3H']))),
        ]

        for left_index in range(0, len(hands)):
            for right_index in range(left_index + 1, len(hands)):
                self.assertTrue(hands[right_index] > hands[left_index])
    
    def test_comparing_flush(self):
        ordered_hands = [
            Hand(list(map(Card, ['2H', '4H', '6H', '8H', 'TH']))),
            Hand(list(map(Card, ['3H', '4H', '6H', '8H', 'TH']))),
            Hand(list(map(Card, ['2H', '5H', '6H', '8H', 'TH']))),
            Hand(list(map(Card, ['2H', '4H', '7H', '8H', 'TH']))),
            Hand(list(map(Card, ['2H', '4H', '6H', '9H', 'TH']))),
            Hand(list(map(Card, ['2H', '4H', '6H', '8H', 'JH']))),
        ]

        for left_index in range(0, len(ordered_hands)):
            for right_index in range(left_index + 1, len(ordered_hands)):
                self.assertTrue(ordered_hands[right_index]
                                > ordered_hands[left_index])

        equal_hands = [
            Hand(list(map(Card, ['2H', '4H', '6H', '8H', 'TH']))),
            Hand(list(map(Card, ['2D', '4D', '6D', '8D', 'TD']))),
            Hand(list(map(Card, ['2S', '4S', '6S', '8S', 'TS']))),
            Hand(list(map(Card, ['2C', '4C', '6C', '8C', 'TC']))),
        ]

        for left_index in range(0, len(equal_hands)):
            for right_index in range(left_index + 1, len(equal_hands)):
                self.assertEqual(equal_hands[right_index],
                                 equal_hands[left_index])

    def test_comparing_straight(self):
        ordered_hands = [
            Hand(list(map(Card, ['2H', '4H', '6H', '8H', 'TH']))),
            Hand(list(map(Card, ['3H', '4H', '6H', '8H', 'TH']))),
            Hand(list(map(Card, ['2H', '5H', '6H', '8H', 'TH']))),
            Hand(list(map(Card, ['2H', '4H', '7H', '8H', 'TH']))),
            Hand(list(map(Card, ['2H', '4H', '6H', '9H', 'TH']))),
            Hand(list(map(Card, ['2H', '4H', '6H', '8H', 'JH']))),
        ]

        for left_index in range(0, len(ordered_hands)):
            for right_index in range(left_index + 1, len(ordered_hands)):
                self.assertTrue(ordered_hands[right_index]
                                > ordered_hands[left_index])
    
    def test_comparing_three_of_a_kind(self):
        ordered_hands = [
            Hand(list(map(Card, ['6H', '6D', '6C', '2S', '4H']))),
            Hand(list(map(Card, ['6H', '6D', '6C', '3S', '4H']))),
            Hand(list(map(Card, ['6H', '6D', '6C', '3S', '5H']))),
            Hand(list(map(Card, ['6H', '6D', '6C', '7S', '9H']))),
            Hand(list(map(Card, ['6H', '6D', '6C', '8S', '9H']))),
            Hand(list(map(Card, ['6H', '6D', '6C', '7S', 'TH']))),
            Hand(list(map(Card, ['7H', '7D', '7C', '2S', '4H']))),
            Hand(list(map(Card, ['7H', '7D', '7C', '8S', '9H']))),
        ]

        for left_index in range(0, len(ordered_hands)):
            for right_index in range(left_index + 1, len(ordered_hands)):
                self.assertTrue(ordered_hands[right_index]
                                > ordered_hands[left_index])
    
    def test_comparing_two_pairs(self):
        ordered_hands = [
            Hand(list(map(Card, ['2H', '2D', '4C', '4S', '6H']))),
            Hand(list(map(Card, ['2H', '2D', '4C', '4S', '7H']))),
            Hand(list(map(Card, ['3H', '3D', '4C', '4S', '6H']))),
            Hand(list(map(Card, ['2H', '2D', '5C', '5S', '6H']))),
            Hand(list(map(Card, ['2H', '2D', '4C', '6S', '6H']))),
            Hand(list(map(Card, ['2H', '2D', '5C', '6S', '6H']))),
            Hand(list(map(Card, ['3H', '3D', '4C', '6S', '6H']))),
            Hand(list(map(Card, ['2H', '2D', '4C', '7S', '7H']))),
            Hand(list(map(Card, ['2H', '4D', '4C', '7S', '7H']))),
            Hand(list(map(Card, ['3H', '4D', '4C', '7S', '7H']))),
            Hand(list(map(Card, ['2H', '5D', '5C', '7S', '7H']))),
            Hand(list(map(Card, ['2H', '4D', '4C', '8S', '8H']))),
        ]

        for left_index in range(0, len(ordered_hands)):
            for right_index in range(left_index + 1, len(ordered_hands)):
                self.assertTrue(ordered_hands[right_index]
                                > ordered_hands[left_index])
        
        equal_hands = [
            # base
            Hand(list(map(Card, ['2C', '2D', '4C', '4D', '6C']))),

            # rotate single suite
            Hand(list(map(Card, ['2C', '2D', '4C', '4D', '6D']))),
            Hand(list(map(Card, ['2C', '2D', '4C', '4D', '6H']))),
            Hand(list(map(Card, ['2C', '2D', '4C', '4D', '6S']))),

            # rotate middle pair suites
            Hand(list(map(Card, ['2C', '2D', '4C', '4H', '6C']))),
            Hand(list(map(Card, ['2C', '2D', '4C', '4S', '6C']))),
            Hand(list(map(Card, ['2C', '2D', '4D', '4H', '6C']))),
            Hand(list(map(Card, ['2C', '2D', '4D', '4S', '6C']))),
            Hand(list(map(Card, ['2C', '2D', '4H', '4S', '6C']))),

            # rotate first pair suites
            Hand(list(map(Card, ['2C', '2H', '4C', '4D', '6C']))),
            Hand(list(map(Card, ['2C', '2S', '4C', '4D', '6C']))),
            Hand(list(map(Card, ['2D', '2H', '4C', '4D', '6C']))),
            Hand(list(map(Card, ['2D', '2S', '4C', '4D', '6C']))),
            Hand(list(map(Card, ['2H', '2S', '4C', '4D', '6C']))),
        ]

        for left_index in range(0, len(equal_hands)):
            for right_index in range(left_index + 1, len(equal_hands)):
                self.assertEqual(equal_hands[right_index],
                                 equal_hands[left_index])
    
    def test_comparing_one_pair(self):
        ordered_hands = [
            Hand(list(map(Card, ['2H', '2D', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2H', '2D', '5C', '6S', '8H']))),
            Hand(list(map(Card, ['2H', '2D', '4C', '7S', '8H']))),
            Hand(list(map(Card, ['2H', '2D', '4C', '6S', '9H']))),
            Hand(list(map(Card, ['2H', '4D', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2H', '4D', '6C', '6S', '8H']))),
            Hand(list(map(Card, ['2H', '4D', '6C', '8S', '8H']))),
            
        ]

        for left_index in range(0, len(ordered_hands)):
            for right_index in range(left_index + 1, len(ordered_hands)):
                self.assertTrue(ordered_hands[right_index]
                                > ordered_hands[left_index])
        
        equal_hands = [
            Hand(list(map(Card, ['2C', '2D', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2C', '2H', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2C', '2S', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2D', '2H', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2D', '2S', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2H', '2S', '4C', '6S', '8H']))),
            Hand(list(map(Card, ['2C', '2D', '4H', '6S', '8H']))),
            Hand(list(map(Card, ['2C', '2D', '4C', '6H', '8H']))),
            Hand(list(map(Card, ['2C', '2D', '4C', '6S', '8D']))),
        ]

        for left_index in range(0, len(equal_hands)):
            for right_index in range(left_index + 1, len(equal_hands)):
                self.assertEqual(equal_hands[right_index],
                                 equal_hands[left_index])
    
    def test_comparing_high_card(self):
        ordered_hands = [
            Hand(list(map(Card, ['2H', '4D', '6C', '8S', 'TH']))),
            Hand(list(map(Card, ['3H', '4D', '6C', '8S', 'TH']))),
            Hand(list(map(Card, ['2H', '5D', '6C', '8S', 'TH']))),
            Hand(list(map(Card, ['2H', '4D', '7C', '8S', 'TH']))),
            Hand(list(map(Card, ['2H', '4D', '6C', '9S', 'TH']))),
            Hand(list(map(Card, ['2H', '4D', '6C', '8S', 'JH']))),
            
        ]

        for left_index in range(0, len(ordered_hands)):
            for right_index in range(left_index + 1, len(ordered_hands)):
                self.assertTrue(ordered_hands[right_index]
                                > ordered_hands[left_index])
        
        equal_hands = [
            Hand(list(map(Card, ['2H', '4D', '6C', '8S', 'TH']))),
            Hand(list(map(Card, ['2S', '4D', '6C', '8S', 'TH']))),
            Hand(list(map(Card, ['2H', '4S', '6C', '8S', 'TH']))),
            Hand(list(map(Card, ['2H', '4D', '6S', '8S', 'TH']))),
            Hand(list(map(Card, ['2H', '4D', '6C', '8H', 'TH']))),
            Hand(list(map(Card, ['2H', '4D', '6C', '8S', 'TS']))),
        ]

        for left_index in range(0, len(equal_hands)):
            for right_index in range(left_index + 1, len(equal_hands)):
                self.assertEqual(equal_hands[right_index],
                                 equal_hands[left_index])

    