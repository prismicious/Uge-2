from models.Hand import Hand
from models.Enums import Action 
from models.TurnResult import TurnResult

class Player():
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.action = None
        self.turns = 0
        self.final_value = 0
        
    def hit(self, card):            
        self.action = Action.HIT
        self.turns += 1
        self.hand.add_card(card)
        
        return TurnResult(self.name, Action.HIT, self.hand, card)
    
    def stand(self):
        self.turns += 1
        self.action = Action.STAND
        self.final_value = self.hand.value
        
        return TurnResult(self.name, Action.STAND, self.hand, None)
        
    def take_turn(self, card):
        if self.action == Action.STAND:
            return TurnResult(self.name, Action.STAND, self.hand)
        
        input = self.receive_input()
        
        if input == Action.HIT:
            result = self.hit(card)
            return result
        
        if input == Action.STAND:
            result = self.stand()
            return result
            
    def receive_input(self):
        if self.hand.value == 0:
            action = input(f'To begin please hit: ').strip().lower()
        
        else:
            action = input(f'Current value: {self.hand.value}. Do you want to hit or stand?').strip().lower()
            
        if action == 'h' or action == 'hit' or 'hit' in action:
            return Action.HIT
        
        if action == 's' or action == 'stand' or 'stand' in action:
            return Action.STAND

        else:
            print('Invalid input. Please try again.')
            self.receive_input()

class Dealer(Player):
    def __init__(self):
        super().__init__('Dealer')

    def start_game(self, cards):
        self.hand.add_cards(cards)
        self.turns += 1
        return TurnResult(self.name, Action.START, self.hand, cards=cards)
        
    def take_turn(self, card):
        action = self.determine_action()
        
        if action == Action.HIT:
            self.hit(card)
            return TurnResult(self.name, Action.HIT, self.hand, card)
            
        else: 
            self.stand()     
            return TurnResult(self.name, Action.STAND, self.hand)
        
    
    def determine_action(self):
        if self.hand.value < 17:
            return Action.HIT
        
        return Action.STAND
