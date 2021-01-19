# https://leetcode.com/problems/valid-anagram/discuss/890311/Hash-table-with-python%3A-Runtime%3A-24-ms-faster-than-98.88
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
                
        for i in t:
            if i in dic:
                dic[i] -= 1
            else:
                return False
            
        for val in dic.values():
            if val != 0:
                return False
                
        return True


s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))