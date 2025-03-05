from models.Hand import Hand
from models.Enums import Action
from models.TurnResult import TurnResult
from utils import handle_finished_or_blackjack, has_blackjack, is_bust


class Player():
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()
        self.action = Action.START
        self.turns = 0

    def hit(self, card):
        action = Action.HIT
        self.turns += 1
        self.hand.add_card(card)
        
        if is_bust(self.hand.value):
            action = Action.BUST
        
        if has_blackjack(self.hand.value):
            action = Action.STAND
            
        self.action = action
        return TurnResult(self.name, action, self.hand, card)

    def stand(self):
        self.turns += 1        
        self.action = Action.STAND

    def take_turn(self, card, card2=None):    
        if self.hand.value == 0:
            cards = []
            cards.append(card)
            cards.append(card2)
            self.hand.add_cards(cards)
            return TurnResult(self.name, Action.START, self.hand, cards=cards)
        
        if self.action == Action.STAND:
            return
            
        input = self.receive_input()    

        if input == Action.HIT:
            result = self.hit(card)
            
            if is_bust(result.hand.value):
                return TurnResult(self.name, Action.BUST, result.hand)
            
            return result

        if input == Action.STAND:
            self.stand()
            return TurnResult(self.name, Action.STAND, self.hand)

    def receive_input(self):
        if self.hand.value == 0:
            action = input(f'To begin please hit: ').strip().lower()

        else:
            action = input(f'\nDo you want to hit or stand?').strip().lower()

        if action == 'h' or action == 'hit' or 'hit' in action or action == '':
            return Action.HIT

        if action == 's' or action == 'stand' or 'stand' in action:
            return Action.STAND

        else:
            print('Invalid input. Please try again.')
            self.receive_input()


class Dealer(Player):
    def __init__(self):
        super().__init__('Dealer')
        self.action = Action.START

    def start_game(self, cards):
        self.hand.add_cards(cards)
        self.turns += 1
        action = Action.START
        
        if has_blackjack(self.hand.value) or self.hand.value >= 17:
            action = Action.STAND       
        
        self.action = action
        return TurnResult(self.name, action, self.hand, cards=cards)

    def take_turn(self, card, card2=None):
        if self.hand.value == 0:
            cards = []
            cards.append(card)
            cards.append(card2)
            self.hand.add_cards(cards)
            return TurnResult(self.name, Action.START, self.hand, cards=cards)
        
        if self.action == Action.STAND:
            return
        
        action = self.determine_action()

        if action == Action.HIT:
            result = self.hit(card)
            action = result.action
    
        if action == Action.STAND:
            action = Action.STAND
            self.stand()
            
        self.action = action
        return TurnResult(self.name, action, self.hand)

    def determine_action(self):
        action = self.action
        
        if is_bust(self.hand.value):
            return Action.BUST
        
        if self.hand.value < 17:
            action = Action.HIT
        
        else:    
            action = Action.STAND        
        
        return action
