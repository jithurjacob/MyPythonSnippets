from __future__ import print_function
def isPal(string):
    return string==string[::-1]
def find(string):
    temp=string
    c=0
    while c < len(string):
        
        if(isPal(string+string[c:0:-1])):
            print(string+string[c:0:-1])
            return len(string)+c
        else:
            c+=1
        
            
    return 2*len(string)-1

       
t=input()
inp=[0 for row in range(0,t)]
for i in range(0,t):
    inp[i]=raw_input().strip()

for i in range(0,t):
    print(inp[i])
    if(isPal(inp[i])):
        print(len(inp[i]))
    else:
        print(find(inp[i]))
       




    
