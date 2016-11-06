# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
elems = [int(elem) for elem in raw_input().split()]
#print max([elem for elem in elems if elem!=max(elems)])
print sorted(set(elems))[-2]