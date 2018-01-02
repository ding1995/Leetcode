# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:28:18 2017

@author: dell
"""

def reverseStr(s, k):
    i=0
    result=''
    while i<len(s):
        el=min(i+k,len(s))
        temp=s[i:el]
        result+=temp[::-1]
        i=i+2*k
        result+=s[el:min(i,len(s))]
    return result

s = "abcd"
k = 4
print(reverseStr(s, k))