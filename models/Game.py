import os
from dotenv import load_dotenv
import time
from models.CMDUI import CMDUI
from models.Deck import Deck
from models.Enums import Action
from models.Hand import Hand
from models.Player import Dealer, Player
from utils import load_player_from_pickle, save_player_to_pickle

load_dotenv()

turn_delay = os.getenv("TURN_DELAY", 1)

sleep_interval = 1

class Game:
    def __init__(self, name):
        self.deck = Deck()
        self.player = Player(name)
        self.dealer = Dealer()
        self.cmd = CMDUI()
        self.bet = 10

    def start_game(self):
        if not os.path.exists('player.pkl'):
            save_player_to_pickle(self.player)
        
        """Start the game by asking the user for input."""
        self.cmd.display_start(self.player.name)
        user_input = input().strip().lower()

        if user_input == "y":
            self.deal()
        elif user_input == "n":
            exit()
        else:
            self.cmd.display_invalid_input()

    def deal(self):
        self.player = load_player_from_pickle() if os.path.exists('player.pkl') else self.player
        if self.player.turns != 0:
            self.player.reset_player_object()
        
        if int(self.player.balance) <= 0:
            print("Looks like you lost all your money. I'm adding some more to your balance.")
            self.player.balance += 100
            save_player_to_pickle(self.player)
            self.deal()
            return
            
        print(f"How much do you wanna bet? balance: {self.player.balance} DKK")
        self.bet = input().strip()

        
        if self.bet == '':
            self.bet = '10'
            
        if not self.bet.isnumeric():
            print("Invalid input. Please enter a number.")
            self.deal()
            return
        
        if int(self.bet) > self.player.balance:
            print("You cannot bet more than your balance.")
            self.deal()
            return
        
        """Handles the initial card dealing and player/dealer turns."""
        self.handle_empty_deck()
        self.player.balance -= int(self.bet)
        self.cmd.display_start_game(self.player.name, self.bet)

        # Step 1: Dealer draws 2 cards (one concealed)
        dealer_start_result = self.dealer.take_turn(self.deck)  
        self.cmd.display_result(dealer_start_result)
        time.sleep(sleep_interval)

        # Step 2: Player draws 2 cards
        player_start_result = self.player.take_turn(self.deck)  
        self.cmd.display_result(player_start_result)
        time.sleep(sleep_interval)

        # Step 3: Player plays until stand or bust
        while self.player.action not in {Action.STAND, Action.BUST}:
            self.cmd.display_game_state(self.player, self.dealer)
            result = self.player.take_turn(self.deck)  
            self.cmd.display_result(result)
            time.sleep(sleep_interval)

        # Step 4: Only if player did not bust, the dealer takes their turn
        if self.player.action != Action.BUST:
            dealer_result = self.dealer.take_turn(self.deck)  
            self.cmd.display_result(dealer_result)

        # Step 5: Determine the winner
        self.check_game_over()

    def check_game_over(self):
        """Check if the game is over and determine the winner."""
        player_bust_or_stand = self.player.action in {Action.BUST, Action.STAND}
        dealer_bust_or_stand = self.dealer.action in {Action.BUST, Action.STAND}

        if player_bust_or_stand or dealer_bust_or_stand:
            winner = self.determine_winner(self.player.hand.value, self.dealer.hand.value)
            self.cmd.display_winner(winner)
            self.ask_play_again()
            return True

        return False

    def determine_winner(self, player_hand_value, dealer_hand_value):
        """Determine the winner based on the hand values."""
        
        bet_amount = int(self.bet)  # Convert once for efficiency

        # If player busts, dealer wins
        if self.player.action == Action.BUST:
            winner = self.dealer.name
            self.player.lost_bet(bet_amount)
            
        # If dealer busts or player has higher hand value, player wins
        elif self.dealer.action == Action.BUST or player_hand_value > dealer_hand_value:
            winner = self.player.name
            self.player.won_bet(bet_amount)

        # If dealer has higher hand value, dealer wins
        elif dealer_hand_value > player_hand_value:
            winner = self.dealer.name
            self.player.lost_bet(bet_amount)
        
        # Tie if both have the same hand value
        else:  
            winner = "Tie"
            self.player.balance += bet_amount  

        save_player_to_pickle(self.player)
        return winner

    def handle_empty_deck(self):
        """Handle case when the deck is empty."""
        if not self.deck.cards:
            self.deck = Deck()
            self.cmd.display_empty_deck()

    def ask_play_again(self):
        """Ask if the player wants to play again after the game is over."""
        user_input = input("Do you want to play again? (y/n): ").strip().lower()
        if user_input == "y" or user_input == "":
            self.reset_game()  # Reset the game state and start a new game
            self.deal()
        elif user_input == "n":
            print("Thank you for playing! Exiting the game.")
            exit()  # Exit the game
        else:
            print("Invalid input. Please enter 'y' to play again or 'n' to quit.")
            self.ask_play_again()  # Recursively ask until a valid input is given
            
    
    def reset_game(self):
        """Reset the game to its initial state."""
        self.deck = Deck()  
        self.player = Player(self.player.name) 
        self.dealer = Dealer()  