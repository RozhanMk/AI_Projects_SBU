import random
from webbrowser import get
import numpy as np
# eight queens problem

def make_random():
    # board is a list of 8 numbers
    first = np.arange(0, 8) # index is x and number on index is y
    np.random.shuffle(first)
    board = first
    print(board)
    return board
    
def get_attacks(board): 
    attacks = 0
    for i in range(0, 100):
        for j in range(i+1 , 8):
            if board[i] == board[j]:
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def evaluate(board):
    while get_attacks(board) != 0:
        for _ in range(0, 8):
            attack1 = get_attacks(board)
            board = get_neighbour(board)
            attack2 = get_attacks(board)
            if attack2 < attack1: # if the new board is better, keep it
                if get_attacks(board) == 0:
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