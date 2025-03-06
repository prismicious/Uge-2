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

