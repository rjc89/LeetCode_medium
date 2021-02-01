# https://leetcode.com/problems/elimination-game/discuss/824126/Python3-3-line-O(logN)
from typing import List

class Solution:
    def lastRemaining(self, n: int) -> int:
        i, di = 0, 2
        for _ in range(n-1):
            if not 0 <= i + di < n:
                i += di//2 if 0 <= i + di//2 < n else -di//2
                di *= -2
            else:
                i += di
                
        return i + 1

s = Solution()
print(s.lastRemaining(n = 9))        