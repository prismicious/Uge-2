import pickle
from models.Hand import Hand
from models.Enums import Action
from models.TurnResult import TurnResult
from utils import has_blackjack, is_bust, print_typewriter


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.action = Action.START
        self.turns = 0
        self.balance = 100
        self.total_bets = 0
        self.bets_won = 0
        self.bets_lost = 0

    def hit(self, card):
        """Add a card and update the action accordingly."""
        self.turns += 1
        self.hand.add_card(card)

        if is_bust(self.hand.value):
            self.action = Action.BUST

        elif has_blackjack(self.hand.value):
            self.action = Action.STAND
        else:
            self.action = Action.HIT

        return TurnResult(self.name, self.action, self.hand, card)

    def stand(self):
        """Player chooses to stand."""
        self.turns += 1
        self.action = Action.STAND
        return TurnResult(self.name, self.action, self.hand)

    def take_turn(self, deck):
        """Handles turn logic for player."""
        if self.hand.value == 0:  # First turn, draw two cards
            self.hand.add_cards([deck.draw(), deck.draw()])
            return TurnResult(self.name, Action.START, self.hand, cards=self.hand.cards)

        action = self.get_action()

        if action == Action.HIT:
            result = self.hit(deck.draw())
            return result
        else:
            return self.stand()

    def get_action(self):
        """Handles user input for a player's turn."""
        while True:
            print()
            print_typewriter("Do you want to hit or stand? ", False, overwrite=True)
            action = input().strip().lower()
            if action in ["h", "hit", ""]:
                return Action.HIT
            elif action in ["s", "stand"]:
                return Action.STAND
            print("Invalid input. Please try again.")

    def lost_bet(self, amount):
        """update balance with 0 if balance goes below 0
        deduct the amount from the balance and update the total bets and bets lost"""
        deducted_amount = self.balance - amount

        if deducted_amount < 0:
            self.balance = 0

        self.total_bets += 1
        self.bets_lost += 1
        self.reset_player_object()
        
    def tie_bet(self, amount):
        """update the balance with the amount and update the total bets"""
        self.total_bets += 1
        self.balance += amount
        self.reset_player_object()

    def won_bet(self, amount):
        won_amount = 2 * amount
        # Handle logistics, update balance with 2 * amount
        self.total_bets += 1
        self.bets_won += 1
        self.balance += won_amount
        self.reset_player_object()

    def reset_player_object(self):
        # Reset the player's hand, turn and action
        self.hand = Hand()
        self.turns = 0
        self.action = Action.START


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def get_action(self):
        """Automated decision-making for the dealer."""
        if is_bust(self.hand.value):
            return Action.BUST
        elif self.hand.value < 17:
            return Action.HIT
        return Action.STAND

    def take_turn(self, deck):
        """Dealer draws until 17 or bust."""
        if self.hand.value == 0:  # First turn, draw two cards
            self.hand.add_cards([deck.draw(), deck.draw()])
            return TurnResult(self.name, Action.START, self.hand, cards=self.hand.cards)

        action = self.get_action()

        if action == Action.HIT:
            result = self.hit(deck.draw())
            return result

        if action == Action.BUST:
            return TurnResult(self.name, Action.BUST, self.hand)

        return self.stand()
