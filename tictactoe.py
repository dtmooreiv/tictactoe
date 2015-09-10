#!/usr/bin/python

def convert_row(row):
    """
        prints an array of 0's,1's,and 2's as their tictactoe characters
    """
    row_string = ''
    for num in row:
        row_string+=(convert_num(num) + '|')
    return row_string


def convert_num(num):
    """
        returns the character that each number represents
    """
    if num == 1:
        return 'O'
    elif num == 2:
        return 'X'
    else:
        return ' '

def print_board(board):
    """
        prints a two-dimensional tictactoe board
    """
    for row in board:
        print(convert_row(row))
        print('______')

def toggle_player(player):
    """
        toggle_player(1) = 2
        toggle_player(2) = 1
        toggle_player(other) = who_cares
    """
    return player % 2 + 1

def has_won(board):
    """
        returns 0 if game is unwon.
        returns player number of winning player if game is won.
    """
    #Check the rows
    if board[0][0] == board[0][1] and board[0][2] == board[0][0] and not board[0][0] == 0:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][2] == board[1][0] and not board[1][0] == 0:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][2] == board[2][0] and not board[2][0] == 0:
        return board[1][0]
    #Check the columns
    elif board[0][0] == board[1][0] and board[2][0] == board[0][0] and not board[0][0] == 0:
        return board[1][0]
    elif board[0][1] == board[1][1] and board[2][1] == board[0][1] and not board[0][1] == 0:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[2][2] == board[0][2] and not board[0][2] == 0:
        return board[0][2]
    #Check the diagonals
    elif board[0][0] == board[1][1] and board[2][2] == board[0][0] and not board[0][0] == 0:
        return board[0][0]
    elif board[2][0] == board[1][1] and board[0][2] == board[1][1] and not board[2][0] == 0:
        return board[2][0]
    else:
        return 0

if __name__ == '__main__':

    board = [[0,0,0],[0,0,0],[0,0,0]]
    player = 1
    while has_won(board) == 0:
        print_board(board)
        print('Please enter the row player:' + str(player))
        row_move = int(input())
        print('Please enter the column player:' + str(player))
        column_move = int(input())
        board[row_move][column_move] = player
        player = toggle_player(player)
    print('player ' + str(has_won(board)) + ' has won!')



