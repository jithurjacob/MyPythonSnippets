from itertools import combinations,permutations,combinations_with_replacement,product
T=input()
for t in xrange(T):

	x=product('PN', repeat=input())
	sum=0
	for i in x:
	
		j= "".join(i)
		if "PP" not in j:
			sum+=1
	print sum**2