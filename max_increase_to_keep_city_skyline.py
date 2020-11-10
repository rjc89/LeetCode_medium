# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
from typing import List
import itertools
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        M, N, R, C = len(grid), len(grid[0]), [max(r) for r in grid], [max(c) for c in zip(*grid)]
        return sum(min(R[i], C[j]) - grid[i][j] for i, j in itertools.product(range(M), range(N)))
s = Solution()
s.maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])