# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 18:23:40 2017

@author: dell
"""

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        rims = collections.Counter()
        for bricks in wall:
            cnt = 0
            for b in bricks:
                if cnt: rims[cnt] += 1
                cnt += b
        return len(wall) - max(rims.values() or [0])