# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:05:46 2017

@author: dell
"""
import collections
def canConstruct(ransomNote, magazine):
 #   A=len(ransomNote)
 #   B=len(magazine)
  #  if A>B:
 #       return False
    A=collections.Counter(ransomNote)
    B=collections.Counter(magazine)
    for letter in ransomNote:
        if A[letter]>B[letter]:
            return False
    return True

print(canConstruct("aa", "aab"))
