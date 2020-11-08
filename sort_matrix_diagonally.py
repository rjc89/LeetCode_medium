#https://leetcode.com/problems/sort-the-matrix-diagonally/
import numpy as np
from typing import List
import collections
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        d = collections.defaultdict(list)  #default dict doesn't throw a KeyError as it has the default factory value for every key that doesn't exist 
        for i in range(n):
            for j in range(m):
                d[i -j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse = 1)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        print(d, mat)
        return mat

s = Solution()
s.diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]])