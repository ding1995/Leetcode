# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 07:48:54 2017

@author: dell
"""

def isPowerOfFour(num):
    if num==0:
        return False
    while(num):
        if num==1:
            return True
        if not num%4:
                num=num/4
        else:
            return False

def isPowerOfFour2(num):
    return (num>0) & ((num & (num-1))==0 ) & ((num & 0x55555555)==num)
    
print(isPowerOfFour2(16))