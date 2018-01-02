# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:08:06 2017

@author: dell
"""

def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r=[[1],[1,1]]
        if numRows==0:
            return []
        if numRows==1:
            return [r[0]]
        for i in range(3,numRows+1):
            temp=[1]
            for j in range(1,i-1):
                temp.append(r[i-2][j]+r[i-2][j-1])
            temp.append(1)
            r.append(temp)
            temp=[1]
        return r

print(generate(5))