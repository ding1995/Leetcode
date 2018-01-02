# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 18:30:09 2017

@author: dell
"""
import collections
def frequencySort(s):
    fre=collections.Counter(s)
    sort_fre=sorted(fre.items(),key=lambda d:d[1],reverse=True)

    alpha=[x[0] for x in sort_fre]
    valu=[x[1] for x in sort_fre]
    result=''
    prod = [a*b for a,b in zip(alpha,valu)]
    result=''.join([x for x in prod])
    #for i in range(len(alpha)):
     #   result=result+valu[i]*alpha[i]
    return result

s="tree"
print(frequencySort(s))
