from decimal import getcontext, Decimal

getcontext().prec = 102
L, d, s = 100, 100, 0
p = pow(10, d-1)

for z in range(2, L):
    q = Decimal(z).sqrt()
    s += sum(int(c) for c in str(q * p)[:d]) if  q % 1 != 0 else 0
 
print "Project Euler 80 Solution =", s
