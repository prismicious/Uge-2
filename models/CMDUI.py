from models.Enums import Action
from models.TurnResult import TurnResult
from utils import has_blackjack

player_has_blackjack = False
dealer_has_blackjack = False


class CMDUI():
    def display_hand(self, player_name, hand):
        print(f'{player_name}: ', end="")
        print(" ".join(str(card) for card in hand.cards), f"[{hand.value}]")

    def display_result(self, result: TurnResult):
        if result.action == Action.START:
            if result.player_name == 'Dealer':
                self.display_hand_concealed(result.hand.cards[0])

            self.display_draw_multiple(
                result.player_name, result.cards, result.hand)
            return

        if result.action == Action.HIT:
            self.display_draw(result.player_name, result.card, result.hand)
            return

        if result.action == Action.STAND:
            if has_blackjack(result.hand.value):
                self.display_hand(result.player_name, result.hand)
                self.display_blackjack(result.player_name)
                return

            self.display_stand(result.player_name, result.hand)

        if result.action == Action.BUST:
            self.display_bust(result.player_name, result.hand.value)
            return

        return


    def display_blackjack(self, player_name):
        print(f'{player_name} has BlackJack! ♠\n')

    def display_game_state(self, player_name, player_hand, dealer_name, dealer_hand):
        if player_hand.value == 0:
            return

        self.display_hand(player_name, player_hand)
        self.display_hand(dealer_name, dealer_hand)

    def display_draw(self, player_name, card, hand):
        print(f"{player_name} has hit and drew {card} [{hand.value}]")

    def display_stand(self, player_name, hand):
        self.display_hand(player_name, hand)
        print(f"{player_name} has decided to stand!")

    def display_draw_multiple(self, player_name, cards, hand):
        print(f"{player_name} drew:")
        print(" ".join(str(card) for card in cards), f"[{hand.value}]")

        if hand.value == 21:
            self.display_blackjack(player_name)

    def display_winner(self, player_name):
        if player_name == 'Tie':
            print('It\'s a tie!\n')

        print(f'{player_name} wins!\n')

    def display_bust(self, player_name, value):
        print(f'{player_name} busts! [{value}]\n')

    def display_empty_deck(self):
        print('Deck is empty. Shuffling...\n')

    def display_start(self, name):
        print(f'Welcome to Blackjack {name}!\n')
        print('Do you wish to start a new game? (y/n)')

    def display_game_over(self):
        print('Game over!\n')
        print('Do you wish to play again?')

    def display_invalid_input(self):
        print('Invalid input. Please try again.\n')

    def display_hand_concealed(self, card):
        print(f'Dealer: ', end="")
        print(str(card), '[?]')
