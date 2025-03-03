from models.Game import Game

def main():
    start_game()
    
def start_game():
    #print("Welcome what is your name?")
    #name = input().strip().lower()
    game: Game = Game("Test")
    game.deal()
    
if __name__ == '__main__':
    main()