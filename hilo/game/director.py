from dealer import Dealer
from player import Player
class Director:
    '''
    The director is responsible for managing the deck, player and dealer.
    The director is where the gameplay loop takes place.
    The Director tracks the players score.
    '''

    def get_num_players(Self):
        while True:
            try: 
                num_players = int(input("Number of players: "))
                if(num_players < 1):
                    raise RuntimeError("Invalid input")
                return num_players
            except Exception as e:
                print("Please enter a whole number above 0")

    def get_max_rounds(Self):
        while True:
            try: 
                max_rounds = int(input("Max rounds (0 for no max): "))
                if(max_rounds < 1):
                    raise RuntimeError("Invalid input")
                return max_rounds
            except Exception as e:
                print("Please enter a whole number above 0")

    def __init__(Self):
        Self.num_players = Self.get_num_players()
        Self.players = []
        for player in range(Self.num_players):
            name = "player " + str(player)
            Self.players.append(Player(name, 0))
        Self.max_rounds = Self.get_max_rounds()
        Self.round = 0
        Self.dealer = Dealer()
        Self.guesses = [False] * Self.num_players

    def update_guesses(Self):
        for player in range(Self.num_players):
            if Self.players[player].get_is_playing():
                #I'm doing it like this so that we don't allocate a new list every turn
                Self.guesses[player] = Self.players[player].promt_guess()
    
    def update_scores(Self, last_card, next_card):
        results = [False] * Self.num_players
        for player in range(Self.num_players):
            if Self.players[player].get_is_playing():
                # If they guessed that it would be higher Self.guesses would be true and last_card would be less then next card
                results[player] = Self.guesses[player] == last_card < next_card

        for player in range(Self.num_players):
            if Self.players[player].get_is_playing():
                points = 0
                if results[player]:
                    points = 100
                else:
                    points = -75
                Self.players[player].add_points(points)

    def display_scores(Self):
        print("Scores: ")
        for player in Self.players:
            print(player.get_name(), "'s score is: ", player.get_score())
    
    def ask_still_playing(Self):
        for player in Self.players:
            player.prompt_contiune()
            

    
    def play(Self):
        Self.playing = True
        while Self.playing:
            last_card = Self.dealer.get_last_card()
            print("The card is: ", last_card)
            
            Self.update_guesses()
            
            next_card = Self.dealer.draw_card()
            print("Next card was: ", next_card)

            Self.update_scores(last_card, next_card)
            Self.display_scores()

            # TODO: Add check to drop out players that score drops below 0

            Self.ask_still_playing()
            
            # TODO: Add check to see if a player has won and end the game if they have

            Self.round += 1





