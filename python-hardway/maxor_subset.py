from itertools import chain, combinations
N=input()
xs=[int(x) for x in raw_input().split()]
#print xs
ma=0
for x in list(chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1))):
    sum=0
    for y in x:
        sum=sum ^ y
    ma= max(ma,sum)
print ma
