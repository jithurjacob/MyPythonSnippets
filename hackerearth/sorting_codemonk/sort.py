#https://www.hackerearth.com/notes/sorting-code-monk/



# Quick sort
#
#This algorithm is also based on the divide and conquer approach. 
#It reduces the space complexity and removes the use of auxiliary array used in merge sort.
#
#Idea: It is based on the idea of choosing one element as pivot element and partitioning the array 
#around it such that the left side of pivot contains all elements less than the pivot element and 
#right side contains all elements greater than the pivot.

#Selecting a random pivot in an array results into an improved time complexity in average cases.
#
#
#Implementation:
#Choose the first element of array as pivot element First, we will see how the partition of the array takes place around the pivot.
# or we could use random element as pivot also
#
# O( n (log n)) .
#worst n2
'''
start = leftmost position of the array.
end = rightmost position of the array.
i = boundary point between those less than pivot and those greater than pivot .
j = boundary point between partitioned and unpartitioned part of array.
piv = pivot element .
'''
print "Quick Sort"
arr=[5,4,3,2,1]
print arr

def partition(arr,start,end):
	pivot,i,j=start,start+1,start+1 #make the first element as pivot element.
	while j<=end:
		#rearrange the array by putting elements which are less than pivot on one side and which are greater that on other.
		if arr[j]<arr[pivot]:
			temp=arr[j]
			arr[j]=arr[i]
			arr[i]=temp
			i=i+1
		j=j+1
	#put the pivot element in its proper place.   swap ( A[ start ] ,A[ i-1 ] ) 
	temp=arr[start]
	arr[start]=arr[i-1]
	arr[i-1]=temp

	return i-1 #return the position of the pivot

def quickSort(arr,start,end):
	if start<end:
		pivot=partition(arr,start,end)
		quickSort(arr,start,pivot-1)#sorts the left side of pivot.
		quickSort(arr,pivot+1,end)#sorts the right side of pivot.
	return arr
quickSort(arr,0,len(arr)-1)
print arr
# end quick sort


#############################################################################################################################

# Merge Sort
#
#divide the array into two sort return recursively / I've seen non recursive also
#
# The height of the tree will be log2n At each level the merge operation will take O( n ) time
# So the overall complexity of this algorithm will be O( n( log2 n )).
#
print "Merge Sort"
arr=[5,4,3,2,1]
print arr

def merge(arr,low,mid,high):
	p,q,r,k,i=low,mid+1,high,0,low
	a=[0 for x in xrange(0,len(arr))]
	#print "\nmerge",low,high
	
	while i <= high:
		if p > mid:     #checks if first part comes to an end or not .
			a[k] = arr[q]
			k,q=k+1,q+1
		elif ( q > high):   #checks if second part comes to an end or not
			a[k] = arr[p]
			k,p=k+1,p+1
		elif( arr[p] < arr[q]):     #checks which part has smaller element.
			a[k] = arr[p]
			k,p=k+1,p+1
		else:
			a[k] = arr[q]
			k,q=k+1,q+1
   		i=i+1
   
	#print a,arr
	i=0
	while i<k:
		arr[low]=a[i]
		i,low=i+1,low+1
	#print arr
	return arr
def sort(arr,low,high):
	#print "sort",low,high
	mid=(low+high)/2
	if low<high:
		sort(arr,low,mid)
		sort(arr,mid+1,high)
		merge(arr,low,mid,high)
		#print "\n"*5
	return arr

print sort(arr,0,len(arr)-1)
#end merge sort



######################################################################################################################

#insertion sort
#
#The idea behind is that in each iteration, it consumes one element from the input elements, 
#removes it and finds its correct position i.e., where it belongs in the sorted list and places it there
#
#in each round we are inserting an element and exchange the element till it gets in right place
#
# complexity O(n2)
#
#

print "Insertion Sort"
arr=[5,4,3,2,1]
print arr
n=len(arr)
for i in xrange(0,n):
	for k in xrange(i,0,-1):
			if arr[k]<arr[k-1]:
				temp=arr[k]
				arr[k]=arr[k-1]
				arr[k-1]=temp
			else:
				break

print arr

#end insertion sort

#################################################################################################

# selection sort
#
# in each round we find the min/max item and place on the right place
#
# Complexity O( n2 )
#
print "Selection Sort"
arr=[5,4,3,2,1]
print arr
n=len(arr)
for i in xrange(0,n):
	min=i
	for j in xrange(i,n):
		if(arr[min]>arr[j]):
			min=j
	temp=arr[i]
	arr[i]=arr[min]
	arr[min]=temp

print arr
# end of selection sort


################################################################################################


#bubble sort
#
# checking bw adjacent items in each round the max item will be on the end
#
#
#
# O(n2) in the worst and average case
#
print "Beubble Sort"
arr=[5,4,3,2,1]
print arr
n=len(arr)
for i in xrange(0,n):
	for j in xrange(0,n-1-i):
		if arr[j]>arr[j+1]:
			temp=arr[j]
			arr[j]=arr[j+1]
			arr[j+1]=temp
		#print arr
print arr

# end bubble sort

