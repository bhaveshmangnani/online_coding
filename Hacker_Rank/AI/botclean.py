#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    right = 1
    bottom = 1
    
    if(board[posr][posc] == 'd'):
        print("CLEAN")
    else:
        nextx = -1
        for i in range(posr, len(board)):
            if board[posr][i] == 'd':
                print('RIGHT')
        
        for i in range(posr, -1, -1):
            if board[posr][i] == 'd':
                print('LEFT')
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
