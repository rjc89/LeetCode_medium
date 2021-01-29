# https://leetcode.com/problems/find-right-interval/discuss/815918/Python-O(blogs)-without-binary-search
from typing import List
import operator

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted([(s, i) for i, (s, e) in enumerate(intervals)], key = operator.itemgetter(0))
        ends = sorted([(e, i) for i, (s, e) in enumerate(intervals)], key = operator.itemgetter(0))
        res = [-1 for _ in range(n)]
        sidx = 0
        for end in ends:
            e, i = end
            while starts[sidx][0] < e and sidx + 1 < n:
                sidx += 1
            if starts[sidx][0] < e:
                break
            else:
                res[i] = starts[sidx][1]
        
        return res

s = Solution()
print(s.findRightInterval(intervals = [[1,4],[2,3],[3,4]]))        