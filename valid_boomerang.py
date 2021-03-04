# https://leetcode.com/problems/valid-boomerang/discuss/901005/Python-math-solution-checking-slopes

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x0, y0), (x1, y1), (x2, y2) = points
        return (y2 - y1) * (x0 - x1) != (x2 - x1) * (y0 - y1)

s = Solution()
print(s.isBoomerang(points = [[1,1],[2,3],[3,2]]))        