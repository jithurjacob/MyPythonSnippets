from __future__ import print_function
t=input()
inp=[0 for row in range(0,t)]
for i in range(0,t):
    inp[i]=raw_input().strip()
for i in range(0,t):
    ar = map(int, inp[i].split())
    n=ar[0]
    b=ar[1]
    mult=[]
    for j in range(n-b,n+b):
        if(j%b==0):
           mult.append(j)

    if(abs(mult[0]-n)<abs(mult[1]-n)):
        print(mult[0])
    else:
        print(mult[1])
    
