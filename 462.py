# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:38:26 2017

@author: dell
"""

def minMoves2(nums):
    if len(nums)<=1:
        return 0
    def sum(x,y):
        return x+y
    count=0
 
    s=sorted(nums)        
    temp=s[len(s)//2]
    for i in range(len(nums)):
        count+=abs(nums[i]-temp)
    return count

nums=[1,2,3]
print(minMoves2(nums))