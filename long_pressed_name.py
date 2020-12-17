# https://leetcode.com/problems/long-pressed-name/discuss/423955/Python%3A-short-and-easy-%3A)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j = 0
        for i in name:
            try:
                j = typed.index(i, j) + 1   #list.index(element, start, end)
            except ValueError:
                return False
        return True

s = Solution()
s.isLongPressedName(name = "alex", typed = "aaleex")