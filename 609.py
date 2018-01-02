# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 07:52:51 2017

@author: dell
"""
import collections
def findDuplicate(paths):
    #txtvisited=collections.defaultdict(list) 
    txtvisited={}
    for txt in paths:
        se=txt.split()
        for j in range(1,len(se)):
            l=se[j].find('(')
            conte=se[j][l+1:]
            txtvisited.setdefault(conte,[]).append(se[0]+'/'+se[j][:l])
    result=[x for x in txtvisited.values() if len(x)>1]
    print(result)
    return result
    
paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
findDuplicate(paths)