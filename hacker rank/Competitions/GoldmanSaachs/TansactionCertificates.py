import numpy as np
from itertools import product
import sys

if __name__ == "__main__":
    n, k, p, m = input().strip().split(' ')
    n, k, p, m = [int(n), int(k), int(p), int(m)]

    c = 1 # testing
    # n,k,p,m = 3,4,3,16
    Cn_1 = c*n-1
    total_digits = Cn_1 +1
    bank_accounts = range(1,k+1)
    vals = [np.array(i) for i in product(bank_accounts, repeat=total_digits)]

    const_array = np.array([ p**(n-1-i) for i in range(0,n) ])
    sums = vals * const_array
    sums_ = np.sum(sums,axis=1)
    new_index_sets = [np.argwhere(i[0]== sums_) for i in np.array(np.unique(sums_, return_counts=True)).T if i[1]>=2]
    for elem in sums[new_index_sets[0]][:2]:
        print(' '.join([str(i) for i in list(elem[0])]))