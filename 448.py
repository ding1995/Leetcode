# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:09:34 2017

@author: dell
"""

def findDisappearedNumbers(nums):
        l1=set(list(range(1,len(nums)+1)))
        l2=set(nums)
        return list(l1-l2)
nums=[4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))