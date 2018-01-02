# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:08:10 2017

@author: dell
"""

def twoSum(nums, target):
    c=len(nums)
    nums.sort()
    for i in range(c):
        for j in range(i+1,c):
            if nums[i]+nums[j]==target:
                return [i,j]
                
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))