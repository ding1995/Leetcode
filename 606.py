# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:43:06 2017

@author: dell
"""

class TreeNode(object):
    def __init__(x):
         self.val = x
         self.left = None
         self.right = None
         
def tree2str(t):
    root=t.val
    result=str(root)
    if t.left!=None:
        result+='('+tree2str(t.left)+')'
    if t.right!=None:
        if t.left==None:
            result+='()'
        result+='('+tree2str(t.right)+')'
    return result