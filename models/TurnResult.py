from typing import List
from models.Card import Card
from models.Enums import Action
from models.Hand import Hand

class TurnResult():
    def __init__(self, player_name: str, action: Action, hand, card=None, cards=None):
        self.player_name = player_name
        self.action = action
        self.card = card
        self.hand = hand
        self.cards = cards
        

    
