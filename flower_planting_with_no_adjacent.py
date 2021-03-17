# https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/717872/Python%3A-Coloring-with-Set-or-12-Lines

from typing import List
from collections import defaultdict

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = [0]*N
        garden = defaultdict(list)
        for src, dst in paths:
            garden[src].append(dst)
            garden[dst].append(src)
        for i in range(1, N+1):
            colors = set([1,2,3,4])
            for neigh in garden[i]:
                if flowers[neigh-1] in colors:
                    colors.remove(flowers[neigh - 1])
            flowers[i - 1] = colors.pop()
        return flowers

s = Solution()
print(s.gardenNoAdj(N = 3, paths = [[1,2],[2,3],[3,1]]))