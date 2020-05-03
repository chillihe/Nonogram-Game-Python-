
######################################################################
## Project Name: Nonogram Game
## Date: 04/01/2020
######################################################################

from Board import Board
from UserInteractionHandler import UserInteractionHandler

class GameManager():

    def __init__(self):
        self.board = Board()
        self.user =  UserInteractionHandler()

    # Generate the game board
    def generate_game_board(self):

        # Game settings
        g = self.user.reset_or_not()
        if g == True:
            self.user.reset_game_size()
            self.user.reset_game_level()
            self.board.set_game_size(self.user.game_size)
            self.board.set_game_level(self.user.game_level)

        # Reset the user Matrix to be all Nan
        self.board.reset_user_board()

        # Print the empty game board
        self.board.print_user_board()
        print(self.board.my_matrix)
    
    # Start to play the game
    def start_the_game(self):

        while True:
            solution_one_counts = Board.one_counts(self.board.my_matrix)
            user_one_counts = Board.one_counts(self.board.user_matrix)

            if solution_one_counts == user_one_counts:
                print('You Won!')
                break
            elif self.board.wrong_move > 5:
                print('You lost!')
                break
            else:
                m = self.user.make_a_move()
                if self.board.move_valid_or_not(m):
                    self.board.verify_user_board(m)
                    print('\n'*100)
                    print("{} chance(s) left!".format((5-self.board.wrong_move)))
                    print('\n')
                    self.board.print_user_board()
                else:
                    print("Please select an empty cell.")
                    continue
    

gm = GameManager()
gm.generate_game_board()
gm.start_the_game()