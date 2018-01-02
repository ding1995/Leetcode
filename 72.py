# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 08:34:19 2017

@author: dell
"""

def minDistance(word1, word2):
    distance=[[1]*(len(word2)+1)]*(len(word1)+1)
    distance[0]=list(range(len(word2)+1))
    distance=list(map(list, zip(*distance)))
    distance[0]=list(range(len(word1)+1))
    for i in range(1,len(word2)+1):
        for j in range(1,len(word1)+1):
            if word1[j-1]==word2[i-1]:
                cost=0                
            else:
                cost=1
            distance[i][j]=min(distance[i-1][j-1]+cost,distance[i-1][j]+1,distance[i][j-1]+1)
    return distance[len(word2)][len(word1)]
    
word1='a'
word2='b'
print(minDistance(word1, word2))