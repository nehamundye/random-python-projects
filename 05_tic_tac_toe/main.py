"""
1. Draw the Tic Tac Toe game board
2. X is 1st player, O is the 2nd player
3. Ask input from player X.
4. O player will be computer.
5. Check if player X or player Y is the winner or if there are no more moves, its a tie and end the game.
"""

import random

def draw_board():
    k = 1
    for i in range(1, 4):
        print("|", end=" ")
        for j in range(k, k+3):
            print(f"{j} |", end=" ")
        k += 3
        print("\r")


def draw_current_board(display_board, current_board, x_input_list, o_input_list):
    for i in range(0,3):
        for j in range(0,3):
            if display_board[i][j] in x_input_list:
                current_board[i][j] = "X"
            if display_board[i][j] in o_input_list:
                current_board[i][j] = "O"

    for i in range(0,3):
        print("|", end=" ")
        for j in range(0,3):
            print(f"{current_board[i][j]} |", end=" ")
        print("\r")


# check diagnol
def check_left_diagnol(input_list):
    count = 0
    for position in input_list:
        if position in [1, 5 ,9]:
            count += 1
    if count == 3:
        return True

def check_right_diagnol(input_list):
    count = 0
    for position in input_list:
        if position in [1, 5 ,9]:
            count += 1
    if count == 3:
        return True

def check_row_top(input_list):
    count = 0
    for position in input_list:
        if position in [1, 2 ,3]:
            count += 1
    if count == 3:
        return True

def check_row_middle(input_list):
    count = 0
    for position in input_list:
        if position in [4, 5 ,6]:
            count += 1
    if count == 3:
        return True

def check_row_bottom(input_list):
    count = 0
    for position in input_list:
        if position in [7, 8 ,9]:
            count += 1
    if count == 3:
        return True
    
def check_col_top(input_list):
    count = 0
    for position in input_list:
        if position in [1, 4 ,7]:
            count += 1
    if count == 3:
        return True

def check_col_middle(input_list):
    count = 0
    for position in input_list:
        if position in [2, 5 ,8]:
            count += 1
    if count == 3:
        return True

def check_col_bottom(input_list):
    count = 0
    for position in input_list:
        if position in [3, 6 ,9]:
            count += 1
    if count == 3:
        return True


display_board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

current_board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

x_input_list = []
o_input_list = []

draw_board()
print("\r")

if __name__ == '__main__':
    while True:

        # Validation to get user_input to be in the range 1 to 9
        while True:
            x_input = input("Player X. Input X in position (1 to 9): ")
            if x_input in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                x_input = int(x_input)
                if x_input in x_input_list or x_input in o_input_list:
                    print(f"Position {x_input} is alreay taken. Please input another position")
                if x_input not in x_input_list and x_input not in o_input_list:
                    break

        x_input_list.append(x_input)

        draw_current_board(display_board, current_board, x_input_list, o_input_list)
        print("\r")
        
        
        # check if X won
        if (check_left_diagnol(x_input_list) or check_right_diagnol(x_input_list) or check_row_top(x_input_list) or check_row_middle(x_input_list) or check_row_bottom(x_input_list) or check_col_top(x_input_list) or check_col_middle(x_input_list) or check_col_bottom(x_input_list)):
            print("Player X won!")
            break

        if len(x_input_list) == 5:
            print("Its a tie.")
            break

        # Computer's turn
        o_input = random.randint(1,9)
        while o_input in x_input_list or o_input in o_input_list:
            o_input = random.randint(1,9)

        o_input_list.append(o_input)

        print(f"Player O chose position {o_input}")
        draw_current_board(display_board, current_board, x_input_list, o_input_list)
        print("\n")

        # check if O won
        if (check_left_diagnol(o_input_list) or check_right_diagnol(o_input_list) or check_row_top(o_input_list) or check_row_middle(o_input_list) or check_row_bottom(o_input_list) or check_col_top(o_input_list) or check_col_middle(o_input_list) or check_col_bottom(o_input_list)):
            print("Player O won!")
            break

    


