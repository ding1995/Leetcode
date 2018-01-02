# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:54:07 2017

@author: dell
"""

def removeElement(nums, val):
    res=len(nums)
    i=0
    while i<len(nums):
        if nums[i]==val:
            del nums[i]
            res-=1
        else:
            i=i+1
    return res

nums=[3,2,2,3]
val=3
print(removeElement(nums, val))