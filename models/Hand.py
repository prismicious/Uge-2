from typing import List
from models.Card import Card


class Hand():
    def __init__(self):
        self.cards: List[Card] = []
        self.value = 0
        
    def add_card(self, card: Card):
        self.cards.append(card)
        self.calc_value()
        
    def add_cards(self, cards: List[Card]):
        
        for card in cards:
            self.cards.append(card)
            self.calc_value()
        
    def calc_value(self):
        self.value = 0
        
        for card in self.cards:
            if card.rank.isnumeric():
                self.value += int(card.rank)
                
            if card.rank in ['J', 'Q', 'K']:
                self.value += 10
                
            if card.rank == 'A':
                if self.value + 11 <= 21:
                    self.value += 11
                    
                else:
                    self.value += 1
            