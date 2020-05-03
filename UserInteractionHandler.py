
class UserInteractionHandler():

    def __init__(self, game_size=5, game_level=0.7):
        self.game_size = game_size
        self.game_level = game_level

    # If user wants to reset the game setting (level & size) or not => output: a boolean
    def reset_or_not(self):
        while True:
            value = input('Do you want to reset the game size and difficulty level? Please enter "y" or "n".')
            if value.lower() in ['y', 'n']:
                if value.lower() == 'y':
                    return True
                else:
                    return False
                break
            else:
                print("Please enter 'y' or 'n'.")

    # User input for the size of the Nonogram, 5, 10, or 15
    def reset_game_size(self):
        '''
        This function asks for an input from the user, which can only be an integer of 5, 10, or 15. 
        It will be used as size of the Nonogram game. 
        For example, if the user enters 5, then the game will be a 5 * 5 game.
        '''
        while True:
            game_dim = input('How large do you want your Nonogram? Please enter 5, 10, or 15. ')
            try:
                game_dim = int(game_dim)
                if game_dim in [5, 10, 15]:
                    self.game_size = game_dim
                    break
                else:
                    print('Please enter a valid integer: 5, 10, or 15.')
                    continue
            except ValueError:
                print('Please enter a valid integer: 5, 10, or 15.')
                continue
        
    # User input for for the difficulty level of the game, Level 1 (easiest) to 3 (hardest)
    def reset_game_level(self):
        '''
        This function asks for an input from the user, which can only be an integer of 1, 2, or 3. 
        It will determine the difficulty level of the game. 1 is the easiest, and 3 is the hardest.
        It is associated with the proportion of 1s in the matrix.
        '''
        while True:
            my_dict = {1:0.8, 2:0.7, 3:0.6}
            level = input('Please enter the difficulty level: 1, 2, or 3. 1 is the easiest and 3 is the hardest. ')
            try:
                level = int(level)
                if level in [1, 2, 3]:
                    self.game_level = my_dict[level]
                    break
                else:
                    print('Please enter a valid integer: 1, 2, or 3.')
                    continue
            except ValueError:
                print('Please enter a valid integer: 1, 2, or 3.')

    #  Define a function that asks for a move from the user
    def make_a_move(self):
        
        # User puts in a move (rnum, cnum, and value (1 or 0))
        move_dict = {'Please enter a row number (from 1 to {})'.format(self.game_size): list(range(1,(self.game_size+1))),
                     'Please enter a column number (from 1 to {})'.format(self.game_size): list(range(1,(self.game_size+1))),
                     'Please enter a value (1 ot 0)': list(range(0,2))}
        user_move = list()

        for mess,input_range in move_dict.items():
            while True:
                value = input('{}'.format(mess))
                try:
                    value = int(value)
                    if value in input_range:
                        user_move.append(value)
                        break
                    else:
                        print('{}'.format(mess))
                        continue
                except:
                    print('Ooops, something went wrong! {}'.format(mess))
                    continue
    
        return user_move
