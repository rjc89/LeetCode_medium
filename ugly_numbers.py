# https://leetcode.com/problems/ugly-number/discuss/728093/Simple-Python-or-5-Lines
from typing import List

class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        for factor in [2,3,5]:
            while num % factor == 0:
                num //=factor       # x //= 3	x = x // 3
        
        return num == 1

s = Solution()
print(s.isUgly(8))        