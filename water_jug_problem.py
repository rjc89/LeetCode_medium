# https://leetcode.com/problems/water-and-jug-problem/discuss/796582/Python-or-Very-Easyor-No-BFS-DFS

from math import gcd
from typing import List
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if z == x or z == y or z == x + y:
            return True
        return not z % gcd(x, y)

s = Solution()
print(s.canMeasureWater(x = 3, y = 5, z = 4))