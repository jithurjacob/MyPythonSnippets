n=input()
sum=0.0
d=(2**n)**-1
print d
for x in xrange(0,n):
	sum=sum+(float(input()))
print sum
print (sum*d)**-1