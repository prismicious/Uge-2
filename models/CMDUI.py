from models.Enums import Action
from models.TurnResult import TurnResult


class CMDUI():        
    def display_hand(player_name, hand):
        print(f'{player_name}\'s hand:')
        for card in hand.cards:
            print(card)
        print(f'Value: {hand.value}')
        
    def display_result(self, result: TurnResult):
        if result.action == Action.START:
            self.display_draw_multiple(result.player_name, result.cards, result.hand)
            return
            
        if result.action == Action.HIT:
            self.display_draw(result.player_name, result.card, result.hand)
            return
            
        if result.action == Action.STAND:
            self.display_stand(result.player_name, result.hand)
            return
        
    def display_game_state(self, player_name, player_hand, dealer_name, dealer_hand):
        self.display_hand(player_name, player_hand)
        self.display_hand(dealer_name, dealer_hand)
    
    def display_draw(self, player_name, card, hand):
        print(f"{player_name} has decided to hit and drew {card}\n")
        print(f"Value: {hand.value}\n")
    
    def display_stand(self, player_name, hand):
        print(f"{player_name} has decided to stand!\n")
        print(f"Value: {hand.value}\n")
    
    def display_draw_multiple(self, player_name, cards, hand):
        print(f'{player_name} drew:')
        for card in cards:
            print(f" {card} ")
        print(f"Value: {hand.value}\n")
        
    def display_winner(self, player_name):
        print(f'{player_name} wins!\n')
        
    def display_bust(self, player):
        print(f'{player.name} busts!\n')
        
    def display_empty_deck(self):
        print('Deck is empty. Shuffling...\n')
        
    def display_turn(self, player):
        print(f'It is {player.name}\'s turn...\n')
        
    def display_start(self, name):
        print(f'Welcome to Blackjack {name}!\n')
        print('Do you wish to start a new game? (y/n)')
        
    def display_game_over(self):
        print('Game over!\n')
        print('Do you wish to play again?')
        
    def display_invalid_input(self):
        print('Invalid input. Please try again.\n')