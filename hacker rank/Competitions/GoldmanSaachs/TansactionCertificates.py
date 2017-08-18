from itertools import product
import sys
from collections import defaultdict
# https://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() 
                            if len(locs)>1)


if __name__ == "__main__":
    # n, k, p, m = input().strip().split(' ')
    # n, k, p, m = [int(n), int(k), int(p), int(m)]

    c = 1 # testing
    n,k,p,m = 3,4,3,16
    Cn_1 = c*n-1
    total_digits = Cn_1 +1
    bank_accounts = range(1,k+1)
    vals = [i for i in product(bank_accounts, repeat=total_digits)]

    const_array = [ p**(n-1-i) for i in range(0,n) ]
    #sums = [([a*b for a,b in zip(val, const_array)]) for val in vals ]
    sums_ = [sum([a*b for a,b in zip(val, const_array)])%m for val in vals ]
    #new_index_sets = [np.argwhere(i[0]== sums_) for i in np.array(np.unique(sums_, return_counts=True)).T if i[1]>=2]
    dups = [_ for _ in list_duplicates(sums_)]
    for elem in  [vals[i] for i in dups[0][1]][:2]:
        print(' '.join([str(i) for i in elem]))