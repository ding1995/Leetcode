# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:57:39 2017

@author: dell
"""

def checkInclusion(s1, s2):
    N1=len(s1)
    N2=len(s2)
    if N1>N2:
        return False
    start=0
    endp=N1
    temp=s2[start:endp]
    c1=[0]*26
    c2=[0]*26
    for i in range(N1):
        c1[ord(s1[i])-97]+=1
        c2[ord(temp[i])-97]+=1
    if c1==c2:
        return True
    while endp+1<=N2:
        c2[ord(temp[0])-97]-=1
        start+=1
        endp+=1
        temp=s2[start:endp]
        c2[ord(temp[-1])-97]+=1
        if c1==c2:
            return True      
    return False
    
s1 = "abc" 
s2 = "dcba"
print(checkInclusion(s1, s2))