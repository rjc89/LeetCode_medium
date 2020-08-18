from typing import List

# baseNeg2 is the same as base2
class Solution:
    def base2(self, x):
        res = []
        while x:
            res.append(x & 1)   # & == Bitwise And
            x = x >> 1          # >> == Right Shift    
        return "".join(map(str, res[::-1] or [0]))

    def baseNeg2(self, x):
        res = []
        while x:
            res.append(x & 1)  # & == Bitwise And
            x = -(x >> 1)      # >> == Right Shift
        return "".join(map(str, res[::-1] or [0]))
        
s = Solution()
print(s.baseNeg2(2))