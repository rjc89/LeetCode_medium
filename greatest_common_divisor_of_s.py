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

# while loop solution

class Solution:
    def gcdOfStrings(self, str1, str2):
        s1, s2 = str1, str2
        while s2:
            s1, s2 = s2, s1[:len(s1)%len(s2)]

        if s1*(len(str1)//len(s1)) == str1 and s1*(len(str2)//len(s1)) == str2:
            return s1
        return ""