#Function for printing the Tic Tac Board
from IPython.display import clear_output

def display_board(board):
    print('\n'*100)
    print(' '+ board[7]+ ' | ' +board[8]+ ' | ' +board[9])
    print('-----------')
    print(' '+ board[4]+ ' | ' +board[5]+ ' | ' +board[6])
    print('-----------')
    print(' '+ board[1]+ ' | ' +board[2]+ ' | ' +board[3])

# Function to get a Player Input as X or O
def player_input(): 
    mark = '' 
    while not (mark == 'X' or mark == 'O'): 
        mark = input("Player 1: Do you want to be X or O? ").upper()   
    if mark == 'X': 
        return ('X', 'O') 
    else: 
        return ('O', 'X') 

# Function to check if a given mark X or O has won
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

# Function to assign a Marker X or O in the given board position
def place_marker(board, marker, position): 
    board[position] = marker 
    return board 
   
# Function to choose who plays first
import random
def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

# Function to check if board is full or not
def full_board_check(board):
    count = 0
    for i in range (1,10):
        if board[i] == ' ':
            count += 1   
    if count == 0:
        return True
    else:
        return False
# Function to check if is any space in board
def space_check(board, position): 

    if board[position] == ' ': 
        return True 
    else: 
        return False 
        
def player_choice(board): 
    ref = False 
    while ref == False: 
        pos = int(input("Choose your cell (between 1-9): ")) 
        if pos<1 and pos>9: 
            print('Number out of range') 
            continue 
        if space_check(board, pos): 
            ref = True 
            return pos 
        else: 
            print('The cell is already filled! Choose another one')

        #return False 
# Function to replay the game
def replay():
    reply = input("Do you want to play again? (Y or N): ").upper()
    return reply == 'Y'

#Final Game Play code
print('Welcome to Tic Tac Toe!')

while True:
    player1_marker, player2_marker = player_input()
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    turn = choose_first()
    print(f'{turn} will go first.')
    # Set the game up here
    #pass
    game_on = True

    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)
            if win_check(game_board, player1_marker):
                display_board(game_board)
                game_on = False
                print(turn +' wins')
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print ('Game is Tied')
                    game_on = False
                else:
                    turn = 'Player 2'
            
        # Player2's turn.
        else:
            
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)
            if win_check(game_board, player2_marker):
                display_board(game_board)
                game_on = False
                print(turn +' wins')
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print ('Game is Tied')
                    game_on = False
                else:
                    turn = 'Player 1'
           
    if not replay():
        break

    #Vignesh adding a comment for his branch vigmo_test