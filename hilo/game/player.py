"""
Author: Dallin Poole
Date: June 15 2021
Last Updated By: Dallin Poole, June 15 2021
"""

class Player:
    '''
    Represents the player in the game. 
    Responsible for parsing input from the user of high or low.
    Holds the score for the player.
    Score can be modified from outside.
    '''
    
    # Player's score
    score = None
    # Is the player still playing?
    is_playing = None
    # Is the player's guess high?
    guess_is_high = None
    # The player's name.
    name = ""

    """
    __init__
    Parameters: string name, int starting_score
    Description: Initializes the member attributes for this player
    and prepares them for gameplay.
    """
    def __init__(self, name, starting_score):
        self.is_playing = True
        self.name = name
        self.score = starting_score


    """
    prompt_guess
    Parameters: None
    Description: Gets input from the player on what their guess is.
    Doesn't ask players that have lost, or dropped out.
    """
    def prompt_guess(self):
        if (self.is_playing):
            self.guess_is_high = input(f"Player {self.name}, higher or lower? [h/l]: ").lower() == 'h'
        return self.guess_is_high        

    """
    prompt_guess
    Parameters: None
    Description: Asks players that are still playing if they still want to play.
    """
    def prompt_continue(self):
        if(self.is_playing): 
            self.is_playing = input(f"{self.name}, keep playing? [y/n]: ").lower() == 'y'
        return self.is_playing

    """
    get_score
    Parameters: None
    Description: Gets this player's score.
    """
    def get_score(self):
        return self.score

    """
    add_score
    Parameters: int points
    Description: Adds the value of points to the player's score.
    If the player's score <= 0, they can't keep playing.
    """
    def add_score(self, points):
        if (not self.is_playing):
            return
            
        self.score += points
        if (self.score <= 0):
            self.is_playing = False
            print(f"Player {self.name}, you ran out of points!")

    """
    get_guess
    Parameters: None
    Description: Gets if the player's current guess is high.
    """
    def get_guess(self):
        return self.guess_is_high

    """
    get_name
    Parameters: None
    Description: Gets the player's name.
    """
    def get_name(self):
        return self.name

    """
    get_is_playing
    Parameters: None
    Description: Gets if the player is still playing.
    """
    def get_is_playing(self):
        return self.is_playing
