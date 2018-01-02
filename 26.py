# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:10:47 2017

@author: dell
"""

def removeDuplicates(nums):
    if len(nums)<2:
        return len(nums)
    i,j=0,1
    re=len(nums)
    while j<len(nums):
        if nums[j]==nums[i]:
            del nums[j]
            re-=1
        else:
            i=j
            j+=1
    return re

nums = [1,1,2]
print(removeDuplicates(nums))