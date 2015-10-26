'''
check whether a smaller item exists in future
'''
T=input()
for x in xrange(0,T):
	n=input()
	arr=[]
	for i in xrange(0,n):
		arr.append(input())
	arr.sort()
	for i in xrange(0,n):
		flag=0
		for j in xrange(i+1,n):
			if arr[j]<arr[i]:
				flag=flag+1
				
		#if n==1:flag=1
		print flag,
	print
		