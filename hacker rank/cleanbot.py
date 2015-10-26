#!/usr/bin/python
def dirt_pos(board):
    for i in xrange(0,5):
        print board[i]
        if "d" in board[i]:
            for j in xrange(0,5):
                if "d"==board[i][j]:
                    print "fghfghfgh"
                    return str(i)+" "+str(j)
def next_move(posr, posc, board):
    dirt_pos(board)
    return 1
    x,y=[int(i) for i in dirt_pos(board).strip().split()]
    print x,y,posr,posc
    if posc < y:
        print "RIGHT"
    elif posc>y:
        print "LEFT"
    elif posr >x:
        print "UP"
    elif posr<x:
        print "DOWN"
    else:
        print "CLEAN"
    
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
