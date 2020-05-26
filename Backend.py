import numpy as np 
import numpy.random as random

class Backend():

    def __init__(self, game_size = 5, game_diff = 0.8):
        self.game_size = game_size
        self.game_diff = game_diff
        self.my_matrix = random.choice(2, (game_size * game_size), p=[(1-game_diff), game_diff]).reshape(game_size, game_size)
        self.row_header = list()
        self.column_header = list()

    @classmethod
    def gen_name(self, num_list):
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

    def generate_header(self):
        for i in self.my_matrix:
            self.row_header.append(self.gen_name(i))
        for i in self.my_matrix.transpose():
            self.column_header.append(self.gen_name(i))

    
        
        