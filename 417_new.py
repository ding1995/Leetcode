# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:55:08 2017

@author: dell
"""

def pacificAtlantic(matrix):
    edge=len(matrix) 
    if edge==0:
        return []
    width=len(matrix[0])
    P=[[0]*width]*edge
    P[0]=[1]*width
    P=list(map(list, zip(*P)))
    P[0]=[1]*edge
    P=list(map(list, zip(*P)))
    
    A=[[0]*width]*edge
    A[-1]=[1]*width
    A=list(map(list, zip(*A)))
    A[-1]=[1]*edge
    A=list(map(list, zip(*A))) 
    for i in range(1,edge):
        for j in range(1,width):
            P[i][j]=int(((matrix[i][j-1]<=matrix[i][j]) & P[i][j-1] ) or ((matrix[i-1][j]<=matrix[i][j] )& P[i-1][j]))
            A[edge-1-i][width-1-j]=int(((matrix[edge-1-i][width-j]<=matrix[edge-1-i][width-1-j] )& A[edge-1-i][width-j] ) or( (matrix[edge-i][width-1-j]<=matrix[edge-1-i][width-1-j]) & A[edge-i][width-1-j] ))          
    print(P,A)    
    result=[[x,y] for x in range(edge) for y in range(width) if P[x][y]==A[x][y] & A[x][y]==1]
    return result
    
#lis=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
lis=[[1,2,3],[8,9,4],[7,6,5]]
#lis[0:0][0:0]=[0]*edge
print(pacificAtlantic(lis))