# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:39:40 2017

@author: dell
"""

def findMinDifference(timePoints):
    def finMinTwo(timePair):    
        t1=timePair[0].split(':')
        t1h,t1m=int(t1[0]),int(t1[1])
        t2=timePair[1].split(':')
        t2h,t2m=int(t2[0]),int(t2[1])
        if t1h==t2h:
            return max(t1m,t2m)-min(t1m,t2m)
        else:
            if t1h>t2h:
                m=(t1h-t2h)*60+(t1m-t2m)
            else:
                m=(-t1h+t2h)*60+(t2m-t1m)
            return min(m,1440-m)
    minmin=1440
    for i in range(len(timePoints)-1):
        for j in range(i+1,len(timePoints)):
            timePair=[timePoints[i],timePoints[j]]
            minmin=min(minmin,finMinTwo(timePair))
    return minmin
            
        
print(findMinDifference(["23:59","12:00","00:00"]))