"""A Python script that attempts to replicate Conway's Game of Life.

..  module:: Game_of_life.py
    :platform: Windows, Mac, Unix
    :synopsis: This script will displays the evolution of cells on a 30 row by 80 column grid.
        The user will input how many generations it wishes the game to run for. In the same input line.
         the user will specify the cells it wishes to be turned "on" at the start of the game. Once the the user inputs
         the values correctly, the game will begin and run on its own. The rules and explanation of the functions
         will be included as you progress through this script.

..  moduleauthors: Joshua Freimark and Evan Stowe, Joshua.freimark@wsu.edu.
..  modulereviewer: Harrison.
..  reviewergrade:
"""
from sys import argv

def initiate_grid(seeds):
    """
    Create the initial grid and define its dimmensions.
    :param seeds: Int - The coordinates on the grid that start the game as on cells.
    :variable grid: Dict - Creates an empty dictonary.
    :return: Dict of Int -  grid of '-' is returned.
    """
    grid = {}
    for r in range(1, 31):
        for c in range(1, 81):
            #Populate the grid with '-' cells which denotes that cell is turned off.
            grid[r,c] = "-"
    #Loop through seeds and insert a "X" in the r,c which denotes the cell is turned on.
    for r,c in seeds:
        grid[r,c] = 'X'
    return grid

def display(grid):
    """
    The display function recieves the grid dictionary and prints the grid to the terminal.
    :param grid: dict - The dictionary that is used as the game of life grid display.
    """
    for r in range(1, 31):
        #Set grid_row as empty string variable
        grid_row = ''
        for c in range(1,81):
            grid_row = grid_row + grid[r,c]   #Concatinates all the cells in a row.
        print(grid_row)   #Once we have the entire row, it is then printed.

def game_rules(r, c, grid):
    """ This function defines the rules of the game.
    :param r: Int - Row coordinate value.
    :param c: Int - Column coordinate value.
    :param grid: Dict - stores the values of the rows and columns.
    """
    #Use boolean logic to determine if cells are on "X", or off  "-". Initial state is set to '-'' for all cells.
    cell_state = 0
    #n is the sum of live neighbors.
    n = find_neighbors(r, c, grid)
    #Rule A. Any “on” cell with two or three “on” neighbors remains “on”.
    if grid[r,c] == "X" and n < 2:
        cell_state = 0
    #Rule B. Any “on” cell with two or three “on” neighbors remains “on”.
    elif grid[r,c] == "X" and (n == 2 or n == 3):
        cell_state = 1
    #Rule C. Any “on” cell with more than three “on” neighbors is turned “off”.
    elif grid[r,c] == "X" and n > 3:
        cell_state = 0
    #Rule D. Any “off” cell with exactly three live neighbors is turned “on”.
    if grid[r,c] == "-" and n == 3:
        cell_state = 1
    return "X" if cell_state == 1 else '-'

def find_neighbors(r, c, grid):
    """
    Finds the live neighbors for each cell.
    :param r: Int - Row coordinate to be observed.
    :param c: Int - Column coordinate to be observed.
    :param grid: Dict of Int - Values of the rows and columns to be stored in the grid dictionary.
    """
    neighbors = call_neighbors(r, c)
    #Start with 0 on neighbor cells.
    on_neighbors = 0
    for x in neighbors:
        if grid[x] =="X":
            on_neighbors += 1
    return on_neighbors

def call_neighbors(r,c):
    """
    for a cell r,c the neighbors will be represented as :

            c-1         c
    r-1    (r-1,c-1)   (r-1, c)   (r-1, c+1)
    r       (r, c-1)    (r,c)      (r, c+1)
    r+1    (r+1, c-1)  (r+1, c)   (r+1, c+1)

    We need to check if each of the neighbors lies within the grid limits.
    i.e. column and row should be always greater than or equal to 1.
    Column should be less than or equal to 80.
    Row should be less than or equal to 30.

    :param r: Int - Row coordinate
    :param c: Int - Column coordinate
    :return: tuple of cell neighbors
    """
    max_row = 31
    max_col = 81
    neighbors = []
    if r-1 >= 1:
        neighbors.append((r-1, c))
    if r-1 >= 1 and c-1 >= 1:
        neighbors.append((r-1, c-1))
    if r-1 >= 1 and c+1 < max_col:
        neighbors.append((r-1, c+1))
    if c-1 >= 1:
        neighbors.append((r, c-1))
    if c-1 >= 1 and r+1 < max_row:
        neighbors.append((r+1, c-1))
    if c+1 < max_col:
        neighbors.append((r, c+1))
    if r+1 < max_row:
        neighbors.append((r+1, c))
    if c+1 < max_col and r+1 < max_row:
        neighbors.append((r+1, c+1))

    return neighbors

def new_grid(grid):
    """
    new_grid creates an empty dictionary for the next generation. It then calculates the cell values
    for the next generation which is based on the current generation's grid.
    :param grid: Dict - Dictionary of values of the rows and columns to be stored in the grid dictionary.
    """
    next_gen = {}
    for r in range(1, 31):
        for c in range(1,81):
            #game_rules provides what the next generation's value of the cells should be.
            next_gen[r,c] = game_rules(r, c, grid)
    return next_gen

def translate_input(input_string):
    """
    Accepts user input and converts it to an integer and stores it in list.
    translate_input will recieve input from the user and convert it to an internger.
    :param ticks: Int - The number of generations the game will run.
    :param user_input: String - The number of row:column the user wishes to turn on in the first generation.
    """
    #This will split the user inputs with a single space.
    user_inputs = input_string.split()
    # The first object of the user_inputs will be the generations and it is seperated from the remaining input.
    generations = (int(user_inputs[0]))
    # The remaining input values will be used to display the on cells on the grid.
    user_inputs = user_inputs[1:]
    # user_seeds is an empty list for now.
    user_seeds = []
    for user_input in user_inputs:
        #The row and column will be split by a colon character ":".
        row_string, column_string = user_input.split(":")
         #Convert row_string and column_string to integers and append them to the user_seed list.
        user_seeds.append((int(row_string), int(column_string)))
        # returns the generations as well as the location of user_seeds in row-column format.

    return generations, user_seeds

def input_function():
    """Will accept user input and display the output on the grid in the terminal"""
    print("Input an integer for the number of generations for the game to run.")
    print("In the same line, seperated by a space, input the coordinates of the grid")
    print("that you want to start as on cells. Use the format row:column.")
    print("Row range: 1-30")
    print("Column range: 1-80")
    print("\n")
    print("Example:10 14:40 15:42")
    #User will input the number of generations for the game to run.
    generations_user_seeds = input(">")
    #Splits the user input into generations and coordinates.
    generations, coordinate = translate_input(generations_user_seeds)
    Show_grid = initiate_grid(coordinate)
    display(Show_grid)
    while generations > 1:
        #Decrease the number of generations by 1 while the game is operating.
        generations -= 1
        # Print 2 empty lines in between the generations.
        print()
        print()
        Show_grid = new_grid(Show_grid)
        display(Show_grid)

input_function()
