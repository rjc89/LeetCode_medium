# https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/384620/Python-Solution-or-Euclid's-algorithm-or-10-lines-or-Time-Complexity-greater-95-or-Space-Complexity-greater-100

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1), len(str2)
        if str2_len > str1_len:
            return self.gcdOfStrings(str2, str1)
        
        if str1[:str2_len] == str2:
            if str1_len == str2_len:
                return str2
            
            return self.gcdOfStrings(str2, str1[str2_len:])
        
        return ""