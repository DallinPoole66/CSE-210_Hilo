'''
This is the entry point for the program. This is where the initial state of the game
is set up and put into motion.
'''

from game.director import Director


'''
Program Entry Point
'''
def main():
    # Initialize needed classes
    director = Director()

    # Start Game
    director.play()

if __name__ == "__main__":
    main()