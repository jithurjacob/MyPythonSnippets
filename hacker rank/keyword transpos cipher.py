from __future__ import print_function
t=input()
key=[0 for row in range(0,t)]
encr=[0 for row in range(0,t)]
decr=[0 for row in range(0,t)]
for i in range(0,t):
    key[i]=raw_input().strip()
    encr[i]=raw_input().strip()
for i in range(0,t):
    temp = map(str,encr[i].split())
    print(temp)
