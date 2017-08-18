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
    n, k, p, m = input().strip().split(' ')
    n, k, p, m = [int(n), int(k), int(p), int(m)]
    

    c = 1 # testing
    Cn_1 = c*n-1
    total_digits = Cn_1 +1
    bank_accounts = range(1,k+1)
    const_array = [ p**(n-1-i) for i in range(0,n) ]

    vals = (i for i in product(bank_accounts, repeat=total_digits))
    sum_vals = []
    vals_ = []
    done = False
    for val in vals:    
        if done: break
        sums_ = sum([a*b for a,b in zip(val, const_array)])%m 
        sum_vals.append(sums_)
        vals_.append(val)
        dups = [_ for _ in list_duplicates(sum_vals)]
        if len(dups)>0:
            for dup_val in dups:
                if done: break
                if(len(dup_val[1])>=2):
                    print(dup_val)
                    for elem in  [vals_[i] for i in dup_val[1][:2]]:
                        print(' '.join([str(i) for i in elem]))                    
                    done = True