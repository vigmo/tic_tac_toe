#Function for printing the Tic Tac Board
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' '+ board[7]+ ' | ' +board[8]+ ' | ' +board[9])
    print('-----------')
    print(' '+ board[4]+ ' | ' +board[5]+ ' | ' +board[6])
    print('-----------')
    print(' '+ board[1]+ ' | ' +board[2]+ ' | ' +board[3])


def player_input(): 
    mark = '' 
    while not (mark == 'X' or mark == 'O'): 
        mark = input("Player 1: Do you want to be X or O? ").upper()   
    if mark == 'X': 
        return ('X', 'O') 
    else: 
        return ('O', 'X') 

 
