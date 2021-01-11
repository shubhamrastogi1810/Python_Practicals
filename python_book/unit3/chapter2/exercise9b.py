""" This is a lab exercise of python book example 9b. """
# This is a program to display a tic-tac-toe board on screen using variables,
# so that you don't need to write many print statements.
def draw_board():
    """ This function will draw a borad of tic-tac-toe using variable."""
    for i in range(1,5):
        if i% 2 == 1:
            print("__|__|__")
        else:
            print("  |  |  ")
draw_board()
