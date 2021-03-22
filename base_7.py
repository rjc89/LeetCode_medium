# https://leetcode.com/problems/base-7/discuss/898375/Simple-and-Easy-Solution-by-Python-3

class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return str(num)
        
        sign = '-' if num < 0 else ''
        num = abs(num)
        result = []
        while num:
            result.append(str(num % 7))
            num //= 7 
            
        result.append(sign)
        return ''.join(reversed(result))

s = Solution()
print(s.convertToBase7(100))