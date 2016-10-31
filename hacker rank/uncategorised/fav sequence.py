from __future__ import print_function
t=input()
inp=[0 for row in range(0,t)]
for i in range(0,t):
    p=input()
    inp[i]=raw_input().strip()
seq=set()
for i in range(0,t):
    ar = map(int, inp[i].split())
    seq.update(ar)
for x in seq:
    print(x,end=" ")
        
        
