
# Import the libraries
import numpy as np
import pandas as pd
import numpy.random as random
import matplotlib.pyplot as plt

# Define the class
class Board():

    # The game board get instantiated with a game level (10*10) and a difficulty level (Level 2)
    def __init__(self, game_size=5, game_level=0.7, wrong_move=0):
        self.game_size = game_size
        self.game_level = game_level
        self.wrong_move = wrong_move
        self.my_matrix = random.choice(2, (game_size * game_size), p=[(1-game_level), game_level]).reshape(game_size, game_size)
        self.user_matrix = np.empty((self.game_size, self.game_size))

    # Allow the user to reset the game board size
    def set_game_size(self, new_game_size):
        self.game_size = new_game_size
        self.my_matrix = random.choice(2, (self.game_size * self.game_size), p=[(1-self.game_level), self.game_level]).reshape(self.game_size, self.game_size)
        self.user_matrix = np.empty((self.game_size, self.game_size))
        
    # Allow the user to reset the difficulty level
    def set_game_level(self, new_game_level):
        self.game_level = new_game_level
        self.my_matrix = random.choice(2, (self.game_size * self.game_size), p=[(1-self.game_level), self.game_level]).reshape(self.game_size, self.game_size)
        self.user_matrix = np.empty((self.game_size, self.game_size))

    # Reset the user matrix to be all NaN
    def reset_user_board(self):
        self.user_matrix[:] = np.nan

    # Take in the user move (from UserInteractionHandler.py)
    # Verify the move.
    # If correct: Update the board with the move
    # If incorrect: Update the board with the correct answer, wrong move count + 1
    def verify_user_board(self, user_move):
        if user_move[2] == self.my_matrix[(user_move[0]-1),(user_move[1]-1)]:
            self.user_matrix[(user_move[0]-1),(user_move[1]-1)] = user_move[2]
            print("Correct!")
        else:
            self.user_matrix[(user_move[0]-1),(user_move[1]-1)] = 1 - user_move[2]
            self.wrong_move = self.wrong_move + 1
            print("Ooops! Wrong move. You have made {a} mistake(s) so far. {b} chances left.".format(a=self.wrong_move, b=(5-self.wrong_move)))
        
    # Verify if the cell of the move is taken -> output is a boolean
    def move_valid_or_not(self, user_move):
        if pd.isnull(self.user_matrix[(user_move[0]-1),(user_move[1]-1)]):
            return True
        else:
            return False

    # Check if all the "1"s  are found
    @classmethod
    def one_counts(self, one_matrix):
        return np.count_nonzero(one_matrix==1)

    # Convert the user matrix to a DataFrame and print out the game board
    def print_user_board(self):

        # Create a DataFrame for the Game Board
        df_solution = pd.DataFrame(data = self.my_matrix)
        df_user = pd.DataFrame(data=self.user_matrix)

        # Define a function to calculate the number of each block of consecutive 1s in each row and column
        def gen_name(num_list):
            '''
            Calculate the number of each block of consecutive 1s in each row and column.
            E.g., [1, 0, 0, 1, 1] will return [1, 2]
            '''
            my_dict = {0: list(), 1:list()}
            count = 0
            list_len = len(num_list)
            current_num = num_list[0]
            for i in range(list_len):
                if i != list_len - 1:
                    if num_list[i] == current_num:
                        count = count + 1
                    else:
                        my_dict[current_num].append(count)
                        current_num = num_list[i]
                        count = 1
                else:
                    if num_list[i] == current_num:
                        count = count + 1
                        my_dict[current_num].append(count)
                    else:
                        my_dict[current_num].append(count)
                        current_num = num_list[i]
                        my_dict[current_num].append(1)
            return str(my_dict[1])

        # Create the index name
        df_user.index = df_solution.apply(lambda x: gen_name(x), axis=1)

        # Creat the column name
        df_user.columns = df_solution.apply(lambda x: gen_name(x), axis=0)

        # Replace 1 with "O" (Square) and 0 with "" (empty)
        value_conv = {1:'O', 0:'X', np.nan: ''}
        df_user = df_user.apply(lambda x: x.map(value_conv), axis=1)

        # Return the Data Frame
        print(df_user)
        return df_user
