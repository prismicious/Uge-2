from models.Game import Game

def main():
    start_game()
    
def start_game():
            
    game = Game("Player")  # Use the entered name for the game
    game.deal()

if __name__ == '__main__':
    start_game()  # Call the start_game function to initiate the game