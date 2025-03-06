from models.Game import Game

def main():
    start_game()
    
def start_game():
    
    """print("Welcome to BlackJack, what is your name?", end=" ")
    
    while True:  # Start an infinite loop to keep asking for a valid name
        name = input().strip().lower()

        if len(name) > 10:
            print("Name too long. Please enter a name less than 10 characters.")
        else:
            break  # Exit the loop if the name is valid (10 characters or less)"""
        
    game = Game("Player")  # Use the entered name for the game
    game.deal()

if __name__ == '__main__':
    start_game()  # Call the start_game function to initiate the game