import time
from models.Enums import Action
from models.Player import Dealer, Player
from models.TurnResult import TurnResult
from utils import (
    animate_symbols,
    calc_value_of_card,
    has_blackjack,
    print_typewriter,
    print_with_delay,
)


class CMDUI:

    def display_hand(self, player_name, hand, is_concealed=False, card=None):
        """ "Display hand of a player or dealer, with the option to conceal the second card."""
        if is_concealed:
            # If the hand is concealed, show the first card and a placeholder for the rest
            print_typewriter(f"Dealer's hand: {card} | ? [{calc_value_of_card(card)}] ")
        else:
            # If the hand is fully revealed, display all cards and the hand's value
            cards_display = f"{player_name}'s hand: " + " | ".join(
                str(card) for card in hand.cards
            )
            print_typewriter(f"{cards_display} [{hand.value}]", False)

    def display_result(self, result: TurnResult):
        """ "Display the result of a turn."""
        if result.action == Action.START:
            if result.player_name == "Dealer":
                self.display_hand_concealed(result.hand.cards[0])
                return

            self.display_draw_multiple(result.player_name, result.cards, result.hand)
            return

        if result.action == Action.HIT:
            self.display_draw(result.player_name, result.card, result.hand)
            return

        if result.action == Action.STAND:
            if result.hand.value == 21:
                self.display_blackjack(result.player_name)
                
            self.display_stand(result.player_name, result.hand)

        if result.action == Action.BUST:
            self.display_draw(result.player_name, result.card, result.hand)
            self.display_bust(result.player_name, result.hand.value)
            return

        return

    def display_blackjack(self, player_name):
        """ "Display a message when a player has BlackJack."""
        print_typewriter(f"{player_name} has BlackJack! ♠\n")

    def display_game_state(self, player: Player, dealer: Dealer):
        """ "Display the game state, including the player's and dealer's hands."""
        if player.hand.value == 0:
            return

        # If dealer's action is 'START', conceal the second card
        if dealer.action == Action.START:
            self.display_hand(
                dealer.name, dealer.hand.cards[0], True, dealer.hand.cards[0]
            )

        # Display the player's hand
        if player.action == Action.STAND:
            return

        self.display_hand(player.name, player.hand)

    def display_draw(self, player_name, card, hand):
        """ "Display drawing a card for a player or dealer."""
        if player_name == "Dealer" and len(hand.cards) == 3:
            self.reveal_card(hand)

        print_typewriter(f"{player_name} has chosen to hit.")
        print_typewriter(f"Drawing card... ")
        animate_symbols()
        print("", end="\r")
        print_with_delay(f" {card} → [{hand.value}] ", end="\n")

    def display_stand(self, player_name, hand):
        """ "Display a player or dealer standing."""
        if player_name == "Dealer" and len(hand.cards) == 2:
            self.reveal_card(hand)
            return

        print_typewriter(f"{player_name} has decided to stand!")

    def display_draw_multiple(self, player_name, cards, hand):
        """ "Display drawing multiple cards for a player or dealer."""
        print_typewriter(f"{player_name} is drawing...", overwrite=True)
        animate_symbols()
        print(f"{player_name} drew: ", end="")
        for card in cards:
            print_with_delay(str(card) + " ")  # Type each card individually
        print(f"→ [{hand.value}]")
        print()

    def display_winner(self, player_name):
        """ "Display the winner of the game."""
        if player_name == "Tie":
            print_typewriter("It's a tie!\n")
            return

        print_typewriter(f"{player_name} wins!\n")

    def display_bust(self, player_name, value):
        """ "Display a player busting."""
        print_typewriter(f"{player_name} busts! [{value}]\n")

    def display_empty_deck(self):
        """ "Display a message when the deck is empty."""
        print_typewriter("Deck is empty. Shuffling...\n")

    def display_start(self):
        """ "Display the start of the game."""
        print("Do you wish to start a new game? (y/n)", end=" ")

    def display_game_over(self):
        """ "Display the end of the game."""
        print_typewriter("Game over!\n")
        print_typewriter("Do you wish to play again?")

    def display_invalid_input(self):
        """ "Display a message for invalid input."""
        print_typewriter("Invalid input. Please try again.\n")

    def display_hand_concealed(self, card):
        """Display the concealed hand (dealer's first card)."""
        print_typewriter(f"Dealer is drawing...")
        animate_symbols()
        print_with_delay(f"Dealer drew: ")
        print_with_delay(f"{card}")
        print_with_delay(" ? ")
        print_with_delay(f"→ [{calc_value_of_card(card)}]\n")

    def display_concealed_hand_text(self, card):
        """ "Display the dealer's concealed hand."""
        # Add flair to the dealer’s name and concealment with dashes
        print_typewriter(f"{"-" * 10} Dealer {"-" * 10}", False)

        # Show the first card with the concealed second card
        print_typewriter(f"\n{card} | [?]  →  [{calc_value_of_card(card)}]")

    def display_start_game(self, player_name, bet):
        """ "Display the start of the game."""
        print_typewriter(f"{player_name} has placed a bet of {int(bet)} DKK.")
        print_typewriter("Starting new game...", False)
        time.sleep(0.5)

        print_typewriter(" Shuffling deck...", True)
        time.sleep(0.5)
        print_typewriter("The game has begun!")
        time.sleep(1)
        print()

    def reveal_card(self, hand):
        """ "Reveal the dealer's second card."""
        print_typewriter("Dealer is revealing their second card...")
        value = 0
        if len(hand.cards) == 3:
            value = calc_value_of_card(hand.cards[2])

        print_with_delay(
            f" {hand.cards[0]} [{hand.cards[1]}] → [{hand.value - value}] ", end="\n"
        )
