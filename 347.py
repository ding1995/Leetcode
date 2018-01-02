# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 20:12:52 2017

@author: dell
"""
import collections
def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt=collections.Counter(nums)
        sort_fre=sorted(cnt.items(),key=lambda d:d[1],reverse=True)
        alpha=sort_fre[:k]
        return [x[0] for x in alpha]

s=[1,1,1,2,2,3,3]
print(topKFrequent(s, 2))