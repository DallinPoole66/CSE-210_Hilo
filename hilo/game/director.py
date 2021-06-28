from game.dealer import Dealer
from game.player import Player
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
                if(max_rounds < 0):
                    raise RuntimeError("Invalid input")
                return max_rounds
            except Exception as e:
                print("Please enter a whole number above 0")

    def __init__(Self):
        Self.num_players = Self.get_num_players()
        Self.players = []
        for player in range(Self.num_players):
            name = "player " + str(player)
            Self.players.append(Player(name, 300))
        Self.max_rounds = Self.get_max_rounds()
        Self.round = 0
        Self.dealer = Dealer()
        Self.guesses = [False] * Self.num_players

    def update_guesses(Self):
        for player in range(Self.num_players):
            if Self.players[player].get_is_playing():
                #I'm doing it like this so that we don't allocate a new list every turn
                Self.guesses[player] = Self.players[player].prompt_guess()
    
    def update_scores(Self, last_card, next_card):
        results = [False] * Self.num_players
        for player in range(Self.num_players):
            if Self.players[player].get_is_playing():
                # If they guessed that it would be higher Self.guesses would be true and last_card would be less then next card
                results[player] = Self.guesses[player] == (last_card < next_card)

        for player in range(Self.num_players):
            if Self.players[player].get_is_playing():
                points = 0
                if results[player]:
                    points = 100
                else:
                    points = -75
                Self.players[player].add_score(points)

    def display_scores(Self):
        print("Scores: ")
        for player in Self.players:
            print(player.get_name(), "'s score is: ", player.get_score())
    
    def ask_still_playing(Self):
        for player in Self.players:
            player.prompt_continue()
            

    
    def play(Self):
        Self.playing = True
        while Self.playing:
            Self.round += 1
            last_card = Self.dealer.get_last_card()
            print("The card is: ", last_card)
            
            Self.update_guesses()
            
            Self.dealer.draw_card()
            next_card = Self.dealer.get_next_card()
            print("Next card was: ", next_card)

            Self.update_scores(last_card, next_card)
            Self.display_scores()

            Self.ask_still_playing()
            
            active_players = 0
            for player in Self.players:
                if player.get_is_playing():
                    active_players += 1
            if active_players < 1 or (Self.max_rounds != 0 and Self.max_rounds == Self.round):
                Self.playing = False
        print("Game Over!")
        # If we did not stop due to max_rounds then there is only one player left, 
        # so find that one player and display their name
        if not (Self.max_rounds != 0 and Self.max_rounds == Self.round):
            for player in Self.players:
                if player.get_is_playing():
                    print(player.get_name(), " Won!")
                    break
        # Display the final scores
        print("\nFinal ", end="")
        Self.display_scores()





