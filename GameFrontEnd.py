from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
from Backend import Backend

LARGE_FONT= ("Ariel", 12)

optionlist_size = {'Small':5, 'Medium':10, 'Large':15}
optionlist_level = {'Easy':0.8, 'Medium':0.7, 'Hard':0.6}
canvas_row_dict = {'Small': (10, 15), "Medium": (7, 17), "Large": (5, 20)}
canvas_col_dict = {'Small': (6, 11), "Medium": (4, 14), "Large": (1, 16)}

class GameFrontEnd:

    def __init__(self, master):
        self.master = master
        master.configure(bg = 'pink')
        master.title("Have Fun at Nonograming")
        self.game_size = 5
        self.game_diff = 0.8
        self.marker = None
        self.canvas_row = (10, 15)
        self.canvas_col = (6, 11)
        self.player_board = np.empty((self.game_size, self.game_size))
        self.button_list = list()
        self.frame_list = list()
        self.header_list = list()
        self.answer_board = None

        def click_sunken(button1, button2):
            button_value = {frame1.button3:1, frame1.button4:0}
            button1.config(relief = SUNKEN, width = 5)
            button2.config(relief = RAISED, width = 3)
            self.marker = button_value[button1]

        def select_size(*args):
            size = frame1.option_size.get()
            self.game_size = optionlist_size[size]
            self.canvas_row = canvas_row_dict[size]
            self.canvas_col = canvas_col_dict[size]
            self.player_board = np.empty((self.game_size, self.game_size))

        def select_level(*args):
            self.game_diff = optionlist_level[frame1.option_level.get()]

        def onClick(row, col):
            self.player_board[row,col] = self.marker
            if self.marker == 1:
                self.button_list[row][col].config(bg = "navy")
            elif self.marker == 0:
                self.button_list[row][col].config(bg = "light grey")
            else:
                pass

        def generate_board():
            row = 0
            col = 0
            width_dict = {5: 70, 10: 70, 15: 70}
            for i in range(self.canvas_row[0], self.canvas_row[1]):
                col = 0
                self.button_list.append(list())
                self.frame_list.append(list())
                for j in range(self.canvas_col[0], self.canvas_col[1]):
                    frame = Frame(master, width = width_dict[self.game_size], height = width_dict[self.game_size], highlightbackground = 'black', highlightthickness = 1, bd = 0)
                    button = Button(frame, text = "", bg = 'white', command=lambda idx = row, idy = col: onClick(idx, idy))
                    button.configure(relief = FLAT)
                    frame.grid_propagate(False)
                    frame.columnconfigure(0, weight = 1)
                    frame.rowconfigure(0, weight = 1)
                    frame.grid(row = i, column = j)
                    button.grid(sticky = 'wens')
                    self.frame_list[row].append(frame)
                    self.button_list[row].append(button)
                    col += 1
                row += 1
        
        def add_header():
            c = Backend(self.game_size, self.game_diff)
            c.generate_header()
            self.answer_board = c.my_matrix
            j = self.canvas_row[0]
            h = self.canvas_col[0]
            for i in range(self.game_size): 
                label1 = Label(master, text = c.row_header[i], bg = 'pink')
                label1.grid(row = j, column = self.canvas_col[0]-1)
                label2 = Label(master, text = c.column_header[i], bg = 'pink', anchor = N)
                label2.grid(row = self.canvas_row[0]-1, column = h)
                self.header_list.append(label1)
                self.header_list.append(label2)
                j += 1
                h += 1

        def reset_user_board():
            self.player_board[:] = np.nan
            for i in self.frame_list:
                for j in i:
                    j.grid_remove()
            for i in self.header_list:
                i.grid_remove()
            self.button_list = list()
            self.frame_list = list()
            self.header_list = list()

        def start_game():
            reset_user_board()
            generate_board()
            add_header()

        def check_command():
            if (self.answer_board == self.player_board).all() or (self.answer_board == np.nan_to_num(self.player_board, nan=0)).all():
                messagebox.showinfo(title = "Congratulations!", message = "Yay! You won!")
                result = messagebox.askyesnocancel(title = "What's Next?", message = "Do you want to start a new game?")
                if result == True:
                    start_game()
                elif result == False:
                    master.destroy()
                else:
                    pass
            else:
                messagebox.showinfo(title = "Oops", message = "Oops! Something is wrong...Check your answer?")

        # Interface
        label = Label(master, text = "Welcome to my Nonogram Game!", font = LARGE_FONT, bg = 'pink')
        label.grid(row = 0, column = 2, columnspan = 12)

        frame1 = Frame(master, bg = 'pink')
        frame1.grid(row = 1, column = 1, columnspan = 15, rowspan = 3)

        frame1.label1 = Label(frame1, text = "Select Size")
        frame1.label1.configure(width = 8, bg = 'pink')
        frame1.label1.grid(row = 1, column = 1, rowspan = 1, columnspan = 3, sticky = 'wens')

        frame1.option_size = StringVar(frame1)
        frame1.option_size.set(list(optionlist_size.keys())[0])
        frame1.option1 = OptionMenu(frame1, frame1.option_size, *list(optionlist_size.keys()))
        frame1.option1.config(width = 8, fg = 'black', bg = 'white')
        frame1.option1.grid(row = 1, column = 4, rowspan = 1, columnspan = 3, sticky = 'wens')
        frame1.option_size.trace('w', select_size)

        frame1.label2 = Label(frame1, text = "Select Level")
        frame1.label2.configure(width = 8, bg = 'pink')
        frame1.label2.grid(row = 1, column = 7, rowspan = 1, columnspan = 3, sticky = 'wens')

        frame1.option_level = StringVar(frame1)
        frame1.option_level.set(list(optionlist_level.keys())[0])
        frame1.option2 = OptionMenu(frame1, frame1.option_level, *list(optionlist_level.keys()))
        frame1.option2.config(width = 8, fg = 'black', bg = 'white')
        frame1.option2.grid(row = 1, column = 10, rowspan = 1, columnspan = 3)
        frame1.option_level.trace('w', select_level)

        frame1.button1 = Button(frame1, text = "Start Game", command = start_game)
        frame1.button1.configure(width = 12)
        frame1.button1.grid(row = 2, column = 4, rowspan = 1, columnspan = 3, sticky = NW, pady = 0)

        frame1.button2 = Button(frame1, text = "Check Answer", command = check_command)
        frame1.button2.configure(width = 12)
        frame1.button2.grid(row = 2, column = 7, rowspan = 1, columnspan = 3, sticky = NW, pady = 0)

        frame1.button3 = Button(frame1, bg = 'navy', command = lambda: click_sunken(frame1.button3, frame1.button4))
        frame1.button3.configure(width = 4, height = 2)
        frame1.button3.grid(row = 3, column = 6)
   
        frame1.button4 = Button(frame1, bg = 'light grey', command = lambda: click_sunken(frame1.button4, frame1.button3))
        frame1.button4.configure(width = 4, height = 2)
        frame1.button4.grid(row = 3, column = 7)

root = Tk()
game = GameFrontEnd(root)
root.mainloop()

    






