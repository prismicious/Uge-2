import os
import pickle
import random
import time

from dotenv import load_dotenv
from models.Enums import Action
from models.TurnResult import TurnResult

load_dotenv()

typewriter_delay = float(os.getenv("TYPEWRITER_DELAY", 0.1))
print_delay = int(os.getenv("PRINT_DELAY", 1))


def handle_finished_or_blackjack(name, action, hand):
    if action == Action.STAND or has_blackjack(hand.value):
        return TurnResult(name, Action.STAND, hand)


def has_blackjack(value):
    return value == 21


def is_bust(value):
    return value > 21

def calc_value_of_card(card):
    """Calculate the value of a single card in Blackjack."""
    if card.rank.isdigit():  # Works for numbers '2'-'10'
        return int(card.rank)
    elif card.rank in {"J", "Q", "K"}:
        return 10
    elif card.rank == "A":
        return 11  # Aces should be counted as 11 initially

def sleep(delay):
    time.sleep(delay)


def print_with_delay(text, end="", overwrite=False):
    
    if overwrite:
        print("\r", end="", flush=True)

    """Helper function to print with delay."""
    print(text, end=end, flush=True)
    sleep(print_delay)


def print_typewriter(text, newline=True, delay=typewriter_delay, overwrite=False):
    """Print each letter one at a time with a delay to simulate typing effect."""
    if overwrite:
        print("\r", end="", flush=True)  # Move to the start of the line to overwrite

    
    for letter in text:
        print(letter, end="", flush=True)
        sleep(delay)

    if not newline:
        return

    print()

def animate_symbols():
    
    symbols = ['♥', '♦', '♣', '♠', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    """Animate the random changing of symbols."""
    for _ in range(5):  # Number of times to shuffle the symbols
        random.shuffle(symbols)  # Shuffle the symbols randomly
        displayed_symbols = " ".join(symbols[:5])  # Display only the first 5 symbols
        print(displayed_symbols, end="\r", flush=True)  # Print symbols in random order
        time.sleep(0.2)  # Adjust speed of the shuffle effect


def save_player_to_pickle(player, filename='player.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(player, file)
        
def load_player_from_pickle(filename='player.pkl'):
    with open(filename, 'rb') as file:
        return pickle.load(file)
   
            