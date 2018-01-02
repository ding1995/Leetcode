# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:22:07 2017

@author: dell
"""

def containsNearbyDuplicate(nums, k):
    visited={}
    if len(set(nums))==len(nums):
        return False
    for i,ele in enumerate(nums):
        if ele in visited:
            if (i-visited[ele])<= k:
                return True
            else:
                visited[ele]=i   
        else:
            visited[ele]=i                
    return False

nums=[1,0,1,1]
k=1
print(containsNearbyDuplicate(nums, k))