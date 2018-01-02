# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:27:55 2017

@author: dell
"""

def plusOne(digits):
    cp=1
    for i in range(len(digits)-1,-1,-1):
        new=digits[i]+cp
        if new>9:
            digits[i]=0
        else:
            digits[i]=new            
            cp=0
            break
    if cp==1:
         digits=[1]+digits
    return digits

digits=[0]
print(plusOne(digits))