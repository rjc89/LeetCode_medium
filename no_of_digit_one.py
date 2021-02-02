# https://leetcode.com/problems/number-of-digit-one/discuss/760282/Easy-intuitive-solution
from typing import List

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 9:
            return 1
        dp = {}
        dp[9] = 1
        i = 9
        
        while i < n + 1:
            dp[i * 10 + 9] = dp[i] * 10 + (i + 1)
            i = i * 10 + 9
        temp = n
        div = 1
        
        while temp//10:
            temp = temp//10
            div = div * 10
        ans = 0
        ans += (n//div) * dp[div - 1]
        if n//div > 1:
            ans += div
        elif n//div == 1:
            ans += (n%div) + 1
        ans += self.countDigitOne(n%div)
        
        return ans

s = Solution()        
print(s.countDigitOne(n = 17))