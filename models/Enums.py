import enum

class Action(enum.Enum):
    HIT = 'hit'
    STAND = 'stand'
    START = 'start'
    BUST = 'bust'

class Suit(enum.Enum):
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'

class Rank(enum.Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'  # Represent Ace as 'A'

    def value(self):
        if self == Rank.ACE:
            return 1  # Ace is 1 by default, but you can modify this in your game logic as needed
        elif self in [Rank.JACK, Rank.QUEEN, Rank.KING]:
            return 10  # Face cards are worth 10
        else:
            return int(self.value)  # For numbered cards, just return the value
