import random
class Dealer:
    '''
    Represents the dealer in the game.
    Responsible for drawing a card and showing it.
    Responsible for showing the current card.
    Attributes: last_card, current_card
    '''
    def __init__(self):
        self.last_card = random.randint(1,13)
        self.current_card = self.last_card
    def draw_card(self):
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)
        return self.current_card
    def get_last_card(self):
        return self.last_card
    def get_next_card(self):
        return self.current_card