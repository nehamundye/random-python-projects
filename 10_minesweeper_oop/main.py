import random


class Board(object):
    def __init__(self, grid_size, num_mines):
        self.grid_size = grid_size
        self.num_mines = num_mines
        self.main_grid = [[0 for i in range(grid_size)]
                          for j in range(grid_size)]
        self.user_grid = [
            [" " for i in range(grid_size)] for j in range(grid_size)]

    def __str__(self):
        '''
        Returns a string representation of the board.
        '''
        user_grid_str_rep = ""
        draw_top = "   "
        num_grid = "\n"
        for i in range(1, self.grid_size+1):
            draw_top += str(i) + "  "

        draw_horizontal_line = "\n"
        for _ in range(self.grid_size):
            draw_horizontal_line += "---"
        draw_horizontal_line += "---" + "\r"

        for i in range(1, self.grid_size+1):
            num_grid += str(i) + " |"
            for j in range(self.grid_size):
                num_grid += str(self.user_grid[i-1][j]) + " |"
            num_grid += "\n"

        user_grid_str_rep += draw_top + draw_horizontal_line + \
            num_grid + draw_horizontal_line
        return user_grid_str_rep

    def plantMinesInMainGrid(self):
        '''
        Adds mine to main grid.
        '''
        mine_count = 0
        while mine_count != self.num_mines:
            row = random.randint(0, self.grid_size-1)
            col = random.randint(0, self.grid_size-1)

            if self.main_grid[row][col] != -1:
                self.main_grid[row][col] = -1
                mine_count += 1

    def fillMainGridNumbers(self):
        '''
        Fills all cells of the main grid. This grid will have mines and all cells filled with number of mines or 0.
        '''
        for index, arr in enumerate(self.main_grid):
            for i, value in enumerate(arr):
                if value == -1:
                    r = index
                    c = i

                    for i in range(-1, 2):
                        for j in range(3):
                            if (0 <= (r+i) <= self.grid_size-1) and (0 <= c-j+1 <= self.grid_size-1) and (r+i, c-j+1) != (r, c) and self.main_grid[r+i][c-j+1] != -1:
                                self.main_grid[r+i][c-j+1] += 1

    def dug_neighboring_cells(self, cellindex_withzero_value):
        '''
        If the user digs a 0-valued cell, then all the neighboring elements must be displayed until a non-zero-valued cell is reached.
        This Funtion updates the user_grid. Returns None.
        '''
        # get a list of all neighboring cells
        neighboring_cells = []
        for elem in cellindex_withzero_value:
            r = elem[0]
            c = elem[1]
            for i in range(-1, 2):
                for j in range(3):
                    if (0 <= (r+i) <= self.grid_size-1) and (0 <= c-j+1 <= self.grid_size-1) and (r+i, c-j+1) != (r, c) and self.main_grid[r+i][c-j+1] != -1:
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
            if self.main_grid[tup[0]][tup[1]] > 0:
                self.user_grid[tup[0]][tup[1]] = self.main_grid[tup[0]][tup[1]]
                list_tup_to_remove.append(tup)
            elif self.main_grid[tup[0]][tup[1]] == 0:
                self.user_grid[tup[0]][tup[1]] = self.main_grid[tup[0]][tup[1]]
        if len(list_tup_to_remove) > 0:
            for elem in list_tup_to_remove:
                neighboring_cells.remove(elem)

        if len(neighboring_cells) == 0:
            return neighboring_cells
        else:
            self.dug_neighboring_cells(neighboring_cells)

    def is_winner(self):
        '''
        Checks to see if the user has dugged all cells correctly.
        Returns True if all dugged cells are correct else returns False
        '''
        for index, arr in enumerate(self.user_grid):
            for i, value in enumerate(arr):
                if value == 'F':
                    if self.main_grid[index][i] != -1:
                        return False
                else:
                    if self.main_grid[index][i] != value:
                        return False
        return True


if __name__ == '__main__':
    # Show user an empty grid
    # Ask user where they want to dig
    #   If input is incorrect- Keep asking for input.
    #   If input is correct:
    #       Check: a. If input is a mine -> Game Over
    #              b. If input is a number/not a mine -> Display that cell/grid
    #              c. If input is 0-valued cell -> Dsiplay all neighboring cells until we reach non-zero cell
    board = Board(4, 2)

    board.plantMinesInMainGrid()
    board.fillMainGridNumbers()
    main_grid = board.main_grid
    user_grid = board.user_grid

    # Show user an empty grid
    print(board)

    while True:

        # Ask user where they want to dig
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
                print(board)
                print("Oops, You dugged a mine! Game Over")
                break
            elif main_grid[int(user_input[0])-1][int(user_input[1])-1] >= 1:
                user_grid[int(user_input[0])-1][int(user_input[1]) -
                                                1] = main_grid[int(user_input[0])-1][int(user_input[1])-1]
                print(board)
            elif main_grid[int(user_input[0])-1][int(user_input[1])-1] == 0:
                user_grid[int(user_input[0])-1][int(user_input[1])-1] = 0
                board.dug_neighboring_cells(
                    [(int(user_input[0])-1, int(user_input[1])-1)])
                print(board)
        # else if the len > 2 and has F in input, then show the grid
        else:
            user_grid[int(user_input[0])-1][int(user_input[1])-1] = 'F'
            print(board)

        # check for winner
        if board.is_winner():
            print("Congratulations. You won!")
            break
