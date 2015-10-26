def insertion_sort(l):
    shift=0
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j > -1):
           l[j+1] = l[j]
           shift+=1
           j -= 1
        l[j+1] = key
    print(shift)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
#print " ".join(map(str,ar))
