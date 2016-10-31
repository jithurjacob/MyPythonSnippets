# Enter your code here. Read input from STDIN. Print output to STDOUT
st=raw_input().split(" ")
r=int(st[0])
c=int(st[1])
index=0
for i in range(1,r):
    #print index
    if i%2==1:
        index=index+1
    else:
        index=index+9
for i in range(1,c):
    index=index+2
print index
