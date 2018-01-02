# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 07:40:02 2017

@author: dell
"""
import math
def arrangeCoins(n):
        """
        :type n: int
        :rtype: int
        """
        a_n=abs(n)
        k_test=int(math.sqrt(2*a_n))

        if k_test*(k_test-1)/2<n<k_test*(k_test+1)/2:
                return k_test-1
        if k_test*(k_test+1)/2<=n:
                return k_test
             
print(arrangeCoins(0))