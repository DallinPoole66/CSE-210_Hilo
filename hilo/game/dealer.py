import random
class Dealer:
    '''
    Represents the dealer in the game.
    Responsible for drawing a card and showing it.
    Responsible for showing the current card.
    Attributes: last_card 
    '''
    def __init__(self):
        self.last_card = random.randint(1,13)
    def draw_card(self):
        card = random.randint(1,13)
        return card