import numpy as np
N = input()
nums = np.array(map(int, raw_input().split()))
print nums
print nums.mean()
print np.median(nums)
print np.mode(nums)

