# https://leetcode.com/problems/nim-game/discuss/847533/Built-in-functions-are-wayyyyy-faster-even-though-the-logic-is-much-more-complicated

class Solution:
    def canWinNim(self, n: int) -> bool:
        b = bin(n)   # bin == binary 
        return b[-1] == '1' or b[-2] == '1'  # compare the last two bits as strings

s = Solution()
print(s.canWinNim(n = 4))