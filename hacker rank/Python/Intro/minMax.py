# https://www.hackerrank.com/challenges/np-min-and-max?h_r=next-challenge&h_v=zen

import numpy as np

N,M = [int(x) for x in raw_input().split()]
print N,M
arr = np.array([[]])

for n in range(N):
	np.append(arr,[int(x) for x in raw_input().split()],axis=0)
print arr
