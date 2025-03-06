from typing import List
from models.Card import Card


class Hand():
    def __init__(self):
        self.cards: List[Card] = []
        self.value = 0
        self.blackjack = False
        
    def add_card(self, card: Card):
        self.cards.append(card)
        self.calc_value()
        
    def add_cards(self, cards: List[Card]):
        for card in cards:
            self.cards.append(card)
            self.calc_value()
        
        if self.value == 21:
            self.blackjack = True
        
    def calc_value(self):
        self.value = 0
        aces = 0  # Track the number of Aces

        for card in self.cards:
            if card.rank.isdigit():  # Works for '2'-'10'
                self.value += int(card.rank)
            elif card.rank in {'J', 'Q', 'K'}:
                self.value += 10
            elif card.rank == 'A':
                self.value += 11  # Count Ace as 11 first
                aces += 1  

        # Adjust Aces from 11 to 1 if needed
        while self.value > 21 and aces:
            self.value -= 10
            aces -= 1