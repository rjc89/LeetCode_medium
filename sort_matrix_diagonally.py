#https://leetcode.com/problems/sort-the-matrix-diagonally/
import numpy as np
from typing import List
import collections
import itertools
class Solution:
    def diagonalSort(self, G: List[List[int]]) -> List[List[int]]:
        M, N, D = len(G), len(G[0]), collections.defaultdict(list)
        for i, j in itertools.product(range(M), range(N)):
            D[i-j].append(G[i][j])
        for k in D:
            D[k].sort(reverse = True)
        result = [[D[i-j].pop() for j in range(N)] for i in range(M)]
        return [[D[i-j].pop() for j in range(N)] for i in range(M)]
s = Solution()
s.diagonalSort(G = [[3,3,1,1],[2,2,1,2],[1,1,1,2]])