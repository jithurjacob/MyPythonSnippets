def princess_pos(n,grid):
    for i in xrange(0,n):
        if "p" in grid[i]:
            for j in xrange(0,n):
                if "p" ==grid[i][j]:
                    return str(i)+" "+str(j)
def nextMove(n,r,c,grid):
    move=""
    y,x = [int(i) for i in princess_pos(n,grid).strip().split()]
    print x,y,princess_pos(n,grid)
    #if abs(r-x)<abs(c-y):
    print r,c,x,y
    if c<x :
        move="RIGHT"
    elif c>x:
        move="LEFT"
    elif r>y:
        move="UP"
    elif r<y:
        move="DOWN"
    return move
if __name__ == '__main__':
    n = int(raw_input())
    r,c = [int(i) for i in raw_input().strip().split()]
    grid = []
    for i in xrange(0, n):
        grid.append(raw_input())
    print nextMove(n,r,c,grid)