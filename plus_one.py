# https://leetcode.com/problems/plus-one/discuss/1034092/Simple-Python-Solution
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

            i -= 1

        digits.insert(0, 1)
        return digits

s = Solution()
print(s.plusOne(digits = [4,3,2,1]))        