# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:14:14 2017

@author: dell
"""

def matrixReshape(nums, r, c):
    orir , oc=len(nums) , len(nums[0])
    if (orir*oc != r*c) or ((orir==r) & (oc==c)):
        return nums
    temp=[]
    result=[]
    count=0
    for i in range(orir):
        for j in range(oc):
            temp.append(nums[i][j])
            count+=1
            if count==c:
                count=0
                result.append(temp)
                temp=[]
    return result

nums = [[1,2], [3,4]]
r = 1
c = 4
print(matrixReshape(nums, r, c))