# https://leetcode.com/problems/valid-palindrome/discuss/1050100/Simple-Python-solution


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                new = new + i
                
        return new == new[::-1]
    
s = Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))