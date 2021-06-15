import random
class Dealer:
    '''
    Represents the dealer in the game.
    Responsible for drawing a card and showing it.
    Responsible for showing the current card.
    Attributes: last_card, current_card
    '''
    def __init__(self):
        #Initializes the last card and sets current card equal to it
        self.last_card = random.randint(1,13)
        self.current_card = self.last_card
    def draw_card(self):
        #Sets the last card to the current card, and then draws a new random card.
        self.last_card = self.current_card
        self.current_card = random.randint(1,13)
    def get_last_card(self):
        #Returns the last card
        return self.last_card
    def get_next_card(self):
        #Returns the current or "next" card
        return self.current_card