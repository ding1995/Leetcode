# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:26:23 2017

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 06:46:28 2017

@author: dell
"""

s=[0,1]

def findMaxLength(nums):
    N=len(nums)
    if N<2:
        return 0
    newnums=[x*2-1 for x in nums]
    dic={}
    dic[0]=-1
    sum=0
    maxl=0
    for i in range(N):
        sum=sum+newnums[i]
        print(sum)
        if sum in dic:
            maxl=max(maxl,i-dic[sum])
        else:
            dic[sum]=i           
    return maxl

t=[0,0,1,0,0,0,1,1]
print(findMaxLength(t))

