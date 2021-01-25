# https://leetcode.com/problems/find-common-characters/discuss/1010839/Python-Solution
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return None
        else:
            freq = Counter(A[0])
            for i in range(1, len(A)):
                for key in freq:
                    freq[key] = min(freq[key], A[i].count(key))
            return freq.elements()

s = Solution()
print(s.commonChars(["bella","label","roller"]))            