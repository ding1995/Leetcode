# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:38:59 2017

@author: dell
"""
import itertools
def findSubsequences(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        if nums==[]:
            return result
        unsort=[]
        sortre=[]
        sort_nums=sorted(nums)
        for i in range(2,len(sort_nums)+1):
            temp=list(itertools.combinations(sort_nums,i))
            temp1=list(itertools.combinations(nums,i))
            #unsort.extend(temp)
            #sortre.extend(temp1)
            result.extend(set(temp)&set(temp1))
        #result=list(set(unsort)&set(sortre))
        return result

nums=[4,3, 1,2]
print(findSubsequences(nums))