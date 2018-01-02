# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:57:56 2017

@author: dell
"""

def nextGreaterElement(n):
    s=list(str(n))
    i=len(s)-1
    while (i>0) & (s[i-1]>=s[i]):
        i=i-1
    if (i==len(s)-1) &(len(s)>1):
        s[i],s[i-1]=s[i-1],s[i]
    elif i==0:
        s.reverse()
    else:
        des=s[i:]
        des.reverse()
        s[:]=s[:i]+des
        j=0
        while (j<len(des)) & (des[j]<=s[i-1]):      
            j=j+1
        s[i-1],s[i+j]=s[i+j],s[i-1]
    r=''.join(s)
    if int(r)>n:
        return int(r)
    else:
        return -1    
    
print(nextGreaterElement(12352))