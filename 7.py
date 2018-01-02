# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:07:16 2017

@author: dell
"""

def reverse(x):
    s=str(abs(x))
    s=s[::-1]
    if int(s)>2147483648:
        return 0
    if x>=0:
        return int(s)
    else:
        return -int(s)