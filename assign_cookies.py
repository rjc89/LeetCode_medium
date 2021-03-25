# https://leetcode.com/problems/assign-cookies/discuss/985308/Python-simple-solution-O(nlogn)-approach

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        ans = 0
        for j in range(len(s)):
            if i < len(g) and s[j] >= g[i]:
                ans = ans + 1
                i = i + 1
            elif i >= len(g):
                break
        return ans
    
s = Solution()
print(s.findContentChildren(g = [1,2,3], s = [1,1]))