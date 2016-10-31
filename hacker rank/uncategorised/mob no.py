from __future__ import print_function
def pretify(ar):
    return "+91 "+ar[-10:-5]+" "+ar[-5:]

t=input()
inp=[0 for row in range(0,t)]
for i in range(0,t):
    inp[i]=raw_input().strip()
for i in range(0,t):
    inp[i]=pretify(inp[i])
inp.sort()
for i in range(0,t):
    print(inp[i])
    #print("+91 "+ar[-10:-5]+" "+ar[-5:])
