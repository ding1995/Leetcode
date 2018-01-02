# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:44:05 2017

@author: dell
"""
def findNthDigit(n):
    '''
    strseq=''
    for i in range(1,n+1):
        if len(strseq)<n:
            strseq=strseq+str(i)
        else:
            break
    return int(strseq[n-1])
    '
    count=0
    flag=1
    for i in range(1,n+1):
        if count<n:
            count=count+len(str(i))
        else:
            flag=0
            break
    if flag:
        temp=str(i)    #print(count,i)
        return temp[n-count+len(str(i))-1]
    else:
        temp=str(i-1)    #print(count,i)
        return temp[n-count+len(str(i-1))-1]
    '
    h=int(math.log10(n/9))
    def mul(x,y):
        return 9*x*math.pow(10,y)
    def sum(x,y):
        return x+y
    subseq=list(map(mul,range(1,h+1),range(h)))
    sumsig=reduce(sum,subseq)
    pre=(x-sumsig)/h
    '''
    size,step,begin=1,9,1
    while n>size*step:
        n,size,step,begin=n-size*step,size+1,step*10,begin*10
    return int((str(begin+(n-1)//size))[(n-1)%size])
print(findNthDigit(15))