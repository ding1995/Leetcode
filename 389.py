# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 05:29:28 2017

@author: dell
"""

import collections
def findTheDifference(s, t):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s_c=collections.Counter(s)
        t_c=collections.Counter(t)
        inter_st=dict.fromkeys(x for x in t_c if ((x not in s_c) or (s_c.get(x) != t_c.get(x)) ))
        result=[key for key in inter_st if not key.startswith('__')]        
        
        return ''.join([x for x in result])

s = "abcd"
t = "abacd"
print(findTheDifference(s, t))