'''
26/10/2015
program that sorts T test cases in incresing order

fallback to default as timeout on some cases
'''
def partition(arr,start,end):
	pivot,i,j=start,start+1,start+1
	while j<=end:
		if arr[j]>arr[pivot]:
			temp=arr[j]
			arr[j]=arr[i]
			arr[i]=temp
			i=i+1
		j=j+1
	temp=arr[i-1]
	arr[i-1]=arr[pivot]
	arr[pivot]=temp
	return i-1
def quick_sort(arr,start,end):
	if start<end:
		pivot=partition(arr,start,end)
		quick_sort(arr,start,pivot-1)
		quick_sort(arr,pivot+1,end)
	return arr
T=input()
for x in xrange(0,T):
	n=input()
	arr=[int(i) for i in raw_input().split()]
	arr.sort(reverse=True)#quick_sort(arr,0,len(arr)-1)
	#print arr
	for elem in arr:
		print elem,
	print
