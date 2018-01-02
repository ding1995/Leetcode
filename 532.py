# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:55:05 2017

@author: dell
"""

def findPairs(nums, k):
    if k>0:
         return len(set(nums)&set(n+k for n in nums))
    else:
        if k==0:
            sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0

nums=[1, 1, 1, 1, 5]
k = 0
print(findPairs(nums, k))