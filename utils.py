from models.Enums import Action
from models.TurnResult import TurnResult


def handle_finished_or_blackjack(name, action, hand):
    if action == Action.STAND or has_blackjack(hand.value):
        return TurnResult(name, Action.STAND, hand)

def has_blackjack(value):
    return value == 21

def is_bust(value):
    return value > 21
