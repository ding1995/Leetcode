# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 09:59:26 2017

@author: dell
"""

def numberOfArithmeticSlices(A):
    if len(A)<=2:
        return 0
    dif_A=[]
    for i in range(len(A)-1):
        dif_A.append(A[i+1]-A[i])
    count=0
    j=0
    for i in range(len(dif_A)):
        if j==len(dif_A):
            break
        temp=1
        for j in range(i+1,len(dif_A)):
            if dif_A[j]==dif_A[i]:
                temp+=1
            else:
                i=j
                if temp>=2:
                    count+=temp*(temp-1)/2
    if temp>=2:
        count+=temp*(temp-1)/2
    return count

A=[1,2,3,4]
B=[0,1,2,1,0]
print(int(numberOfArithmeticSlices(A)))