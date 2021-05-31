import random

grid_size = 4
num_mines = 2


def draw_user_grid(user_grid):
    '''
    Returns a string representation of the board.
    '''
    user_grid_str_rep = ""
    draw_top = "   "
    num_grid = "\n"
    for i in range(1, grid_size+1):
        draw_top += str(i) + "  "

    draw_horizontal_line = "\n"
    for _ in range(grid_size):
        draw_horizontal_line += "---"
    draw_horizontal_line += "---" + "\r"

    for i in range(1, grid_size+1):
        num_grid += str(i) + " |"
        for j in range(grid_size):
            num_grid += str(user_grid[i-1][j]) + " |"
        num_grid += "\n"

    user_grid_str_rep += draw_top + draw_horizontal_line + \
        num_grid + draw_horizontal_line
    return user_grid_str_rep


def dug_neighboring_cells(cellindex_withzero_value, main_grid, user_grid):
    '''
    If the user digs a 0-valued cell, then all the neighboring elements must be displayed until a non-zero-valued cell is reached.
    Returns string represenation of the board.
    '''
    # get a list of all neighboring cells
    neighboring_cells = []
    for elem in cellindex_withzero_value:
        r = elem[0]
        c = elem[1]
        for i in range(-1, 2):
            for j in range(3):
                if (0 <= (r+i) <= grid_size-1) and (0 <= c-j+1 <= grid_size-1) and (r+i, c-j+1) != (r, c) and main_grid[r+i][c-j+1] != -1:
                    neighboring_cells.append((r+i, c-j+1))

    # get unique values in neighboring_cells
    neighboring_cells = list(set(neighboring_cells))

    # remove if the cell has already been dugged
    already_dugged_cell = []
    for tup in neighboring_cells:
        if user_grid[tup[0]][tup[1]] != ' ':
            already_dugged_cell.append(tup)
    for elem in already_dugged_cell:
        neighboring_cells.remove(elem)

    list_tup_to_remove = []
    for tup in neighboring_cells:
        if main_grid[tup[0]][tup[1]] > 0:
            user_grid[tup[0]][tup[1]] = main_grid[tup[0]][tup[1]]
            list_tup_to_remove.append(tup)
        elif main_grid[tup[0]][tup[1]] == 0:
            user_grid[tup[0]][tup[1]] = main_grid[tup[0]][tup[1]]
    if len(list_tup_to_remove) > 0:
        for elem in list_tup_to_remove:
            neighboring_cells.remove(elem)

    if len(neighboring_cells) == 0:
        return neighboring_cells
    else:
        dug_neighboring_cells(neighboring_cells, main_grid, user_grid)
    return draw_user_grid(user_grid)


def is_winner(user_grid, main_grid):
    '''
    Checks to see if the user has dugged all cells correctly.
    Returns True if all dugged cells are correct else returns False
    '''
    for index, arr in enumerate(user_grid):
        for i, value in enumerate(arr):
            if value == 'F':
                if main_grid[index][i] != -1:
                    return False
            else:
                if main_grid[index][i] != value:
                    return False
    return True


if __name__ == '__main__':

    # draw the user grid to be shown to the user
    user_grid = []
    for i in range(grid_size):
        user_grid.append([])
        for j in range(grid_size):
            user_grid[i].append(" ")

    # draw the main grid which will have all cells filled. This will be used to compare with user_grid
    main_grid = []
    for i in range(grid_size):
        main_grid.append([])
        for j in range(grid_size):
            main_grid[i].append(0)

    # plant mines
    def get_a_random_num(grid_size):
        return random.randint(0, grid_size-1)

    mine_count = 0
    while mine_count != num_mines:
        row = get_a_random_num(grid_size)
        col = get_a_random_num(grid_size)

        if main_grid[row][col] != -1:
            main_grid[row][col] = -1
            mine_count += 1

    # setting up the grid numbers
    for index, arr in enumerate(main_grid):
        for i, value in enumerate(arr):
            if value == -1:
                r = index
                c = i

                for i in range(-1, 2):
                    for j in range(3):
                        if (0 <= (r+i) <= grid_size-1) and (0 <= c-j+1 <= grid_size-1) and (r+i, c-j+1) != (r, c) and main_grid[r+i][c-j+1] != -1:
                            main_grid[r+i][c-j+1] += 1

    # Show the initial blank grid to the user
    print(draw_user_grid(user_grid))

    while True:
        # Ask where the user wants to dig.
        # Following block will keep on asking for user input if the cell has been already dugged or if the input is incorrect.
        while True:
            user_input = input(
                "Enter row number followed by space and column number (Ex.2 3). If you want to Flag a cell, enter F at the end (Ex.1 2 F)= ").split()
            if len(user_input) == 2 and len(user_input[0]) == 1 and len(user_input[1]) == 1 and user_input[0].isnumeric() and user_input[1].isnumeric() and (user_grid[int(user_input[0])-1][int(user_input[1])-1] == ' ' or user_grid[int(user_input[0])-1][int(user_input[1])-1] == 'F'):
                break
            elif len(user_input) == 3 and len(user_input[0]) == 1 and len(user_input[1]) == 1 and len(user_input[2]) == 1 and user_input[0].isnumeric() and user_input[1].isnumeric() and user_input[2].lower() == "f" and user_grid[int(user_input[0])-1][int(user_input[1])-1] == ' ':
                break

        if len(user_input) == 2:
            if main_grid[int(user_input[0])-1][int(user_input[1])-1] == -1:
                user_grid[int(user_input[0])-1][int(user_input[1])-1] = "M"
                print(draw_user_grid(user_grid))
                print("Oops, You dugged a mine! Game Over")
                break
            elif main_grid[int(user_input[0])-1][int(user_input[1])-1] >= 1:
                user_grid[int(user_input[0])-1][int(user_input[1]) -1] = main_grid[int(user_input[0])-1][int(user_input[1])-1]
                print(draw_user_grid(user_grid))
            elif main_grid[int(user_input[0])-1][int(user_input[1])-1] == 0:
                user_grid[int(user_input[0])-1][int(user_input[1])-1] = 0
                print(dug_neighboring_cells(
                    [(int(user_input[0])-1, int(user_input[1])-1)], main_grid, user_grid))
        # else if the len > 2 and has F in input, then show the grid
        else:
            user_grid[int(user_input[0])-1][int(user_input[1])-1] = 'F'
            print(draw_user_grid(user_grid))

        # check for winner
        if is_winner(user_grid, main_grid):
            print("Congratulations. You won!")
            break
