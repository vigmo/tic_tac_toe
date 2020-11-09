# tic_tac_toe
def player_input(): 
    mark = '' 
    while not (mark == 'X' or mark == 'O'): 
        mark = input("Player 1: Do you want to be X or O? ").upper()   
    if mark == 'X': 
        return ('X', 'O') 
    else: 
        return ('O', 'X') 
