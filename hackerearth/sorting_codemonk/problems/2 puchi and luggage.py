'''
check whether a smaller item exists in future
'''
for x in xrange(0,input()):
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
				
		print flag,
	print
		