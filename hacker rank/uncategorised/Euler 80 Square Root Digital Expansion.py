from math import sqrt
import decimal
n=decimal.Decimal(raw_input())
p=int(raw_input())
decimal.getcontext().prec = p+5#10000
sum=0
for j in range(1,n+1):
    root=decimal.Decimal(j).sqrt()
    q=str(root)
    if not int(root)**2==int(j):
        q=q.replace(".","")#.ljust(p, '0')
        #print q,len(q)
        
        for i in range(0,p):
            #print i,q[i]
            sum+= int(q[i])
print sum
    
