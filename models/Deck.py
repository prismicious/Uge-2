import random
from models.Card import Card
from models.Enums import Suit

class Deck():
    def __init__(self):
        suits = Suit.CLUBS.value, Suit.DIAMONDS.value, Suit.HEARTS.value, Suit.SPADES.value
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
        
    def draw(self):
        """"Draw a card from the deck."""
        return self.cards.pop()
    
    def draw_multiple(self, num_cards):
        """Draw multiple cards from the deck."""
        
        draw = []
        
        for _ in range(num_cards):
            if len(self.cards) == 0:
                raise ValueError('Deck is empty')
            
            self.draw()
            draw.append(self.draw())
            
        return draw