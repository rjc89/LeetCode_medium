# https://leetcode.com/problems/generate-parentheses/discuss/916464/Python-backtracking-faster-than-98
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(ans, curr, openp, closep, maxp):
            if len(curr) == 2*maxp:
                ans.append(curr)
            if openp < maxp:
                backtrack(ans, curr+'(', openp+1, closep, maxp)
            if closep < openp:
                backtrack(ans, curr+')', openp, closep+1, maxp)
        
        ans = []
        openp, closep = 0, 0
        curr = ''
        backtrack(ans, curr, openp, closep, n)
        return ans

s = Solution()
print(s.generateParenthesis(n = 3))