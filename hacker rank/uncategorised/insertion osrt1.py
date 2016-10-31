#!/bin/python
from __future__ import print_function
def insertionSort(ar):
    val=ar[-1]
    pos=0
    size=len(ar)
    for i in range(size-2,-1,-1):
        
        if(ar[i]>val):
            ar[i+1]=ar[i]
        else:
            pos=i+1
            
            break
        printar(ar)
       
    ar[pos]=val
    printar(ar)
    return ""
def printar(ar):
    size=len(ar)
    for i in range(0,size):
        print(ar[i],end=" ")
    print('')
    return ""
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
