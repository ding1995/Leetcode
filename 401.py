# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 08:06:42 2017

@author: dell
"""
import itertools

def readBinaryWatch(num):
    if num==0:
        return ["0:00"]
    ran=[0,1,2,3,4,5,6,7,8,9]
    dec=[8,4,2,1,32,16,8,4,2,1]
    sub=list(itertools.combinations(ran,num))
    result=[]
    for it in sub:     
         hour=0
         minute=0          
         for i in it:
             if i<4:
                 hour+=dec[i]
             else:
                  minute+=dec[i]
         if hour>11 or minute>59:
                 continue
         dis=str(hour)+":"
         if minute<10:
             dis=dis+"0"+str(minute)
         else:
             dis=dis+str(minute)
         result.append(dis)
    return result

print(readBinaryWatch(0))