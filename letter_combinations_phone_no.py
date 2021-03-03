# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/1062185/Python-or-Faster-than-99
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combinations(ans: List[str], t:str):
            a = []
            if not t:
                return ans
            if not ans:
                return [i for i in t]
            
            for i in ans:
                for j in t:
                    a.append(i+j)
            
            return a
        
        s = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        ans = []
        
        for i in digits:
            ans = combinations(ans, s[i])
            
        return ans

s = Solution()
print(s.letterCombinations(digits = "23"))