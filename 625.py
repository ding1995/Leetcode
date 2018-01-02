# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:28:16 2017

@author: dell
"""

def wordPattern(pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        n_w=str.split()
        if not len(pattern)==len(n_w):
            return False
        dic={}
        dic1={}        
        s=[]
        s1=[]
        count=0
        count1=0
        for i in range(len(n_w)):
            if dic1.get(pattern[i])==None:
                dic1[pattern[i]]=count1
                count1+=1
            s1.append(dic1.get(pattern[i]))  

            if dic.get(n_w[i])==None:
                dic[n_w[i]]=count
                count+=1
            s.append(dic.get(n_w[i]))

        return s==s1        

pattern = "abba"
str = "dog cat cat dog"
print(wordPattern(pattern, str))