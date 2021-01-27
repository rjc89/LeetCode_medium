# https://leetcode.com/problems/isomorphic-strings/discuss/943150/Python-3-Dict-Explained
from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mydict = dict()
        val = ""
        for i in range(len(s)):
            if s[i] not in mydict:
                if t[i] not in val:
                    mydict[s[i]] = t[i]
                    val += t[i]
                else:
                    return False
            else:
                if mydict[s[i]] != t[i]:
                    return False
                
        return True

s = Solution()
print(s.isIsomorphic(s = "egg", t = "add"))