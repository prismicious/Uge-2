from models.CMDUI import CMDUI
from models.Deck import Deck
from models.Enums import Action
from models.Player import Dealer
from models.Player import Player


class Game():
    def __init__(self, name):
        self.deck = Deck()
        self.player = Player(name)
        self.dealer = Dealer()
        self.cmd = CMDUI()
        self.turn = 0

    def start_game(self):
        self.cmd.display_start(self.player.name)

        user_input = input().strip().lower()

        if user_input == 'y':
            self.deal()

        if user_input == 'n':
            exit()

        else:
            self.cmd.display_invalid_input()

    def deal(self):
        while not self.check_game_over():
            if self.is_deck_empty():
                self.deck = Deck()
                self.cmd.display_empty_deck()

            if self.turn == 0:
                result = self.dealer.start_game(self.deck.draw_multiple(2))
                self.cmd.display_result(result)

            if self.turn != 0:
                if self.dealer.action != Action.STAND:
                    result = self.dealer.take_turn(self.deck.draw())
                    self.cmd.display_result(result)

            result = self.player.take_turn(self.deck.draw())
            self.cmd.display_result(result)

            self.turn += 1

    def check_game_over(self):
        if self.player.action == Action.STAND and self.dealer.action == Action.STAND:
            winner = self.determine_winner(self.player.hand.value,
                                  self.dealer.hand.value)
            self.cmd.display_winner(winner)
            return True

        if self.player.hand.value >= 22:
            self.cmd.display_bust(self.player)
            return True

        if self.dealer.hand.value >= 22:
            self.cmd.display_bust(self.dealer)
            self.cmd.display_winner(self.player.name)
            return True

        return False

    def is_deck_empty(self):
        return len(self.deck.cards) == 0

    def determine_winner(self, player_hand_value, dealer_hand_value):
        if player_hand_value > dealer_hand_value:
            return self.player.name

        if dealer_hand_value > player_hand_value:
            return self.dealer.name
