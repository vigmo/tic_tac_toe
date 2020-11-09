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

def win_check(board, mark):
    check_result = False
    if mark == board[1] == board[2] == board[3]:
        check_result = True
    elif mark == board[4] == board[5] == board[6]:
        check_result = True
    elif mark == board[7] == board[8] == board[9]:
        check_result = True
    elif mark == board[1] == board[4] == board[7]:
        check_result = True
    elif mark == board[2] == board[5] == board[8]:
        check_result = True
    elif mark == board[3] == board[6] == board[9]:
        check_result = True    
    elif mark == board[1] == board[5] == board[9]:
        check_result = True
    elif mark == board[3] == board[5] == board[7]:
        check_result = True
        
    return check_result

def place_marker(board, marker, position): 

    #test_board = ['#','X','O','X','O','X','O','X','O','X'] given in the beginning of this exercise 

    #append board list with the latest X or O value 

    board[position] = marker 

    return board 

    #pass 

