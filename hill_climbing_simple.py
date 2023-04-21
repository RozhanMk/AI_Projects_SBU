import random
from webbrowser import get
# eight queens problem

def make_random():
    # board is a list of 8 numbers
    board = [i for i in range(8)] # index is x and number on index is y
    random.shuffle(board)
    return board
    
def get_attacks(board): 
    attacks = 0
    for i in range(8):
        for j in range(i+1 , 8):
            if board[i] == board[j]:
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def evaluate(board ):
    main_attack = get_attacks(board)
    while main_attack != 0:
        temp = board
        temp = get_neighbour(temp)
        if get_attacks(temp) < main_attack:
            board = temp
            main_attack = get_attacks(temp)
    return board
    
                
def get_neighbour(board):
    row = random.randint(0, 7)
    move = random.choice(['right','left'])
    if move == 'right':
        board[row] = (board[row] + 1) % 8
        board[(board[row] + 1) % 8] = row
    else:
        board[row] = (board[row] - 1) % 8
        board[(board[row] - 1) % 8] = row
    return board

def print_board(board):
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i] == j:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()

def main():
    board = make_random()
    print_board(evaluate(board))
main() # run the main function
