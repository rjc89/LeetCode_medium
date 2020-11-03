#https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
from typing import List
import collections
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            cache[str(vals)] += 1
            cache[str(trans)] += 1
        print(max(cache.values()))
        return max(cache.values())

s = Solution()
s.maxEqualRowsAfterFlips([[0,1],[1,1]])
        