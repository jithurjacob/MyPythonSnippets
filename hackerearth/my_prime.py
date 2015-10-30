#https://www.hackerearth.com/problem/algorithm/my-prime/
n=input()
arr=[int(i) for i in raw_input().split(" ")]
x=0
while x<len( arr):
	y=0
	while y<len(arr):
		#print y,arr
		if arr[x]!=arr[y] and arr[y]%arr[x]==0:
			#print "here",arr[y],arr[x],arr
			arr.remove(arr[y])
			y-=1
			x-=1
		y+=1
	x+=1	
for x in arr:
	print x,


