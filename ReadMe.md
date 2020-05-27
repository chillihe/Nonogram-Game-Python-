# Nonogram Game
This is a Nonograms game. Nonogram, which is also known as a Japanese crossword, is a puzzle and usually has a picture encoded in numbers. In this version of the Nonogram game, no picutre is embedded. 

There are three sizes of the game board (Easy: 5 * 5; Medium: 10 * 10; Hard: 15 * 15) and three difficulty levels (Easy, Medium, and Hard). After selecting the game size and level, users can click the **Start Game** button to play. There are two types of markers: navy and light gray. Based on the hints displayed vertically and horizontally besides the game board, users need to click all the buttons that are supposed to be navy. Then, users can click the **Check Answers** button to check if the answers are correct. If users successfully checked all the navy buttons, a congratulating message will be displayed, and users will be asked if they want to replay the game. If there is one or more mistakes in the answers, a warning message will be displayed and users can go back to revise their answers.

## Files in the Repo
Users can download **Backend.py** and **GameFrontEnd.py** and run the **GameFrontEnd.py**. A user interface will pop up and users can play the game. Alternatively, users can download the executable program in the **exe** folder and directly run the program on Windows. In the **Nonogram_RunOnPython** folder, there are python code that allows users to play the game on Python. The following third-party libraries / packages are used:
* Numpy

## How to play the game?
A detailed instructions on how to play the Nonogram game can be found on the [Nonograms website](https://www.nonograms.org/instructions). 

> Numbers, shown on the left and above the crossword – describe the groups of painted squares (which go in sequence, no blanks) horizontally and vertically accordingly. The order of these numbers describes the order of location of these groups, but it is unknown where each group starts and finishes (in fact it is the task of the puzzle to define their location). Each separate number means a separate group of the given size (i.e. number 5 – means a group of five painted squares in sequence, 1 – a group of only one painted square). In black and white crosswords we always paint the square black, in colour ones – we paint the square using the colour by which the number is marked. Between the groups of one colour there should be at least one unpainted square (otherwise they would make one group). Between groups of different colour there can be no empty squares.

