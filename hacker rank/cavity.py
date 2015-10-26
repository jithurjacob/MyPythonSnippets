from __future__ import print_function
if __name__ == '__main__':
    n = input()
    i=0
    b=[[0 for col in range(0,n)] for row in range(0,n)]
    c=[[0 for col in range(0,n)] for row in range(0,n)]
    for i in range(0,n):
            data=raw_input().strip()
            for j in range(0,n):
                b[i][j] = data[j]
                c[i][j] = data[j]
     
    for i in range(1,n-1):
        for j in range(1,n-1):
            if(b[i][j] > b[i-1][j] and b[i][j] > b[i+1][j] and b[i][j] > b[i][j-1] and b[i][j] > b[i][j+1] ):
                c[i][j]='X'
    
    for i in range(0,n):
        for j in range(0,n):
            print(c[i][j], end="")
        print('')
            
        
       
        
