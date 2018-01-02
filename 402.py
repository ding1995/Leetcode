# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:06:12 2017

@author: dell
"""

def removeKdigits(num, k):
    #digit=int(num)
    N=len(num)
    loc=0
    result=''
    count=0
    if k>=N:
        return "0"
    while (k+count<N) & (count<=N-k):
        temp=num[loc:k+count+1] 
        loc=loc+temp.index(min(temp))+1
        result+=min(temp)
        count+=1
    result+=num[loc:loc+N-k-count]
    return result.lstrip('0') or '0'

num="1432219"
k = 8
print(removeKdigits(num, k))